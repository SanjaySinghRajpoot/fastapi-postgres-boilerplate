import re

import httpx

from app.models import models
from datetime import datetime, timedelta
from collections import defaultdict
import asyncio
from fastapi import APIRouter, HTTPException, Path, Request
import os
from bs4 import BeautifulSoup
import requests

def convert_rating_to_int(rating_str: str) -> float:
    try:
        # Example: "4.3 out of 5"
        rating_value = float(rating_str.split("\n")[0])  # Extracts "4.3" and converts to float
        return float(rating_value)  # Converts float to int, truncating decimal
    except (ValueError, IndexError):
        return -1

def extract_asin_from_amazon_url(url):
    """
    Extracts the ASIN from an Amazon product URL.
    
    Args:
        url (str): The Amazon product URL
        
    Returns:
        str: The ASIN if found, None otherwise
    """
    # List of possible ASIN patterns in Amazon URLs
    patterns = [
        r'/dp/([A-Z0-9]{10})',  # Standard /dp/ format
        r'/gp/product/([A-Z0-9]{10})',  # Alternate /gp/product/ format
        r'/product/([A-Z0-9]{10})',  # Shorter product format
        r'/dp/([A-Z0-9]{10})/',  # With trailing slash
        r'/([A-Z0-9]{10})/',  # Sometimes just the ASIN between slashes
        r'[/?&]asin=([A-Z0-9]{10})',  # URL parameter format
        r'[/?&]pd_rd_i=([A-Z0-9]{10})'  # Another common parameter name
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url, re.IGNORECASE)
        if match:
            return match.group(1).upper()  # ASINs are usually uppercase
    
    # If no pattern matched, return None
    return None

def checkDuplicateConversation(product1_url: str, product2_url: str) -> (bool, str): 
    try:
        
        product1_asin = extract_asin_from_amazon_url(product1_url)
        product2_asin = extract_asin_from_amazon_url(product2_url)

        # check if the product details are present in the database or not
        from app.services.db_interaction import DB_service
        db_obj = DB_service()
        
        item1 = db_obj.db.query(models.Item).filter(models.Item.asin_code == product1_asin).first()

        item2 = db_obj.db.query(models.Item).filter(models.Item.asin_code == product2_asin).first()

        if not item1 or not item2:
            return False, ""

        conversation_history = db_obj.db.query(models.ConversationHistory).filter(models.ConversationHistory.product_id_1 == item1.id, models.ConversationHistory.product_id_2 == item2.id).first()

        if not conversation_history:
            return False, ""
        
        return True, conversation_history.llm_response_string


    except Exception as e:
        return False, f"something went wrong {e}"


# In-memory storage for rate limiting (for production, consider using Redis)
request_counts = defaultdict(list)
lock = asyncio.Lock()

async def ip_based_rate_limiter(request: Request):
    """Custom IP-based rate limiter middleware"""
    # Get client IP (handles proxies if needed)
    client_ip = request.client.host
    
    # Rate limit configuration (5 requests per minute)
    max_requests = 3
    time_window = 60  # seconds
    
    async with lock:
        now = datetime.now()
        
        # Remove old requests outside the time window
        request_counts[client_ip] = [
            timestamp for timestamp in request_counts[client_ip]
            if now - timestamp < timedelta(seconds=time_window)
        ]
        
        # Check if limit exceeded
        if len(request_counts[client_ip]) >= max_requests:
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded. Try again in {time_window} seconds."
            )
        
        # Add current request timestamp
        request_counts[client_ip].append(now)
    
    return True