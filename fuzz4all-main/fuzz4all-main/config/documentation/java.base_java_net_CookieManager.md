# Class CookieManager

**Source:** `java.base\java\net\CookieManager.html`

### Class Description

```java
public class
CookieManager

extends
CookieHandler
```

CookieManager provides a concrete implementation of

CookieHandler

,
which separates the storage of cookies from the policy surrounding accepting
and rejecting cookies. A CookieManager is initialized with a

CookieStore

which manages storage, and a

CookiePolicy

object, which makes
policy decisions on cookie acceptance/rejection.

The HTTP cookie management in java.net package looks like:

```java
use
CookieHandler <------- HttpURLConnection
^
| impl
| use
CookieManager -------> CookiePolicy
| use
|--------> HttpCookie
| ^
| | use
| use |
|--------> CookieStore
^
| impl
|
Internal in-memory implementation
```

- CookieHandler is at the core of cookie management. User can call
CookieHandler.setDefault to set a concrete CookieHanlder implementation
to be used.
- CookiePolicy.shouldAccept will be called by CookieManager.put to see whether
or not one cookie should be accepted and put into cookie store. User can use
any of three pre-defined CookiePolicy, namely ACCEPT_ALL, ACCEPT_NONE and
ACCEPT_ORIGINAL_SERVER, or user can define his own CookiePolicy implementation
and tell CookieManager to use it.
- CookieStore is the place where any accepted HTTP cookie is stored in.
If not specified when created, a CookieManager instance will use an internal
in-memory implementation. Or user can implements one and tell CookieManager
to use it.
- Currently, only CookieStore.add(URI, HttpCookie) and CookieStore.get(URI)
are used by CookieManager. Others are for completeness and might be needed
by a more sophisticated CookieStore implementation, e.g. a NetscapeCookieStore.

There're various ways user can hook up his own HTTP cookie management behavior, e.g.

- Use CookieHandler.setDefault to set a brand new

CookieHandler

implementation

Let CookieManager be the default

CookieHandler

implementation,
but implement user's own

CookieStore

and

CookiePolicy

and tell default CookieManager to use them:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager(new MyCookieStore(), new MyCookiePolicy()));
```

Let CookieManager be the default

CookieHandler

implementation, but
use customized

CookiePolicy

:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager());
// this can be done at any point of an HTTP session
((CookieManager)CookieHandler.getDefault()).setCookiePolicy(new MyCookiePolicy());
```

The implementation conforms to

RFC 2965

, section 3.3.

**Since:** 1.6
**See Also:** CookiePolicy

---

### Field Details

*No entries found.*

### Constructor Details

#### public CookieManager()

Create a new cookie manager.

This constructor will create new cookie manager with default
cookie store and accept policy. The effect is same as

CookieManager(null, null)

.

---

#### public CookieManager​(
CookieStore
store,

CookiePolicy
cookiePolicy)

Create a new cookie manager with specified cookie store and cookie policy.

**Parameters:**
- store

- a

CookieStore

to be used by cookie manager.
if

null

, cookie manager will use a default one,
which is an in-memory CookieStore implementation.
- cookiePolicy

- a

CookiePolicy

instance
to be used by cookie manager as policy callback.
if

null

, ACCEPT_ORIGINAL_SERVER will
be used.

---

### Method Details

#### public void setCookiePolicy​(
CookiePolicy
cookiePolicy)

To set the cookie policy of this cookie manager.

A instance of

CookieManager

will have
cookie policy ACCEPT_ORIGINAL_SERVER by default. Users always
can call this method to set another cookie policy.

**Parameters:**
- cookiePolicy

- the cookie policy. Can be

null

, which
has no effects on current cookie policy.

---

#### public
CookieStore
getCookieStore()

To retrieve current cookie store.

**Returns:**
- the cookie store currently used by cookie manager.

---

### Additional Sections

#### Class CookieManager

java.lang.Object

- java.net.CookieHandler
- - java.net.CookieManager

