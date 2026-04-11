# Interface CookieStore

**Source:** `java.base\java\net\CookieStore.html`

### Class Description

```java
public interface
CookieStore
```

A CookieStore object represents a storage for cookie. Can store and retrieve
cookies.

CookieManager

will call

CookieStore.add

to save cookies
for every incoming HTTP response, and call

CookieStore.get

to
retrieve cookie for every outgoing HTTP request. A CookieStore
is responsible for removing HttpCookie instances which have expired.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void add​(
URI
uri,

HttpCookie
cookie)

Adds one HTTP cookie to the store. This is called for every
incoming HTTP response.

A cookie to store may or may not be associated with an URI. If it
is not associated with an URI, the cookie's domain and path attribute
will indicate where it comes from. If it is associated with an URI and
its domain and path attribute are not specified, given URI will indicate
where this cookie comes from.

If a cookie corresponding to the given URI already exists,
then it is replaced with the new one.

**Parameters:**
- uri

- the uri this cookie associated with.
if

null

, this cookie will not be associated
with an URI
- cookie

- the cookie to store

**Throws:**
- NullPointerException

- if

cookie

is

null

**See Also:**
- get(java.net.URI)

---

#### List
<
HttpCookie
> get​(
URI
uri)

Retrieve cookies associated with given URI, or whose domain matches the
given URI. Only cookies that have not expired are returned.
This is called for every outgoing HTTP request.

**Parameters:**
- uri

- the uri associated with the cookies to be returned

**Returns:**
- an immutable list of HttpCookie,
return empty list if no cookies match the given URI

**Throws:**
- NullPointerException

- if

uri

is

null

**See Also:**
- add(java.net.URI, java.net.HttpCookie)

---

#### List
<
HttpCookie
> getCookies()

Get all not-expired cookies in cookie store.

**Returns:**
- an immutable list of http cookies;
return empty list if there's no http cookie in store

---

#### List
<
URI
> getURIs()

Get all URIs which identify the cookies in this cookie store.

**Returns:**
- an immutable list of URIs;
return empty list if no cookie in this cookie store
is associated with an URI

---

#### boolean remove​(
URI
uri,

HttpCookie
cookie)

Remove a cookie from store.

**Parameters:**
- uri

- the uri this cookie associated with.
if

null

, the cookie to be removed is not associated
with an URI when added; if not

null

, the cookie
to be removed is associated with the given URI when added.
- cookie

- the cookie to remove

**Returns:**
- true

if this store contained the specified cookie

**Throws:**
- NullPointerException

- if

cookie

is

null

---

#### boolean removeAll()

Remove all cookies in this cookie store.

**Returns:**
- true

if this store changed as a result of the call

---

### Additional Sections

#### Interface CookieStore

```java
public interface
CookieStore
```

A CookieStore object represents a storage for cookie. Can store and retrieve
cookies.

CookieManager

will call

CookieStore.add

to save cookies
for every incoming HTTP response, and call

CookieStore.get

to
retrieve cookie for every outgoing HTTP request. A CookieStore
is responsible for removing HttpCookie instances which have expired.

**Since:** 1.6

public interface

CookieStore

A CookieStore object represents a storage for cookie. Can store and retrieve
cookies.

CookieManager

will call

CookieStore.add

to save cookies
for every incoming HTTP response, and call

CookieStore.get

to
retrieve cookie for every outgoing HTTP request. A CookieStore
is responsible for removing HttpCookie instances which have expired.

CookieManager

will call

CookieStore.add

to save cookies
for every incoming HTTP response, and call

CookieStore.get

to
retrieve cookie for every outgoing HTTP request. A CookieStore
is responsible for removing HttpCookie instances which have expired.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

URI

uri,

HttpCookie

cookie)

Adds one HTTP cookie to the store.

List

<

HttpCookie

>

get

​(

URI

uri)

Retrieve cookies associated with given URI, or whose domain matches the
given URI.

List

<

HttpCookie

>

getCookies

()

Get all not-expired cookies in cookie store.

List

<

URI

>

getURIs

()

Get all URIs which identify the cookies in this cookie store.

boolean

remove

​(

URI

uri,

HttpCookie

cookie)

Remove a cookie from store.

boolean

removeAll

()

Remove all cookies in this cookie store.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

URI

uri,

HttpCookie

cookie)

Adds one HTTP cookie to the store.

List

<

HttpCookie

>

get

​(

URI

uri)

Retrieve cookies associated with given URI, or whose domain matches the
given URI.

List

<

