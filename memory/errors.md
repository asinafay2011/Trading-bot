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
### 2026-05-19T16:15:47.724849 — cycle failure for DIS
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
### 2026-05-19T16:15:51.447632 — cycle failure for RCUS
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
### 2026-05-19T18:20:51.246522 — cycle failure for V
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
### 2026-05-19T18:20:57.722416 — cycle failure for DIS
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
### 2026-05-19T18:21:01.200787 — cycle failure for QQQ
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
### 2026-05-19T18:21:08.284501 — cycle failure for RCUS
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
### 2026-05-19T18:21:09.084468 — cycle failure for RLAY
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
### 2026-05-20T18:39:15.521435 — cycle failure for GOOGL
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
### 2026-05-20T18:39:21.114195 — cycle failure for V
```
APIError: insufficient qty available for order (requested: 7, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 7, available: 0)
```
### 2026-05-20T18:39:32.228238 — cycle failure for SATS
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
### 2026-05-20T18:39:36.830056 — cycle failure for RCUS
```
APIError: insufficient qty available for order (requested: 95, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 95, available: 0)
```
### 2026-05-21T16:13:53.439570 — cycle failure for ORCL
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
### 2026-05-21T18:14:43.615218 — cycle failure for RCUS
```
APIError: insufficient qty available for order (requested: 105, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 105, available: 0)
```
### 2026-05-22T15:46:40.404053 — cycle failure for TSLA
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
### 2026-05-22T15:46:41.348201 — cycle failure for NVDA
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
### 2026-05-22T15:47:17.561492 — cycle failure for VKTX
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
### 2026-05-22T17:48:42.699547 — cycle failure for TSLA
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
### 2026-05-22T17:48:43.431172 — cycle failure for NVDA
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
### 2026-05-22T17:48:59.344799 — cycle failure for VKTX
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
### 2026-05-22T19:28:28.848979 — cycle failure for MSFT
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
### 2026-05-22T19:28:29.800990 — cycle failure for TSLA
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
### 2026-05-22T19:28:31.013512 — cycle failure for NVDA
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
### 2026-05-22T19:28:51.250699 — cycle failure for SPY
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
### 2026-05-22T19:28:54.831770 — cycle failure for PARR
```
APIError: insufficient qty available for order (requested: 46, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 46, available: 0)
```
### 2026-05-22T19:28:59.941243 — cycle failure for RLAY
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
### 2026-05-22T19:29:04.035128 — discord webhook post failed
```
HTTPError: 503 Server Error: Service Unavailable for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/notifications.py", line 25, in send_discord_message
    response.raise_for_status()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
```
### 2026-05-22T19:29:04.676604 — cycle failure for VKTX
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
### 2026-05-26T16:39:12.076091 — cycle failure for ADBE
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
### 2026-05-26T16:39:17.110789 — cycle failure for JPM
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
### 2026-05-26T19:09:24.088920 — cycle failure for CRM
```
APIError: insufficient qty available for order (requested: 17, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 17, available: 0)
```
### 2026-05-26T19:09:25.035298 — cycle failure for ADBE
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
### 2026-05-26T19:09:28.631113 — cycle failure for BAC
```
APIError: insufficient qty available for order (requested: 58, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 58, available: 0)
```
### 2026-05-26T19:09:35.696081 — cycle failure for COST
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
### 2026-05-26T19:09:41.832935 — cycle failure for NKE
```
APIError: insufficient qty available for order (requested: 62, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 62, available: 0)
```
### 2026-05-26T19:09:46.823045 — cycle failure for PLTR
```
APIError: insufficient qty available for order (requested: 18, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 18, available: 0)
```
### 2026-05-27T16:34:18.818129 — cycle failure for ADBE
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
### 2026-05-27T16:34:23.331095 — cycle failure for COST
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
### 2026-05-27T16:34:29.163774 — cycle failure for SBAC
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
### 2026-05-27T19:04:40.050957 — cycle failure for ADBE
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
### 2026-05-27T19:04:49.842835 — cycle failure for COST
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
### 2026-05-27T19:05:02.330410 — cycle failure for SBAC
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
### 2026-05-28T16:51:09.344984 — cycle failure for ADBE
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
### 2026-05-28T16:51:12.234946 — cycle failure for COST
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
### 2026-05-28T19:33:39.604724 — cycle failure for ADBE
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
### 2026-05-28T19:33:47.790209 — cycle failure for COST
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
### 2026-05-28T19:33:58.548956 — cycle failure for SBAC
```
APIError: insufficient qty available for order (requested: 12, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 12, available: 0)
```
### 2026-05-29T16:40:21.226623 — cycle failure for NVDA
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
### 2026-05-29T19:16:37.238457 — cycle failure for NVDA
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
### 2026-05-29T19:16:44.357957 — cycle failure for V
```
APIError: insufficient qty available for order (requested: 5, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 5, available: 0)
```
### 2026-06-02T17:17:34.449616 — cycle failure for AMD
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
### 2026-06-02T17:17:55.054220 — cycle failure for COST
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
### 2026-06-02T17:18:15.963029 — cycle failure for RLAY
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
### 2026-06-03T17:58:39.619535 — cycle failure for COST
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
### 2026-06-04T18:33:39.668513 — cycle failure for QCOM
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
### 2026-06-04T18:33:48.206624 — cycle failure for COST
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
### 2026-06-04T18:34:02.393076 — cycle failure for PLUG
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
### 2026-06-08T16:45:33.694690 — cycle failure for MSFT
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
### 2026-06-08T16:45:47.274276 — cycle failure for RLAY
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
### 2026-06-08T19:18:15.276490 — cycle failure for MSFT
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
### 2026-06-08T19:18:50.882443 — cycle failure for RLAY
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
### 2026-06-09T15:50:31.208512 — cycle failure for NVDA
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
### 2026-06-09T15:50:31.770434 — cycle failure for AMD
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
### 2026-06-09T15:50:36.034574 — cycle failure for QCOM
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
### 2026-06-09T15:50:42.336167 — cycle failure for NOK
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
### 2026-06-09T15:50:44.411361 — cycle failure for PLUG
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
### 2026-06-09T17:57:20.176548 — cycle failure for NVDA
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
### 2026-06-09T17:57:21.111292 — cycle failure for AMD
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
### 2026-06-09T17:57:24.102533 — cycle failure for NFLX
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
### 2026-06-09T17:57:32.493013 — cycle failure for QCOM
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
### 2026-06-09T17:57:49.018026 — cycle failure for PLTR
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
### 2026-06-09T17:57:51.411249 — cycle failure for NOK
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
### 2026-06-09T17:57:55.263678 — cycle failure for SBAC
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
### 2026-06-09T17:57:58.001795 — cycle failure for PLUG
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
### 2026-06-10T16:31:21.344107 — cycle failure for AAPL
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
### 2026-06-10T16:31:23.566132 — cycle failure for NVDA
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
### 2026-06-10T16:31:24.512469 — cycle failure for AMD
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
### 2026-06-10T16:31:27.572543 — cycle failure for GOOGL
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
### 2026-06-10T16:31:29.241196 — cycle failure for AVGO
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
### 2026-06-10T16:31:33.318783 — cycle failure for QCOM
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
### 2026-06-10T16:31:41.190759 — cycle failure for WMT
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
### 2026-06-10T16:31:51.148031 — cycle failure for NOK
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
### 2026-06-10T16:31:53.196748 — cycle failure for VSAT
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
### 2026-06-10T16:31:55.782350 — cycle failure for PLUG
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
### 2026-06-10T19:19:28.147142 — cycle failure for NVDA
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
### 2026-06-10T19:19:29.076748 — cycle failure for AMD
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
### 2026-06-10T19:19:32.073266 — cycle failure for AVGO
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
### 2026-06-10T19:19:36.706378 — cycle failure for QCOM
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
### 2026-06-10T19:19:47.971174 — cycle failure for DIS
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
### 2026-06-10T19:19:49.388057 — cycle failure for UBER
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
### 2026-06-10T19:19:52.257322 — cycle failure for NOK
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
### 2026-06-10T19:19:56.140524 — cycle failure for PLUG
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
### 2026-06-11T16:49:31.768955 — cycle failure for NVDA
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
### 2026-06-11T16:49:32.791501 — cycle failure for AMD
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
### 2026-06-11T16:49:36.643092 — cycle failure for AVGO
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
### 2026-06-11T16:49:41.208036 — cycle failure for QCOM
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
### 2026-06-11T16:49:55.290386 — cycle failure for NOK
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
### 2026-06-11T16:49:59.184143 — cycle failure for PLUG
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
### 2026-06-11T19:31:55.663251 — cycle failure for NVDA
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
### 2026-06-11T19:31:56.572176 — cycle failure for AMD
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
### 2026-06-11T19:31:58.290818 — cycle failure for AVGO
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
### 2026-06-11T19:32:00.523561 — cycle failure for QCOM
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
### 2026-06-11T19:32:07.510145 — cycle failure for NOK
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
### 2026-06-11T19:32:09.373568 — cycle failure for PLUG
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
### 2026-06-12T16:13:42.580667 — cycle failure for AMD
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
### 2026-06-12T16:13:46.180410 — cycle failure for QCOM
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
### 2026-06-12T16:13:51.892477 — cycle failure for NOK
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
### 2026-06-12T16:13:52.158106 — cycle failure for SATS
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
### 2026-06-12T18:20:24.304599 — cycle failure for AMD
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
### 2026-06-12T18:20:26.305242 — cycle failure for META
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
### 2026-06-12T18:20:34.250941 — cycle failure for ADBE
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
### 2026-06-12T18:20:35.283605 — cycle failure for QCOM
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
### 2026-06-12T18:20:45.914498 — cycle failure for NKE
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
### 2026-06-12T18:20:50.748597 — cycle failure for QQQ
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
### 2026-06-12T18:20:51.751811 — cycle failure for NOK
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
### 2026-06-12T18:20:52.749698 — cycle failure for SATS
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
### 2026-06-12T18:20:56.864354 — cycle failure for PI
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
### 2026-06-15T17:50:45.123395 — cycle failure for AAPL
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
### 2026-06-15T17:50:52.795065 — cycle failure for AMZN
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
### 2026-06-15T17:50:57.002116 — cycle failure for ORCL
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
### 2026-06-15T17:50:58.407507 — cycle failure for CRM
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
### 2026-06-15T17:51:23.809852 — cycle failure for PLUG
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
### 2026-06-16T18:00:07.321843 — cycle failure for QQQ
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
### 2026-06-16T18:00:08.974887 — cycle failure for NOK
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
### 2026-06-16T18:00:15.402569 — cycle failure for TSEM
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
### 2026-06-17T16:35:56.455423 — cycle failure for NFLX
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
### 2026-06-17T19:12:06.516361 — cycle failure for TSLA
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
### 2026-06-17T19:12:10.172782 — cycle failure for AMD
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
### 2026-06-17T19:12:14.847361 — cycle failure for GOOGL
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
### 2026-06-17T19:12:19.737680 — cycle failure for QCOM
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
### 2026-06-18T18:40:54.843431 — cycle failure for GOOGL
```
APIError: insufficient qty available for order (requested: 9, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 9, available: 0)
```
### 2026-06-22T17:27:34.556461 — cycle failure for MSFT
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
### 2026-06-22T17:27:40.516436 — cycle failure for AMZN
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
### 2026-06-22T17:27:41.520803 — cycle failure for NFLX
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
### 2026-06-22T17:27:43.941553 — cycle failure for ORCL
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
### 2026-06-22T17:27:45.660937 — cycle failure for ADBE
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
### 2026-06-22T17:28:00.769657 — cycle failure for PLTR
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
### 2026-06-22T17:28:07.723159 — cycle failure for PARR
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
### 2026-06-23T15:44:53.119319 — cycle failure for ADBE
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
### 2026-06-23T17:30:56.333479 — cycle failure for ADBE
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
### 2026-06-23T17:31:04.701600 — cycle failure for WMT
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
### 2026-06-23T17:31:13.770713 — cycle failure for SPY
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
### 2026-06-23T19:31:30.186668 — cycle failure for AMD
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
### 2026-06-23T19:31:36.429315 — cycle failure for ADBE
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
### 2026-06-23T19:31:37.840519 — cycle failure for QCOM
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
### 2026-06-23T19:31:50.707613 — cycle failure for DIS
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
### 2026-06-24T15:31:25.457109 — cycle failure for ADBE
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
### 2026-06-24T17:31:11.913869 — cycle failure for ADBE
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
### 2026-06-24T19:17:37.217934 — cycle failure for ADBE
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
### 2026-06-25T15:37:28.750224 — cycle failure for ADBE
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
### 2026-06-25T17:33:53.870965 — cycle failure for AVGO
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
### 2026-06-25T17:33:55.620325 — cycle failure for ADBE
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
### 2026-06-25T17:34:03.579166 — cycle failure for COST
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
### 2026-06-25T17:34:05.515205 — cycle failure for MCD
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
### 2026-06-25T17:34:13.108266 — cycle failure for SBAC
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
### 2026-06-25T19:29:47.274636 — cycle failure for ADBE
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
### 2026-06-25T19:29:49.521862 — cycle failure for COST
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
### 2026-06-25T19:29:50.088714 — cycle failure for MCD
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
### 2026-06-26T15:21:16.885469 — cycle failure for AAPL
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
### 2026-06-26T15:21:29.361866 — cycle failure for AVGO
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
### 2026-06-26T15:21:30.330211 — cycle failure for ORCL
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
### 2026-06-26T15:21:32.852110 — cycle failure for QCOM
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
### 2026-06-26T15:21:34.315658 — cycle failure for JPM
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
### 2026-06-26T15:21:36.046105 — cycle failure for BAC
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
### 2026-06-26T15:21:49.289019 — cycle failure for PLTR
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
### 2026-06-26T15:21:50.854043 — cycle failure for QQQ
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
### 2026-06-26T15:21:57.460901 — cycle failure for TSEM
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
### 2026-06-26T17:14:47.832756 — cycle failure for AAPL
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
### 2026-06-26T17:14:50.020170 — cycle failure for AVGO
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
### 2026-06-26T17:14:50.378397 — cycle failure for ORCL
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
### 2026-06-26T17:14:51.554037 — cycle failure for QCOM
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
### 2026-06-26T17:15:03.490179 — cycle failure for PLTR
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
### 2026-06-26T17:15:06.334432 — cycle failure for PARR
```
APIError: insufficient qty available for order (requested: 67, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 67, available: 0)
```
### 2026-06-26T17:15:07.674322 — cycle failure for TSEM
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
### 2026-06-26T19:06:12.919819 — cycle failure for AAPL
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
### 2026-06-26T19:06:20.470196 — cycle failure for AVGO
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
### 2026-06-26T19:06:21.631987 — cycle failure for ORCL
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
### 2026-06-26T19:06:23.711262 — cycle failure for QCOM
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
### 2026-06-26T19:06:24.985292 — cycle failure for JPM
```
APIError: insufficient qty available for order (requested: 10, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 10, available: 0)
```
### 2026-06-26T19:06:30.059814 — cycle failure for HOOD
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
### 2026-06-26T19:06:32.460041 — cycle failure for WMT
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
### 2026-06-26T19:06:37.887239 — cycle failure for UBER
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
### 2026-06-26T19:06:38.901042 — cycle failure for PLTR
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
### 2026-06-26T19:06:40.472564 — cycle failure for QQQ
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
### 2026-06-26T19:06:43.764074 — cycle failure for PARR
```
APIError: insufficient qty available for order (requested: 67, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 67, available: 0)
```
### 2026-06-26T19:06:46.540201 — cycle failure for TSEM
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
### 2026-06-29T16:36:17.133506 — cycle failure for AAPL
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
### 2026-06-29T16:36:23.780389 — cycle failure for WMT
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
### 2026-06-29T16:36:25.388658 — cycle failure for DIS
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
### 2026-06-29T16:36:26.599385 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-06-29T18:32:27.552656 — cycle failure for AAPL
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
### 2026-06-29T18:32:35.596993 — cycle failure for WMT
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
### 2026-06-29T18:32:37.520871 — cycle failure for DIS
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
### 2026-06-29T18:32:39.286802 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-06-30T15:23:46.997306 — cycle failure for AAPL
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
### 2026-06-30T15:23:53.008483 — cycle failure for WMT
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
### 2026-06-30T15:23:55.542270 — cycle failure for DIS
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
### 2026-06-30T15:23:57.332231 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-06-30T17:22:03.523341 — cycle failure for AAPL
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
### 2026-06-30T17:22:08.675219 — cycle failure for HOOD
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
### 2026-06-30T17:22:10.155149 — cycle failure for WMT
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
### 2026-06-30T17:22:11.481625 — cycle failure for DIS
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
### 2026-06-30T17:22:13.506651 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-06-30T19:16:38.347119 — cycle failure for AAPL
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
### 2026-06-30T19:16:43.889334 — cycle failure for HOOD
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
### 2026-06-30T19:16:44.811372 — cycle failure for WMT
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
### 2026-06-30T19:16:46.297671 — cycle failure for DIS
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
### 2026-06-30T19:16:47.860541 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-07-01T15:38:15.397050 — cycle failure for WMT
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
### 2026-07-01T15:38:18.167416 — cycle failure for DIS
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
### 2026-07-01T15:38:20.951646 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-07-01T17:32:56.655753 — cycle failure for WMT
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
### 2026-07-01T17:33:02.445587 — cycle failure for DIS
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
### 2026-07-01T17:33:07.328544 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-07-01T19:23:24.962742 — cycle failure for V
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
### 2026-07-01T19:23:29.511417 — cycle failure for WMT
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
### 2026-07-01T19:23:33.804035 — cycle failure for DIS
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
### 2026-07-01T19:23:38.207873 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-07-02T15:10:52.117728 — cycle failure for WMT
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
### 2026-07-02T15:10:57.167144 — cycle failure for DIS
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
### 2026-07-02T15:11:01.625579 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-07-02T17:00:53.599266 — cycle failure for WMT
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
### 2026-07-02T17:00:55.480120 — cycle failure for DIS
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
### 2026-07-02T17:00:58.620639 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-07-02T18:47:13.976666 — cycle failure for WMT
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
### 2026-07-02T18:47:16.042186 — cycle failure for DIS
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
### 2026-07-02T18:47:18.233188 — cycle failure for SATS
```
APIError: asset "SATS" not found
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
alpaca_trade_api.rest.APIError: asset "SATS" not found
```
### 2026-07-06T16:16:31.373817 — cycle failure for COIN
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
### 2026-07-06T16:16:43.406498 — cycle failure for TSEM
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
### 2026-07-06T16:16:47.563169 — cycle failure for SNDX
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
### 2026-07-06T18:25:30.696197 — cycle failure for MSFT
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
### 2026-07-06T18:25:39.339023 — cycle failure for CRM
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
### 2026-07-06T18:25:57.722297 — cycle failure for TSEM
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
### 2026-07-06T18:26:00.963932 — cycle failure for RLAY
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
### 2026-07-07T15:41:39.281924 — cycle failure for NOK
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
### 2026-07-07T15:41:39.631139 — cycle failure for VSAT
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
### 2026-07-07T15:41:41.126975 — cycle failure for PLUG
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
### 2026-07-07T15:41:41.505760 — cycle failure for TSEM
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
### 2026-07-07T15:41:42.226601 — cycle failure for YSS
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
### 2026-07-07T17:36:41.836454 — cycle failure for NOK
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
### 2026-07-07T17:36:47.621759 — cycle failure for TSEM
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
### 2026-07-07T19:25:14.872690 — cycle failure for NOK
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
### 2026-07-07T19:25:17.834053 — cycle failure for TSEM
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
### 2026-07-08T15:15:37.397052 — cycle failure for NOK
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
### 2026-07-08T15:15:39.996658 — cycle failure for TSEM
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
### 2026-07-08T16:51:30.787106 — cycle failure for NOK
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
### 2026-07-08T16:51:32.236130 — cycle failure for TSEM
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
### 2026-07-08T18:14:32.113700 — cycle failure for NOK
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
### 2026-07-08T18:14:33.588971 — cycle failure for TSEM
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
### 2026-07-08T19:56:13.496275 — cycle failure for NOK
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
### 2026-07-08T19:56:15.247939 — cycle failure for TSEM
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
### 2026-07-09T15:54:12.940008 — cycle failure for NOK
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
### 2026-07-09T15:54:14.878187 — cycle failure for TSEM
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
### 2026-07-09T15:54:16.677071 — cycle failure for VKTX
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
### 2026-07-09T17:51:26.070411 — cycle failure for NOK
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
### 2026-07-09T17:51:27.858313 — cycle failure for TSEM
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
### 2026-07-09T19:37:24.062386 — cycle failure for TSEM
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
### 2026-07-10T15:28:44.370131 — cycle failure for TSLA
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
### 2026-07-10T17:19:52.838544 — cycle failure for TSLA
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
### 2026-07-10T18:57:17.562490 — cycle failure for TSLA
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
### 2026-07-10T18:57:19.211136 — cycle failure for AMD
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
### 2026-07-13T15:41:23.052905 — cycle failure for COST
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
### 2026-07-13T15:41:24.412486 — cycle failure for HD
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
### 2026-07-13T17:36:04.837527 — cycle failure for HOOD
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
### 2026-07-13T17:36:08.192042 — cycle failure for COST
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
### 2026-07-13T17:36:23.567299 — cycle failure for TSEM
```
APIError: insufficient qty available for order (requested: 8, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 8, available: 0)
```
### 2026-07-13T19:03:16.225177 — cycle failure for TSEM
```
APIError: insufficient qty available for order (requested: 8, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 8, available: 0)
```
### 2026-07-14T14:44:58.800574 — cycle failure for AAPL
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
### 2026-07-14T14:45:09.945180 — cycle failure for CRM
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
### 2026-07-14T14:45:18.815700 — cycle failure for COST
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
### 2026-07-14T14:45:25.013234 — cycle failure for QQQ
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
### 2026-07-14T14:45:36.922112 — cycle failure for YSS
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
### 2026-07-14T16:03:48.719625 — cycle failure for JPM
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
### 2026-07-14T16:03:53.616675 — cycle failure for COST
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
### 2026-07-14T17:33:28.939425 — cycle failure for CRM
```
APIError: insufficient qty available for order (requested: 14, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 14, available: 0)
```
### 2026-07-14T17:33:33.576354 — cycle failure for COST
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
### 2026-07-14T17:33:40.047628 — cycle failure for VSAT
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
### 2026-07-14T18:46:16.560758 — cycle failure for CRM
```
APIError: insufficient qty available for order (requested: 14, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 14, available: 0)
```
### 2026-07-14T18:46:23.616527 — cycle failure for COST
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
### 2026-07-15T14:44:40.738472 — cycle failure for COST
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
### 2026-07-15T16:09:01.799742 — cycle failure for COST
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
### 2026-07-15T17:37:26.130084 — cycle failure for COST
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
### 2026-07-15T18:44:56.740789 — cycle failure for CRM
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
### 2026-07-15T18:45:03.977504 — cycle failure for COST
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
### 2026-07-15T19:54:23.559133 — cycle failure for COST
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
### 2026-07-15T19:54:27.125458 — cycle failure for UBER
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
### 2026-07-15T19:54:32.118119 — cycle failure for SBAC
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
### 2026-07-17T14:28:45.468109 — cycle failure for QCOM
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
### 2026-07-17T14:28:47.576674 — cycle failure for HOOD
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
### 2026-07-17T14:28:48.554081 — cycle failure for COST
```
APIError: insufficient qty available for order (requested: 2, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 2, available: 0)
```
### 2026-07-17T15:56:52.155137 — cycle failure for QCOM
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
### 2026-07-17T15:56:54.751429 — cycle failure for HOOD
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
### 2026-07-17T15:56:55.956082 — cycle failure for COST
```
APIError: insufficient qty available for order (requested: 2, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 2, available: 0)
```
### 2026-07-17T15:56:58.061886 — cycle failure for DIS
```
APIError: insufficient qty available for order (requested: 27, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 27, available: 0)
```
### 2026-07-17T17:10:09.690681 — cycle failure for QCOM
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
### 2026-07-17T17:10:15.792125 — cycle failure for HOOD
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
### 2026-07-17T17:10:18.064958 — cycle failure for COST
```
APIError: insufficient qty available for order (requested: 2, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 2, available: 0)
```
### 2026-07-17T17:10:21.924178 — cycle failure for DIS
```
APIError: insufficient qty available for order (requested: 27, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 27, available: 0)
```
### 2026-07-17T17:10:39.757791 — cycle failure for SNDX
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
### 2026-07-17T18:16:25.957651 — cycle failure for QCOM
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
### 2026-07-17T18:16:28.271905 — cycle failure for HOOD
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
### 2026-07-17T18:16:31.033390 — cycle failure for COST
```
APIError: insufficient qty available for order (requested: 2, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 2, available: 0)
```
### 2026-07-17T18:16:32.845085 — cycle failure for DIS
```
APIError: insufficient qty available for order (requested: 27, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 27, available: 0)
```
### 2026-07-17T19:39:15.086053 — cycle failure for QCOM
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
### 2026-07-17T19:39:19.885355 — cycle failure for HOOD
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
### 2026-07-17T19:39:22.210334 — cycle failure for COST
```
APIError: insufficient qty available for order (requested: 2, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 2, available: 0)
```
### 2026-07-17T19:39:26.370236 — cycle failure for DIS
```
APIError: insufficient qty available for order (requested: 27, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 27, available: 0)
```
### 2026-07-17T19:39:39.528300 — cycle failure for RLAY
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
### 2026-07-20T15:07:42.858882 — cycle failure for PI
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
### 2026-07-20T15:07:44.128244 — cycle failure for TSEM
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
### 2026-07-20T15:07:47.943901 — cycle failure for SNDX
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
### 2026-07-20T15:07:49.697713 — cycle failure for YSS
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
### 2026-07-20T16:43:19.953478 — cycle failure for MSFT
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
### 2026-07-20T16:43:34.297377 — cycle failure for MA
```
APIError: insufficient qty available for order (requested: 5, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 5, available: 0)
```
### 2026-07-20T16:43:37.322020 — cycle failure for HD
```
APIError: insufficient qty available for order (requested: 7, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 7, available: 0)
```
### 2026-07-20T16:43:39.572032 — cycle failure for NKE
```
APIError: insufficient qty available for order (requested: 56, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 56, available: 0)
```
### 2026-07-20T16:43:46.781623 — cycle failure for SBAC
```
APIError: insufficient qty available for order (requested: 12, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 12, available: 0)
```
### 2026-07-20T16:43:52.349220 — cycle failure for SNDX
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
### 2026-07-20T16:43:53.954567 — cycle failure for YSS
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
### 2026-07-20T18:33:07.716812 — cycle failure for MA
```
APIError: insufficient qty available for order (requested: 5, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 5, available: 0)
```
### 2026-07-20T18:33:08.819969 — cycle failure for HD
```
APIError: insufficient qty available for order (requested: 7, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 7, available: 0)
```
### 2026-07-20T18:33:09.361116 — cycle failure for NKE
```
APIError: insufficient qty available for order (requested: 56, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 56, available: 0)
```
### 2026-07-20T18:33:12.594306 — cycle failure for SBAC
```
APIError: insufficient qty available for order (requested: 12, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 12, available: 0)
```
### 2026-07-20T18:33:14.866214 — cycle failure for SNDX
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
### 2026-07-20T18:33:15.296081 — cycle failure for YSS
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
### 2026-07-21T15:00:13.176015 — cycle failure for TSLA
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
### 2026-07-21T15:00:16.342475 — cycle failure for AMD
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
### 2026-07-21T15:00:31.934463 — cycle failure for HOOD
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
### 2026-07-21T16:36:13.075802 — cycle failure for AAPL
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
### 2026-07-21T16:36:14.512416 — cycle failure for TSLA
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
### 2026-07-21T16:36:15.467970 — cycle failure for AMD
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
### 2026-07-21T16:36:26.416663 — cycle failure for HOOD
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
### 2026-07-21T16:36:37.324958 — cycle failure for SBAC
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
### 2026-07-21T17:58:25.207537 — cycle failure for TSLA
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
### 2026-07-21T17:58:31.271484 — cycle failure for HOOD
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
### 2026-07-21T19:35:24.637648 — cycle failure for TSLA
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
### 2026-07-21T19:35:25.519200 — cycle failure for AMD
```
APIError: stop price must be less than current price
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 115, in _manage_open_position
    exchange.submit_stop_loss(symbol, qty, entry_price)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 74, in submit_stop_loss
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
alpaca_trade_api.rest.APIError: stop price must be less than current price
```
### 2026-07-21T19:35:32.307573 — cycle failure for HOOD
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
### 2026-07-22T15:00:32.665995 — cycle failure for TSLA
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
### 2026-07-22T15:00:41.808872 — cycle failure for HOOD
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
### 2026-07-22T16:43:19.768610 — cycle failure for TSLA
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
### 2026-07-22T16:43:28.303935 — cycle failure for HOOD
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
### 2026-07-22T17:54:06.637462 — cycle failure for TSLA
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
### 2026-07-22T17:54:11.688526 — cycle failure for HOOD
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
### 2026-07-22T19:06:16.047660 — cycle failure for TSLA
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
### 2026-07-22T19:06:32.389103 — cycle failure for MA
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
### 2026-07-22T19:06:33.356299 — cycle failure for HOOD
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
### 2026-07-22T19:06:46.369233 — cycle failure for VSAT
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
### 2026-07-23T15:04:08.908336 — cycle failure for TSLA
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
### 2026-07-23T15:04:22.231177 — cycle failure for HOOD
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
### 2026-07-23T16:44:40.761140 — cycle failure for TSLA
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
### 2026-07-23T16:44:41.684215 — discord webhook post failed
```
HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
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

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/notifications.py", line 25, in send_discord_message
    response.raise_for_status()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
```
### 2026-07-23T16:44:46.017074 — discord webhook post failed
```
HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/notifications.py", line 25, in send_discord_message
    response.raise_for_status()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
```
### 2026-07-23T16:44:51.693813 — discord webhook post failed
```
HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/notifications.py", line 25, in send_discord_message
    response.raise_for_status()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
```
### 2026-07-23T16:44:53.945365 — cycle failure for HOOD
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
### 2026-07-23T18:02:07.736520 — cycle failure for TSLA
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
### 2026-07-23T18:02:29.062694 — discord webhook post failed
```
ReadTimeout: HTTPSConnectionPool(host='discord.com', port=443): Read timed out. (read timeout=10)
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 468, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 463, in _make_request
    httplib_response = conn.getresponse()
                       ^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/http/client.py", line 1450, in getresponse
    response.begin()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/http/client.py", line 336, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/http/client.py", line 297, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/socket.py", line 720, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/ssl.py", line 1251, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/ssl.py", line 1103, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TimeoutError: The read operation timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/adapters.py", line 696, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 802, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/util/retry.py", line 552, in increment
    raise six.reraise(type(error), error, _stacktrace)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/packages/six.py", line 770, in reraise
    raise value
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 716, in urlopen
    httplib_response = self._make_request(
                       ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 470, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 358, in _raise_timeout
    raise ReadTimeoutError(
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='discord.com', port=443): Read timed out. (read timeout=10)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/notifications.py", line 24, in send_discord_message
    response = requests.post(webhook, json={"content": text}, timeout=10)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/api.py", line 134, in post
    return request("post", url, data=data, json=json, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/api.py", line 71, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/sessions.py", line 651, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/sessions.py", line 784, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/adapters.py", line 742, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='discord.com', port=443): Read timed out. (read timeout=10)
```
### 2026-07-23T18:02:33.187897 — discord webhook post failed
```
HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/notifications.py", line 25, in send_discord_message
    response.raise_for_status()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
```
### 2026-07-23T18:02:34.902970 — cycle failure for HOOD
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
### 2026-07-23T18:02:43.604402 — discord webhook post failed
```
HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
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

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/notifications.py", line 25, in send_discord_message
    response.raise_for_status()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: https://discord.com/api/webhooks/1495973356225167492/L8IeO-sbKGOJ3lzZfNTGzKswSHMRdL_zR3aIsXOKzfsIw4dymhssJq3WoABtOllj6rUy
```
### 2026-07-23T19:44:27.359993 — cycle failure for TSLA
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
### 2026-07-23T19:44:36.701679 — cycle failure for HOOD
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
### 2026-07-24T14:50:14.656089 — cycle failure for TSLA
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
### 2026-07-24T14:50:23.925703 — cycle failure for ORCL
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
### 2026-07-24T14:50:30.469833 — cycle failure for HOOD
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
### 2026-07-24T14:50:37.629608 — cycle failure for UBER
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
### 2026-07-24T14:50:44.827199 — cycle failure for SBAC
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
### 2026-07-24T16:33:58.361900 — cycle failure for TSLA
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
### 2026-07-24T16:34:03.219747 — cycle failure for AVGO
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
### 2026-07-24T16:34:03.906725 — cycle failure for ORCL
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
### 2026-07-24T16:34:09.070833 — cycle failure for MA
```
APIError: stop price must be less than current price
Traceback (most recent call last):
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 184, in run_trading_cycle
    _manage_open_position(symbol, position, bars, account)
  File "/home/runner/work/Trading-bot/Trading-bot/bot.py", line 115, in _manage_open_position
    exchange.submit_stop_loss(symbol, qty, entry_price)
  File "/home/runner/work/Trading-bot/Trading-bot/exchange.py", line 74, in submit_stop_loss
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
alpaca_trade_api.rest.APIError: stop price must be less than current price
```
### 2026-07-24T16:34:09.678569 — cycle failure for HOOD
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
### 2026-07-24T16:34:15.803616 — cycle failure for UBER
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
### 2026-07-24T16:34:21.623727 — cycle failure for SBAC
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
### 2026-07-24T17:58:14.007712 — cycle failure for TSLA
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
### 2026-07-24T17:58:22.497221 — cycle failure for ORCL
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
### 2026-07-24T17:58:31.355368 — cycle failure for HOOD
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
### 2026-07-24T17:58:39.310043 — cycle failure for UBER
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
### 2026-07-24T17:58:46.771467 — cycle failure for SBAC
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
### 2026-07-24T19:27:19.202282 — cycle failure for TSLA
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
### 2026-07-24T19:27:27.686302 — cycle failure for ORCL
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
### 2026-07-24T19:27:34.769602 — cycle failure for HOOD
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
### 2026-07-24T19:27:45.033117 — cycle failure for UBER
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
### 2026-07-24T19:27:52.125256 — cycle failure for SBAC
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
### 2026-07-27T15:38:49.707130 — cycle failure for NVDA
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
### 2026-07-27T15:38:59.452526 — cycle failure for V
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
### 2026-07-27T15:39:01.000633 — cycle failure for HOOD
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
### 2026-07-27T15:39:07.265864 — cycle failure for UBER
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
### 2026-07-27T17:21:31.886576 — cycle failure for NVDA
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
### 2026-07-27T17:21:39.642728 — cycle failure for HOOD
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
### 2026-07-27T17:21:43.445593 — cycle failure for UBER
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
### 2026-07-27T18:54:04.050865 — cycle failure for NVDA
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
### 2026-07-27T18:54:13.090271 — cycle failure for V
```
APIError: insufficient qty available for order (requested: 7, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 7, available: 0)
```
### 2026-07-27T18:54:14.453141 — cycle failure for HOOD
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
### 2026-07-27T18:54:18.992910 — cycle failure for UBER
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
### 2026-07-28T15:16:02.706079 — cycle failure for TSLA
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
### 2026-07-28T15:16:03.689350 — cycle failure for NVDA
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
### 2026-07-28T15:16:08.476585 — cycle failure for ORCL
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
### 2026-07-28T15:16:09.539120 — cycle failure for QCOM
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
### 2026-07-28T15:16:18.789948 — cycle failure for TSEM
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
### 2026-07-28T15:16:20.235601 — cycle failure for VKTX
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
### 2026-07-28T16:57:18.506757 — cycle failure for TSLA
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
### 2026-07-28T16:57:18.847379 — cycle failure for NVDA
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
### 2026-07-28T16:57:22.441088 — cycle failure for ORCL
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
### 2026-07-28T16:57:23.565235 — cycle failure for QCOM
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
### 2026-07-28T16:57:28.192630 — cycle failure for SBAC
```
APIError: insufficient qty available for order (requested: 12, available: 0)
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
alpaca_trade_api.rest.APIError: insufficient qty available for order (requested: 12, available: 0)
```
### 2026-07-28T16:57:29.402065 — cycle failure for TSEM
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
### 2026-07-28T16:57:30.414254 — cycle failure for VKTX
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
