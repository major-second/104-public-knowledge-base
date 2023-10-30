- 前置
  - [[openai-account]]
  - [[curl-wget]]
- [得到key](https://platform.openai.com/account/api-keys)
- [curl使用key](https://platform.openai.com/docs/api-reference/making-requests)
```sh
curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'
```
- 注意`YOUR_API_KEY`记得替换成自己的