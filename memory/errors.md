# Errors

### 2026-04-22T16:39:58.445242 — cycle failure for MSFT
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:39:59.599041 — cycle failure for TSLA
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:02.132053 — cycle failure for AMD
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:12.024142 — cycle failure for ORCL
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:18.690513 — cycle failure for BAC
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:19.072034 — cycle failure for V
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:19.462816 — cycle failure for MA
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:22.412040 — cycle failure for COIN
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:23.906573 — cycle failure for WMT
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:25.684480 — cycle failure for COST
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:26.632722 — cycle failure for HD
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:30.503250 — cycle failure for DIS
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:32.885576 — cycle failure for PLTR
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:35.569127 — cycle failure for SATS
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:37.119486 — cycle failure for VSAT
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:40.970393 — cycle failure for PLUG
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:42.312895 — cycle failure for PI
```
APIError: potential wash trade detected. use complex orders
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 137, in _try_enter
    exchange.submit_stop_loss(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 56, in submit_stop_loss
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: potential wash trade detected. use complex orders
```
### 2026-04-22T16:40:44.099853 — cycle failure for TSEM
```
APIError: insufficient buying power
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 135, in _try_enter
    exchange.submit_market_buy(symbol, qty)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 49, in submit_market_buy
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: insufficient buying power
```
### 2026-04-22T16:40:44.514506 — cycle failure for RCUS
```
APIError: insufficient buying power
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 135, in _try_enter
    exchange.submit_market_buy(symbol, qty)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 49, in submit_market_buy
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: insufficient buying power
```
### 2026-04-22T16:40:46.469224 — cycle failure for YSS
```
APIError: insufficient buying power
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 192, in run_trading_cycle
    if _try_enter(symbol, bars, account):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 135, in _try_enter
    exchange.submit_market_buy(symbol, qty)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 49, in submit_market_buy
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: insufficient buying power
```
### 2026-04-23T17:56:01.905948 — cycle failure for CRM
```
APIError: insufficient qty available for order (requested: 116, available: 0)
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 94, in _manage_open_position
    exchange.close_position(symbol)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 94, in close_position
    return _client().close_position(symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 528, in close_position
    resp = self.delete('/positions/{}'.format(symbol), data=data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 116, available: 0)
```
### 2026-05-04T17:01:17.444156 — cycle failure for AMD
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-05T16:54:35.011102 — cycle failure for WMT
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-07T15:27:19.042340 — cycle failure for ORCL
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-12T15:38:11.536780 — cycle failure for PLTR
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-12T17:37:12.508462 — cycle failure for TSLA
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-12T19:22:05.733567 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-12T19:22:12.715389 — cycle failure for RCUS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T15:40:57.926707 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T15:41:10.172069 — cycle failure for RCUS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T17:50:54.484761 — cycle failure for CRM
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T17:51:02.329810 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T17:51:10.046747 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T17:51:10.873804 — cycle failure for MCD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T17:51:20.363580 — cycle failure for RCUS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T19:48:24.906045 — cycle failure for TSLA
```
APIError: insufficient qty available for order (requested: 3, available: 0)
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 94, in _manage_open_position
    exchange.close_position(symbol)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 94, in close_position
    return _client().close_position(symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 528, in close_position
    resp = self.delete('/positions/{}'.format(symbol), data=data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 3, available: 0)
```
### 2026-05-13T19:48:26.380756 — cycle failure for AMZN
```
APIError: insufficient qty available for order (requested: 4, available: 0)
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 94, in _manage_open_position
    exchange.close_position(symbol)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 94, in close_position
    return _client().close_position(symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 528, in close_position
    resp = self.delete('/positions/{}'.format(symbol), data=data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 4, available: 0)
```
### 2026-05-13T19:48:28.084853 — cycle failure for CRM
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T19:48:29.669936 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T19:48:33.219219 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T19:48:33.762643 — cycle failure for MCD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-13T19:48:37.904756 — cycle failure for RCUS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T15:15:27.404486 — cycle failure for CRM
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T15:15:29.439806 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T15:15:32.336258 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T15:15:32.912428 — cycle failure for MCD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T15:15:35.940986 — cycle failure for RCUS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T17:14:47.345231 — cycle failure for CRM
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T17:14:50.164368 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T17:14:57.058346 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T17:14:57.981121 — cycle failure for MCD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T17:15:08.099527 — cycle failure for RCUS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T19:09:36.466761 — cycle failure for CRM
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T19:09:39.333262 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T19:09:44.637046 — cycle failure for WMT
```
APIError: insufficient qty available for order (requested: 11, available: 0)
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 94, in _manage_open_position
    exchange.close_position(symbol)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 94, in close_position
    return _client().close_position(symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 528, in close_position
    resp = self.delete('/positions/{}'.format(symbol), data=data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 11, available: 0)
```
### 2026-05-14T19:09:45.881823 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T19:09:46.720369 — cycle failure for MCD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-14T19:09:55.960424 — cycle failure for RCUS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T15:11:12.336754 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T15:11:14.553505 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T15:11:15.677843 — cycle failure for DIS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T15:11:15.960039 — cycle failure for UBER
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T15:11:17.673356 — cycle failure for SBAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T15:11:19.873391 — cycle failure for VKTX
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T17:00:59.233970 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T17:01:05.951941 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T17:01:06.843132 — cycle failure for DIS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T17:01:07.221351 — cycle failure for UBER
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T17:01:09.337776 — cycle failure for SBAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T17:01:11.806174 — cycle failure for VKTX
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T18:52:47.997322 — cycle failure for BAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T18:52:49.923400 — cycle failure for HD
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T18:52:50.477605 — cycle failure for NKE
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T18:52:50.745779 — cycle failure for DIS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T18:52:51.186613 — cycle failure for UBER
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T18:52:52.641224 — cycle failure for SBAC
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-15T18:52:54.835417 — cycle failure for VKTX
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-18T16:20:07.437522 — cycle failure for TSLA
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-18T16:20:24.446969 — cycle failure for COIN
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-18T16:20:41.807422 — cycle failure for YSS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-18T18:17:54.528786 — cycle failure for AMZN
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-18T18:18:06.208043 — cycle failure for COIN
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
### 2026-05-18T18:18:07.559482 — cycle failure for WMT
```
APIError: order is already in "filled" state
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 96, in _manage_open_position
    exchange.cancel_order(order.id)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 89, in cancel_order
    _client().cancel_order(order_id)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 492, in cancel_order
    self.delete('/orders/{}'.format(order_id))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 266, in delete
    return self._request('DELETE', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: order is already in "filled" state
```
### 2026-05-18T18:18:22.628013 — cycle failure for YSS
```
APIError: stop_loss.stop_price must be <= base_price - 0.01
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 196, in run_trading_cycle
    committed = _try_enter(symbol, bars, account, remaining_cash)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 136, in _try_enter
    exchange.submit_buy_with_stop(symbol, qty, stop)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 61, in submit_buy_with_stop
    return _client().submit_order(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 433, in submit_order
    resp = self.post('/orders', params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 257, in post
    return self._request('POST', path, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 222, in _request
    return self._one_request(method, url, opts, retry)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 248, in _one_request
    raise_api_error(resp, http_error)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/alpaca_trade_api/rest.py", line 83, in raise_api_error
    raise APIError(error, http_error) from None
alpaca_trade_api.rest.APIError: stop_loss.stop_price must be <= base_price - 0.01
```