java.net.CookieHandler

- java.net.CookieManager

java.net.CookieManager

```java
public class
CookieManager

extends
CookieHandler
```

CookieManager provides a concrete implementation of

CookieHandler

,
which separates the storage of cookies from the policy surrounding accepting
and rejecting cookies. A CookieManager is initialized with a

CookieStore

which manages storage, and a

CookiePolicy

object, which makes
policy decisions on cookie acceptance/rejection.

The HTTP cookie management in java.net package looks like:

```java
use
CookieHandler <------- HttpURLConnection
^
| impl
| use
CookieManager -------> CookiePolicy
| use
|--------> HttpCookie
| ^
| | use
| use |
|--------> CookieStore
^
| impl
|
Internal in-memory implementation
```

- CookieHandler is at the core of cookie management. User can call
CookieHandler.setDefault to set a concrete CookieHanlder implementation
to be used.
- CookiePolicy.shouldAccept will be called by CookieManager.put to see whether
or not one cookie should be accepted and put into cookie store. User can use
any of three pre-defined CookiePolicy, namely ACCEPT_ALL, ACCEPT_NONE and
ACCEPT_ORIGINAL_SERVER, or user can define his own CookiePolicy implementation
and tell CookieManager to use it.
- CookieStore is the place where any accepted HTTP cookie is stored in.
If not specified when created, a CookieManager instance will use an internal
in-memory implementation. Or user can implements one and tell CookieManager
to use it.
- Currently, only CookieStore.add(URI, HttpCookie) and CookieStore.get(URI)
are used by CookieManager. Others are for completeness and might be needed
by a more sophisticated CookieStore implementation, e.g. a NetscapeCookieStore.

There're various ways user can hook up his own HTTP cookie management behavior, e.g.

- Use CookieHandler.setDefault to set a brand new

CookieHandler

implementation

Let CookieManager be the default

CookieHandler

implementation,
but implement user's own

CookieStore

and

CookiePolicy

and tell default CookieManager to use them:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager(new MyCookieStore(), new MyCookiePolicy()));
```

Let CookieManager be the default

CookieHandler

implementation, but
use customized

CookiePolicy

:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager());
// this can be done at any point of an HTTP session
((CookieManager)CookieHandler.getDefault()).setCookiePolicy(new MyCookiePolicy());
```

The implementation conforms to

RFC 2965

, section 3.3.

**Since:** 1.6
**See Also:** CookiePolicy

public class

CookieManager

extends

CookieHandler

CookieManager provides a concrete implementation of

CookieHandler

,
which separates the storage of cookies from the policy surrounding accepting
and rejecting cookies. A CookieManager is initialized with a

CookieStore

which manages storage, and a

CookiePolicy

object, which makes
policy decisions on cookie acceptance/rejection.

The HTTP cookie management in java.net package looks like:

```java
use
CookieHandler <------- HttpURLConnection
^
| impl
| use
CookieManager -------> CookiePolicy
| use
|--------> HttpCookie
| ^
| | use
| use |
|--------> CookieStore
^
| impl
|
Internal in-memory implementation
```

- CookieHandler is at the core of cookie management. User can call
CookieHandler.setDefault to set a concrete CookieHanlder implementation
to be used.
- CookiePolicy.shouldAccept will be called by CookieManager.put to see whether
or not one cookie should be accepted and put into cookie store. User can use
any of three pre-defined CookiePolicy, namely ACCEPT_ALL, ACCEPT_NONE and
ACCEPT_ORIGINAL_SERVER, or user can define his own CookiePolicy implementation
and tell CookieManager to use it.
- CookieStore is the place where any accepted HTTP cookie is stored in.
If not specified when created, a CookieManager instance will use an internal
in-memory implementation. Or user can implements one and tell CookieManager
to use it.
- Currently, only CookieStore.add(URI, HttpCookie) and CookieStore.get(URI)
are used by CookieManager. Others are for completeness and might be needed
by a more sophisticated CookieStore implementation, e.g. a NetscapeCookieStore.

