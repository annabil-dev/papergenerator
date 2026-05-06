#!/usr/bin/env python3
"""
Router API Program
Tests the router API connection and sends messages to AI models
Supports both VIOLAGPT and VIOLAGEMINI models
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/home/otomasi/VIOLA/python/.env')

ROUTER_API = os.getenv('ROUTER_API')
ROUTER_API_KEY = os.getenv('ROUTER_API_KEY')
MODELVIOLAGPT = os.getenv('MODELVIOLAGPT')
MODELVIOLAGEMINI = os.getenv('MODELVIOLAGEMINI')

def test_router_connection():
    """Test basic connection to router API"""
    print("=" * 60)
    print("ROUTER API CONNECTION TEST")
    print("=" * 60)
    print(f"Router API URL: {ROUTER_API}")
    print(f"API Key: {ROUTER_API_KEY[:20]}...")
    print()
    
    headers = {
        'Authorization': f'Bearer {ROUTER_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(
            f"{ROUTER_API}/models",
            headers=headers,
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("\n✓ Router API connection successful!")
            return True
        else:
            print(f"\n✗ Router API connection failed: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"\n✗ Error connecting to Router API: {e}")
        return False

def send_message(message, model="VIOLAGPT"):
    """
    Send a message to the specified AI model
    
    Args:
        message (str): The message to send
        model (str): The model to use (VIOLAGPT or VIOLAGEMINI)
    
    Returns:
        dict: Response from the API
    """
    headers = {
        'Authorization': f'Bearer {ROUTER_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    
    try:
        response = requests.post(
            f"{ROUTER_API}/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            # Try to parse as JSON first (non-streaming)
            try:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    return {
                        'success': True,
                        'model': model,
                        'response': result['choices'][0]['message']['content'],
                        'usage': result.get('usage', {})
                    }
            except json.JSONDecodeError:
                # Try to extract first JSON object if there's extra data
                try:
                    text = response.text.strip()
                    brace_count = 0
                    end_idx = 0
                    for i, char in enumerate(text):
                        if char == '{':
                            brace_count += 1
                        elif char == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                end_idx = i + 1
                                break
                    if end_idx > 0:
                        first_json = text[:end_idx]
                        result = json.loads(first_json)
                        if 'choices' in result and len(result['choices']) > 0:
                            return {
                                'success': True,
                                'model': model,
                                'response': result['choices'][0]['message']['content'],
                                'usage': result.get('usage', {})
                            }
                except:
                    pass
            
            # Check if response is streaming (SSE format)
            if 'data:' in response.text:
                full_content = ""
                for line in response.text.split('\n'):
                    if line.startswith('data: '):
                        data = line[6:]
                        if data == '[DONE]':
                            break
                        try:
                            chunk = json.loads(data)
                            if 'choices' in chunk and len(chunk['choices']) > 0:
                                delta = chunk['choices'][0].get('delta', {})
                                if 'content' in delta:
                                    full_content += delta['content']
                                elif 'message' in chunk['choices'][0]:
                                    full_content += chunk['choices'][0]['message'].get('content', '')
                        except json.JSONDecodeError:
                            continue
                
                if full_content:
                    return {
                        'success': True,
                        'model': model,
                        'response': full_content,
                        'usage': {}
                    }
                else:
                    return {
                        'success': False,
                        'error': 'No content in streaming response'
                    }
            else:
                return {
                    'success': False,
                    'error': 'Unknown response format'
                }
        else:
            return {
                'success': False,
                'error': f'API Error: {response.status_code} - {response.text}'
            }
            
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'Request Error: {str(e)}'
        }

def send_message_to_both_models(message):
    """
    Send a message to both VIOLAGPT and VIOLAGEMINI models
    
    Args:
        message (str): The message to send
    
    Returns:
        dict: Responses from both models
    """
    results = {}
    
    # Send to VIOLAGPT
    results[MODELVIOLAGPT] = send_message(message, MODELVIOLAGPT)
    
    # Send to VIOLAGEMINI
    results[MODELVIOLAGEMINI] = send_message(message, MODELVIOLAGEMINI)
    
    return results

def print_results(results):
    """Print the results from both models"""
    for model, result in results.items():
        if result['success']:
            print(f"[{model}]")
            print(result['response'])
            print()
        else:
            print(f"[{model}] Error: {result['error']}")
            print()

def interactive_mode():
    """Run interactive mode - read input and send to both models"""
    print("=" * 60)
    print("INTERACTIVE MODE - Type message and press Enter")
    print("=" * 60)
    print("Commands: 'quit' or 'exit' to stop")
    print()
    
    while True:
        try:
            message = input("You: ").strip()
            
            if not message:
                continue
            
            if message.lower() in ['quit', 'exit', 'q']:
                print("Exiting...")
                break
            
            results = send_message_to_both_models(message)
            print_results(results)
            
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

def show_usage():
    """Show usage instructions"""
    print("=" * 60)
    print("ROUTER API PROGRAM - USAGE")
    print("=" * 60)
    print("\nUsage:")
    print("  python router_api.py [command] [message]")
    print("\nCommands:")
    print("  test              - Test router API connection only")
    print("  send [message]    - Send message to both models")
    print("  interactive       - Interactive mode (read terminal input)")
    print("  (no command)      - Interactive mode")
    print("\nExamples:")
    print("  python router_api.py test")
    print("  python router_api.py send \"Hello, how are you?\"")
    print("  python router_api.py interactive")
    print("  python router_api.py")
    print("=" * 60)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "test":
            test_router_connection()
            
        elif command == "send":
            if len(sys.argv) > 2:
                message = ' '.join(sys.argv[2:])
            else:
                message = "Hello! Please introduce yourself and tell me what you can do."
            
            results = send_message_to_both_models(message)
            print_results(results)
            
        elif command == "interactive":
            if test_router_connection():
                interactive_mode()
            
        elif command in ["help", "-h", "--help"]:
            show_usage()
            
        else:
            message = ' '.join(sys.argv[1:])
            results = send_message_to_both_models(message)
            print_results(results)
    else:
        if test_router_connection():
            interactive_mode()
