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