There're various ways user can hook up his own HTTP cookie management behavior, e.g.

- Use CookieHandler.setDefault to set a brand new

CookieHandler

implementation

Let CookieManager be the default

CookieHandler

implementation,
but implement user's own

CookieStore

and

CookiePolicy

and tell default CookieManager to use them:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager(new MyCookieStore(), new MyCookiePolicy()));
```

Let CookieManager be the default

CookieHandler

implementation, but
use customized

CookiePolicy

:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager());
// this can be done at any point of an HTTP session
((CookieManager)CookieHandler.getDefault()).setCookiePolicy(new MyCookiePolicy());
```

The implementation conforms to

RFC 2965

, section 3.3.

The HTTP cookie management in java.net package looks like:

```java
use
CookieHandler <------- HttpURLConnection
^
| impl
| use
CookieManager -------> CookiePolicy
| use
|--------> HttpCookie
| ^
| | use
| use |
|--------> CookieStore
^
| impl
|
Internal in-memory implementation
```

- CookieHandler is at the core of cookie management. User can call
CookieHandler.setDefault to set a concrete CookieHanlder implementation
to be used.
- CookiePolicy.shouldAccept will be called by CookieManager.put to see whether
or not one cookie should be accepted and put into cookie store. User can use
any of three pre-defined CookiePolicy, namely ACCEPT_ALL, ACCEPT_NONE and
ACCEPT_ORIGINAL_SERVER, or user can define his own CookiePolicy implementation
and tell CookieManager to use it.
- CookieStore is the place where any accepted HTTP cookie is stored in.
If not specified when created, a CookieManager instance will use an internal
in-memory implementation. Or user can implements one and tell CookieManager
to use it.
- Currently, only CookieStore.add(URI, HttpCookie) and CookieStore.get(URI)
are used by CookieManager. Others are for completeness and might be needed
by a more sophisticated CookieStore implementation, e.g. a NetscapeCookieStore.

There're various ways user can hook up his own HTTP cookie management behavior, e.g.

- Use CookieHandler.setDefault to set a brand new

CookieHandler

implementation

Let CookieManager be the default

CookieHandler

implementation,
but implement user's own

CookieStore

and

CookiePolicy

and tell default CookieManager to use them:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager(new MyCookieStore(), new MyCookiePolicy()));
```

Let CookieManager be the default

CookieHandler

implementation, but
use customized

CookiePolicy

:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager());
// this can be done at any point of an HTTP session
((CookieManager)CookieHandler.getDefault()).setCookiePolicy(new MyCookiePolicy());
```

The implementation conforms to

RFC 2965

, section 3.3.

use
CookieHandler <------- HttpURLConnection
^
| impl
| use
CookieManager -------> CookiePolicy
| use
|--------> HttpCookie
| ^
| | use
| use |
|--------> CookieStore
^
| impl
|
Internal in-memory implementation

CookieHandler is at the core of cookie management. User can call
CookieHandler.setDefault to set a concrete CookieHanlder implementation
to be used.

CookiePolicy.shouldAccept will be called by CookieManager.put to see whether
or not one cookie should be accepted and put into cookie store. User can use
any of three pre-defined CookiePolicy, namely ACCEPT_ALL, ACCEPT_NONE and
ACCEPT_ORIGINAL_SERVER, or user can define his own CookiePolicy implementation
and tell CookieManager to use it.

CookieStore is the place where any accepted HTTP cookie is stored in.
If not specified when created, a CookieManager instance will use an internal
in-memory implementation. Or user can implements one and tell CookieManager
to use it.

Currently, only CookieStore.add(URI, HttpCookie) and CookieStore.get(URI)
are used by CookieManager. Others are for completeness and might be needed
by a more sophisticated CookieStore implementation, e.g. a NetscapeCookieStore.

There're various ways user can hook up his own HTTP cookie management behavior, e.g.