HttpCookie

>

getCookies

()

Get all not-expired cookies in cookie store.

List

<

URI

>

getURIs

()

Get all URIs which identify the cookies in this cookie store.

boolean

remove

​(

URI

uri,

HttpCookie

cookie)

Remove a cookie from store.

boolean

removeAll

()

Remove all cookies in this cookie store.

---

#### Method Summary

Adds one HTTP cookie to the store.

Retrieve cookies associated with given URI, or whose domain matches the
given URI.

Get all not-expired cookies in cookie store.

Get all URIs which identify the cookies in this cookie store.

Remove a cookie from store.

Remove all cookies in this cookie store.

============ METHOD DETAIL ==========

- Method Detail

- add

```java
void add​(
URI
uri,

HttpCookie
cookie)
```

Adds one HTTP cookie to the store. This is called for every
incoming HTTP response.

A cookie to store may or may not be associated with an URI. If it
is not associated with an URI, the cookie's domain and path attribute
will indicate where it comes from. If it is associated with an URI and
its domain and path attribute are not specified, given URI will indicate
where this cookie comes from.

If a cookie corresponding to the given URI already exists,
then it is replaced with the new one.

**Parameters:** uri

- the uri this cookie associated with.
if

null

, this cookie will not be associated
with an URI
**Parameters:** cookie

- the cookie to store
**Throws:** NullPointerException

- if

cookie

is

null
**See Also:** get(java.net.URI)

- get

```java
List
<
HttpCookie
> get​(
URI
uri)
```

Retrieve cookies associated with given URI, or whose domain matches the
given URI. Only cookies that have not expired are returned.
This is called for every outgoing HTTP request.

**Parameters:** uri

- the uri associated with the cookies to be returned
**Returns:** an immutable list of HttpCookie,
return empty list if no cookies match the given URI
**Throws:** NullPointerException

- if

uri

is

null
**See Also:** add(java.net.URI, java.net.HttpCookie)

- getCookies

```java
List
<
HttpCookie
> getCookies()
```

Get all not-expired cookies in cookie store.

**Returns:** an immutable list of http cookies;
return empty list if there's no http cookie in store

- getURIs

```java
List
<
URI
> getURIs()
```

Get all URIs which identify the cookies in this cookie store.

**Returns:** an immutable list of URIs;
return empty list if no cookie in this cookie store
is associated with an URI

- remove

```java
boolean remove​(
URI
uri,

HttpCookie
cookie)
```

Remove a cookie from store.

**Parameters:** uri

- the uri this cookie associated with.
if

null

, the cookie to be removed is not associated
with an URI when added; if not

null

, the cookie
to be removed is associated with the given URI when added.
**Parameters:** cookie

- the cookie to remove
**Returns:** true

if this store contained the specified cookie
**Throws:** NullPointerException

- if

cookie

is

null

- removeAll

```java
boolean removeAll()
```

Remove all cookies in this cookie store.

**Returns:** true

if this store changed as a result of the call

Method Detail

- add

```java
void add​(
URI
uri,

HttpCookie
cookie)
```

Adds one HTTP cookie to the store. This is called for every
incoming HTTP response.

A cookie to store may or may not be associated with an URI. If it
is not associated with an URI, the cookie's domain and path attribute
will indicate where it comes from. If it is associated with an URI and
its domain and path attribute are not specified, given URI will indicate
where this cookie comes from.

If a cookie corresponding to the given URI already exists,
then it is replaced with the new one.

**Parameters:** uri

- the uri this cookie associated with.
if

null

, this cookie will not be associated
with an URI
**Parameters:** cookie

- the cookie to store
**Throws:** NullPointerException

- if

cookie

is

null
**See Also:** get(java.net.URI)

- get

```java
List
<
HttpCookie
> get​(
URI
uri)
```

Retrieve cookies associated with given URI, or whose domain matches the
given URI. Only cookies that have not expired are returned.
This is called for every outgoing HTTP request.

**Parameters:** uri

- the uri associated with the cookies to be returned
**Returns:** an immutable list of HttpCookie,
return empty list if no cookies match the given URI
**Throws:** NullPointerException

- if

uri

is

null
**See Also:** add(java.net.URI, java.net.HttpCookie)

- getCookies

```java
List
<
HttpCookie
> getCookies()
```

Get all not-expired cookies in cookie store.

**Returns:** an immutable list of http cookies;
return empty list if there's no http cookie in store

- getURIs

```java
List
<
URI
> getURIs()
```

Get all URIs which identify the cookies in this cookie store.

