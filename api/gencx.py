# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2025-03-27 12:25:13
# @Last Modified by:   Your name
# @Last Modified time: 2025-03-27 12:30:54

import json

def handler(event, context):
    if event['httpMethod'] == 'POST':
        try:
            body = json.loads(event['body'])
            # 假设传入的 JSON 包含两个数字：'num1' 和 'num2'
            num1 = body.get('num1')
            num2 = body.get('num2')

            if num1 is not None and num2 is not None:
                result = num1 + num2  # 简单的加法计算
                return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': 'application/json'
                    },
                    'body': json.dumps({'result': result})
                }
            else:
                return {
                    'statusCode': 400,
                    'headers': {
                        'Content-Type': 'application/json'
                    },
                    'body': json.dumps({'error': 'Missing "num1" or "num2" in the JSON body'})
                }
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': 'Invalid JSON format in the request body'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': f'Internal Server Error: {str(e)}'})
            }
    else:
        return {
            'statusCode': 405,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Method Not Allowed. Only POST requests are supported.'})
        }

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