- Use CookieHandler.setDefault to set a brand new

CookieHandler

implementation

Let CookieManager be the default

CookieHandler

implementation,
but implement user's own

CookieStore

and

CookiePolicy

and tell default CookieManager to use them:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager(new MyCookieStore(), new MyCookiePolicy()));
```

Let CookieManager be the default

CookieHandler

implementation, but
use customized

CookiePolicy

:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager());
// this can be done at any point of an HTTP session
((CookieManager)CookieHandler.getDefault()).setCookiePolicy(new MyCookiePolicy());
```

The implementation conforms to

RFC 2965

, section 3.3.

Use CookieHandler.setDefault to set a brand new

CookieHandler

implementation

Let CookieManager be the default

CookieHandler

implementation,
but implement user's own

CookieStore

and

CookiePolicy

and tell default CookieManager to use them:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager(new MyCookieStore(), new MyCookiePolicy()));
```

Let CookieManager be the default

CookieHandler

implementation, but
use customized

CookiePolicy

:

```java
// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager());
// this can be done at any point of an HTTP session
((CookieManager)CookieHandler.getDefault()).setCookiePolicy(new MyCookiePolicy());
```

// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager(new MyCookieStore(), new MyCookiePolicy()));

// this should be done at the beginning of an HTTP session
CookieHandler.setDefault(new CookieManager());
// this can be done at any point of an HTTP session
((CookieManager)CookieHandler.getDefault()).setCookiePolicy(new MyCookiePolicy());

The implementation conforms to

RFC 2965

, section 3.3.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CookieManager

()

Create a new cookie manager.

CookieManager

​(

CookieStore

store,

CookiePolicy

cookiePolicy)

Create a new cookie manager with specified cookie store and cookie policy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CookieStore

getCookieStore

()

To retrieve current cookie store.

void

setCookiePolicy

​(

CookiePolicy

cookiePolicy)

To set the cookie policy of this cookie manager.

- Methods declared in class java.net.

CookieHandler

get

,

getDefault

,

put

,

setDefault

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

CookieManager

()

Create a new cookie manager.

CookieManager

​(

CookieStore

store,

CookiePolicy

cookiePolicy)

Create a new cookie manager with specified cookie store and cookie policy.

---

#### Constructor Summary

Create a new cookie manager.

Create a new cookie manager with specified cookie store and cookie policy.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CookieStore

getCookieStore

()

To retrieve current cookie store.

void

setCookiePolicy

​(

CookiePolicy

cookiePolicy)

To set the cookie policy of this cookie manager.

- Methods declared in class java.net.

CookieHandler

get

,

getDefault

,

put

,

setDefault

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

To retrieve current cookie store.

To set the cookie policy of this cookie manager.

Methods declared in class java.net.

CookieHandler

get

,

getDefault

,

put

,

setDefault

---

#### Methods declared in class java.net. CookieHandler

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CookieManager

```java
public CookieManager()
```

Create a new cookie manager.

This constructor will create new cookie manager with default
cookie store and accept policy. The effect is same as

CookieManager(null, null)

.

- CookieManager

```java
public CookieManager​(
CookieStore
store,

CookiePolicy
cookiePolicy)
```

Create a new cookie manager with specified cookie store and cookie policy.

**Parameters:** store

- a

CookieStore

to be used by cookie manager.
if

null

, cookie manager will use a default one,
which is an in-memory CookieStore implementation.
**Parameters:** cookiePolicy

- a

CookiePolicy

instance
to be used by cookie manager as policy callback.
if

null

, ACCEPT_ORIGINAL_SERVER will
be used.

============ METHOD DETAIL ==========

- Method Detail

- setCookiePolicy

```java
public void setCookiePolicy​(
CookiePolicy
cookiePolicy)
```

To set the cookie policy of this cookie manager.

A instance of

CookieManager

will have
cookie policy ACCEPT_ORIGINAL_SERVER by default. Users always
can call this method to set another cookie policy.

**Parameters:** cookiePolicy

- the cookie policy. Can be

null

, which
has no effects on current cookie policy.

- getCookieStore

```java
public
CookieStore
getCookieStore()
```

To retrieve current cookie store.

**Returns:** the cookie store currently used by cookie manager.

Constructor Detail

- CookieManager

```java
public CookieManager()
```

Create a new cookie manager.

This constructor will create new cookie manager with default
cookie store and accept policy. The effect is same as

CookieManager(null, null)

.

- CookieManager

```java
public CookieManager​(
CookieStore
store,

CookiePolicy
cookiePolicy)
```

Create a new cookie manager with specified cookie store and cookie policy.

**Parameters:** store

- a

CookieStore

to be used by cookie manager.
if

null

, cookie manager will use a default one,
which is an in-memory CookieStore implementation.
**Parameters:** cookiePolicy

- a

CookiePolicy

instance
to be used by cookie manager as policy callback.
if

null

, ACCEPT_ORIGINAL_SERVER will
be used.

---

#### Constructor Detail

CookieManager

```java
public CookieManager()
```

Create a new cookie manager.

This constructor will create new cookie manager with default
cookie store and accept policy. The effect is same as

CookieManager(null, null)

.

---

#### CookieManager

public CookieManager()

Create a new cookie manager.

This constructor will create new cookie manager with default
cookie store and accept policy. The effect is same as

CookieManager(null, null)

.

This constructor will create new cookie manager with default
cookie store and accept policy. The effect is same as

CookieManager(null, null)

.

CookieManager

```java
public CookieManager​(
CookieStore
store,

CookiePolicy
cookiePolicy)
```

Create a new cookie manager with specified cookie store and cookie policy.

**Parameters:** store

- a

CookieStore

to be used by cookie manager.
if

null

, cookie manager will use a default one,
which is an in-memory CookieStore implementation.
**Parameters:** cookiePolicy

- a

CookiePolicy

instance
to be used by cookie manager as policy callback.
if

null

, ACCEPT_ORIGINAL_SERVER will
be used.

---

#### CookieManager

public CookieManager​(

CookieStore

store,

CookiePolicy

cookiePolicy)

Create a new cookie manager with specified cookie store and cookie policy.

Method Detail

- setCookiePolicy

```java
public void setCookiePolicy​(
CookiePolicy
cookiePolicy)
```

To set the cookie policy of this cookie manager.

A instance of

CookieManager

will have
cookie policy ACCEPT_ORIGINAL_SERVER by default. Users always
can call this method to set another cookie policy.

**Parameters:** cookiePolicy

- the cookie policy. Can be

null

, which
has no effects on current cookie policy.

- getCookieStore

```java
public
CookieStore
getCookieStore()
```

To retrieve current cookie store.

**Returns:** the cookie store currently used by cookie manager.

---

#### Method Detail

setCookiePolicy

```java
public void setCookiePolicy​(
CookiePolicy
cookiePolicy)
```

To set the cookie policy of this cookie manager.

A instance of

CookieManager

will have
cookie policy ACCEPT_ORIGINAL_SERVER by default. Users always
can call this method to set another cookie policy.

**Parameters:** cookiePolicy

- the cookie policy. Can be

null

, which
has no effects on current cookie policy.

---

#### setCookiePolicy

public void setCookiePolicy​(

CookiePolicy

cookiePolicy)

To set the cookie policy of this cookie manager.

A instance of

CookieManager

will have
cookie policy ACCEPT_ORIGINAL_SERVER by default. Users always
can call this method to set another cookie policy.

A instance of

CookieManager

will have
cookie policy ACCEPT_ORIGINAL_SERVER by default. Users always
can call this method to set another cookie policy.

getCookieStore

```java
public
CookieStore
getCookieStore()
```

To retrieve current cookie store.

**Returns:** the cookie store currently used by cookie manager.

---

#### getCookieStore

public

CookieStore

getCookieStore()

To retrieve current cookie store.

---

