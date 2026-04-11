# Interface CookiePolicy

**Source:** `java.base\java\net\CookiePolicy.html`

### Class Description

```java
public interface
CookiePolicy
```

CookiePolicy implementations decide which cookies should be accepted
and which should be rejected. Three pre-defined policy implementations
are provided, namely ACCEPT_ALL, ACCEPT_NONE and ACCEPT_ORIGINAL_SERVER.

See RFC 2965 sec. 3.3 and 7 for more detail.

**Since:** 1.6

---

### Field Details

#### static final
CookiePolicy
ACCEPT_ALL

One pre-defined policy which accepts all cookies.

---

#### static final
CookiePolicy
ACCEPT_NONE

One pre-defined policy which accepts no cookies.

---

#### static final
CookiePolicy
ACCEPT_ORIGINAL_SERVER

One pre-defined policy which only accepts cookies from original server.

---

### Constructor Details

*No entries found.*

### Method Details

#### boolean shouldAccept​(
URI
uri,

HttpCookie
cookie)

Will be called to see whether or not this cookie should be accepted.

**Parameters:**
- uri

- the URI to consult accept policy with
- cookie

- the HttpCookie object in question

**Returns:**
- true

if this cookie should be accepted;
otherwise,

false

---

### Additional Sections

#### Interface CookiePolicy

```java
public interface
CookiePolicy
```

CookiePolicy implementations decide which cookies should be accepted
and which should be rejected. Three pre-defined policy implementations
are provided, namely ACCEPT_ALL, ACCEPT_NONE and ACCEPT_ORIGINAL_SERVER.

See RFC 2965 sec. 3.3 and 7 for more detail.

**Since:** 1.6

public interface

CookiePolicy

CookiePolicy implementations decide which cookies should be accepted
and which should be rejected. Three pre-defined policy implementations
are provided, namely ACCEPT_ALL, ACCEPT_NONE and ACCEPT_ORIGINAL_SERVER.

See RFC 2965 sec. 3.3 and 7 for more detail.

See RFC 2965 sec. 3.3 and 7 for more detail.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

CookiePolicy

ACCEPT_ALL

One pre-defined policy which accepts all cookies.

static

CookiePolicy

ACCEPT_NONE

One pre-defined policy which accepts no cookies.

static

CookiePolicy

ACCEPT_ORIGINAL_SERVER

One pre-defined policy which only accepts cookies from original server.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

shouldAccept

​(

URI

uri,

HttpCookie

cookie)

Will be called to see whether or not this cookie should be accepted.

Field Summary

Fields

Modifier and Type

Field

Description

static

CookiePolicy

ACCEPT_ALL

One pre-defined policy which accepts all cookies.

static

CookiePolicy

ACCEPT_NONE

One pre-defined policy which accepts no cookies.

static

CookiePolicy

ACCEPT_ORIGINAL_SERVER

One pre-defined policy which only accepts cookies from original server.

---

#### Field Summary

One pre-defined policy which accepts all cookies.

One pre-defined policy which accepts no cookies.

One pre-defined policy which only accepts cookies from original server.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

shouldAccept

​(

URI

uri,

HttpCookie

cookie)

Will be called to see whether or not this cookie should be accepted.

---

#### Method Summary

Will be called to see whether or not this cookie should be accepted.

============ FIELD DETAIL ===========

- Field Detail

- ACCEPT_ALL

```java
static final
CookiePolicy
ACCEPT_ALL
```

One pre-defined policy which accepts all cookies.

- ACCEPT_NONE

```java
static final
CookiePolicy
ACCEPT_NONE
```

One pre-defined policy which accepts no cookies.

- ACCEPT_ORIGINAL_SERVER

```java
static final
CookiePolicy
ACCEPT_ORIGINAL_SERVER
```

One pre-defined policy which only accepts cookies from original server.

============ METHOD DETAIL ==========

- Method Detail

- shouldAccept

```java
boolean shouldAccept​(
URI
uri,

HttpCookie
cookie)
```

Will be called to see whether or not this cookie should be accepted.

**Parameters:** uri

- the URI to consult accept policy with
**Parameters:** cookie

- the HttpCookie object in question
**Returns:** true

if this cookie should be accepted;
otherwise,

false

Field Detail

- ACCEPT_ALL

```java
static final
CookiePolicy
ACCEPT_ALL
```

One pre-defined policy which accepts all cookies.

- ACCEPT_NONE

```java
static final
CookiePolicy
ACCEPT_NONE
```

One pre-defined policy which accepts no cookies.

- ACCEPT_ORIGINAL_SERVER

```java
static final
CookiePolicy
ACCEPT_ORIGINAL_SERVER
```

One pre-defined policy which only accepts cookies from original server.

---

#### Field Detail

ACCEPT_ALL

```java
static final
CookiePolicy
ACCEPT_ALL
```

One pre-defined policy which accepts all cookies.

---

#### ACCEPT_ALL

static final

CookiePolicy

ACCEPT_ALL

One pre-defined policy which accepts all cookies.

ACCEPT_NONE

```java
static final
CookiePolicy
ACCEPT_NONE
```

One pre-defined policy which accepts no cookies.

---

#### ACCEPT_NONE

static final

CookiePolicy

ACCEPT_NONE

One pre-defined policy which accepts no cookies.

ACCEPT_ORIGINAL_SERVER

```java
static final
CookiePolicy
ACCEPT_ORIGINAL_SERVER
```

One pre-defined policy which only accepts cookies from original server.

---

#### ACCEPT_ORIGINAL_SERVER

static final

CookiePolicy

ACCEPT_ORIGINAL_SERVER

One pre-defined policy which only accepts cookies from original server.

Method Detail

- shouldAccept

```java
boolean shouldAccept​(
URI
uri,

HttpCookie
cookie)
```

Will be called to see whether or not this cookie should be accepted.

**Parameters:** uri

- the URI to consult accept policy with
**Parameters:** cookie

- the HttpCookie object in question
**Returns:** true

if this cookie should be accepted;
otherwise,

false

---

#### Method Detail

shouldAccept

```java
boolean shouldAccept​(
URI
uri,

HttpCookie
cookie)
```

Will be called to see whether or not this cookie should be accepted.

**Parameters:** uri

- the URI to consult accept policy with
**Parameters:** cookie

- the HttpCookie object in question
**Returns:** true

if this cookie should be accepted;
otherwise,

false

---

#### shouldAccept

boolean shouldAccept​(

URI

uri,

HttpCookie

cookie)

Will be called to see whether or not this cookie should be accepted.

---