**Returns:** an immutable list of URIs;
return empty list if no cookie in this cookie store
is associated with an URI

- remove

```java
boolean remove​(
URI
uri,

HttpCookie
cookie)
```

Remove a cookie from store.

**Parameters:** uri

- the uri this cookie associated with.
if

null

, the cookie to be removed is not associated
with an URI when added; if not

null

, the cookie
to be removed is associated with the given URI when added.
**Parameters:** cookie

- the cookie to remove
**Returns:** true

if this store contained the specified cookie
**Throws:** NullPointerException

- if

cookie

is

null

- removeAll

```java
boolean removeAll()
```

Remove all cookies in this cookie store.

**Returns:** true

if this store changed as a result of the call

---

#### Method Detail

add

```java
void add​(
URI
uri,

HttpCookie
cookie)
```

Adds one HTTP cookie to the store. This is called for every
incoming HTTP response.

A cookie to store may or may not be associated with an URI. If it
is not associated with an URI, the cookie's domain and path attribute
will indicate where it comes from. If it is associated with an URI and
its domain and path attribute are not specified, given URI will indicate
where this cookie comes from.

If a cookie corresponding to the given URI already exists,
then it is replaced with the new one.

**Parameters:** uri

- the uri this cookie associated with.
if

null

, this cookie will not be associated
with an URI
**Parameters:** cookie

- the cookie to store
**Throws:** NullPointerException

- if

cookie

is

null
**See Also:** get(java.net.URI)

---

#### add

void add​(

URI

uri,

HttpCookie

cookie)

Adds one HTTP cookie to the store. This is called for every
incoming HTTP response.

A cookie to store may or may not be associated with an URI. If it
is not associated with an URI, the cookie's domain and path attribute
will indicate where it comes from. If it is associated with an URI and
its domain and path attribute are not specified, given URI will indicate
where this cookie comes from.

If a cookie corresponding to the given URI already exists,
then it is replaced with the new one.

A cookie to store may or may not be associated with an URI. If it
is not associated with an URI, the cookie's domain and path attribute
will indicate where it comes from. If it is associated with an URI and
its domain and path attribute are not specified, given URI will indicate
where this cookie comes from.

If a cookie corresponding to the given URI already exists,
then it is replaced with the new one.

If a cookie corresponding to the given URI already exists,
then it is replaced with the new one.

get

```java
List
<
HttpCookie
> get​(
URI
uri)
```

Retrieve cookies associated with given URI, or whose domain matches the
given URI. Only cookies that have not expired are returned.
This is called for every outgoing HTTP request.

**Parameters:** uri

- the uri associated with the cookies to be returned
**Returns:** an immutable list of HttpCookie,
return empty list if no cookies match the given URI
**Throws:** NullPointerException

- if

uri

is

null
**See Also:** add(java.net.URI, java.net.HttpCookie)

---

#### get

List

<

HttpCookie

> get​(

URI

uri)

Retrieve cookies associated with given URI, or whose domain matches the
given URI. Only cookies that have not expired are returned.
This is called for every outgoing HTTP request.

getCookies

```java
List
<
HttpCookie
> getCookies()
```

Get all not-expired cookies in cookie store.

**Returns:** an immutable list of http cookies;
return empty list if there's no http cookie in store

---

#### getCookies

List

<

HttpCookie

> getCookies()

Get all not-expired cookies in cookie store.

getURIs

```java
List
<
URI
> getURIs()
```

Get all URIs which identify the cookies in this cookie store.

**Returns:** an immutable list of URIs;
return empty list if no cookie in this cookie store
is associated with an URI

---

#### getURIs

List

<

URI

> getURIs()

Get all URIs which identify the cookies in this cookie store.

remove

```java
boolean remove​(
URI
uri,

HttpCookie
cookie)
```

Remove a cookie from store.

**Parameters:** uri

- the uri this cookie associated with.
if

null

, the cookie to be removed is not associated
with an URI when added; if not

null

, the cookie
to be removed is associated with the given URI when added.
**Parameters:** cookie

- the cookie to remove
**Returns:** true

if this store contained the specified cookie
**Throws:** NullPointerException

- if

cookie

is

null

---

#### remove

boolean remove​(

URI

uri,

HttpCookie

cookie)

Remove a cookie from store.

removeAll

```java
boolean removeAll()
```

Remove all cookies in this cookie store.

**Returns:** true

if this store changed as a result of the call

---

#### removeAll

boolean removeAll()

Remove all cookies in this cookie store.

---

