# Class AuthorizeCallback

**Source:** `java.security.sasl\javax\security\sasl\AuthorizeCallback.html`

### Class Description

```java
public class
AuthorizeCallback

extends
Object

implements
Callback
,
Serializable
```

This callback is used by

SaslServer

to determine whether
one entity (identified by an authenticated authentication id)
can act on
behalf of another entity (identified by an authorization id).

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public AuthorizeCallback​(
String
authnID,

String
authzID)

Constructs an instance of

AuthorizeCallback

.

**Parameters:**
- authnID

- The (authenticated) authentication id.
- authzID

- The authorization id.

---

### Method Details

#### public
String
getAuthenticationID()

Returns the authentication id to check.

**Returns:**
- The authentication id to check.

---

#### public
String
getAuthorizationID()

Returns the authorization id to check.

**Returns:**
- The authentication id to check.

---

#### public boolean isAuthorized()

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

**Returns:**
- true

if authorization is allowed;

false

otherwise

**See Also:**
- setAuthorized(boolean)

,

getAuthorizedID()

---

#### public void setAuthorized​(boolean ok)

Sets whether the authorization is allowed.

**Parameters:**
- ok

-

true

if authorization is allowed;

false

otherwise

**See Also:**
- isAuthorized()

,

setAuthorizedID(java.lang.String)

---

#### public
String
getAuthorizedID()

Returns the id of the authorized user.

**Returns:**
- The id of the authorized user.

null

means the
authorization failed.

**See Also:**
- setAuthorized(boolean)

,

setAuthorizedID(java.lang.String)

---

#### public void setAuthorizedID​(
String
id)

Sets the id of the authorized entity. Called by handler only when the id
is different from getAuthorizationID(). For example, the id
might need to be canonicalized for the environment in which it
will be used.

**Parameters:**
- id

- The id of the authorized user.

**See Also:**
- setAuthorized(boolean)

,

getAuthorizedID()

---

### Additional Sections

#### Class AuthorizeCallback

java.lang.Object

- javax.security.sasl.AuthorizeCallback

javax.security.sasl.AuthorizeCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
AuthorizeCallback

extends
Object

implements
Callback
,
Serializable
```

This callback is used by

SaslServer

to determine whether
one entity (identified by an authenticated authentication id)
can act on
behalf of another entity (identified by an authorization id).

**Since:** 1.5
**See Also:** Serialized Form

public class

AuthorizeCallback

extends

Object

implements

Callback

,

Serializable

This callback is used by

SaslServer

to determine whether
one entity (identified by an authenticated authentication id)
can act on
behalf of another entity (identified by an authorization id).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AuthorizeCallback

​(

String

authnID,

String

authzID)

Constructs an instance of

AuthorizeCallback

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAuthenticationID

()

Returns the authentication id to check.

String

getAuthorizationID

()

Returns the authorization id to check.

String

getAuthorizedID

()

Returns the id of the authorized user.

boolean

isAuthorized

()

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

void

setAuthorized

​(boolean ok)

Sets whether the authorization is allowed.

void

setAuthorizedID

​(

String

id)

Sets the id of the authorized entity.

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

AuthorizeCallback

​(

String

authnID,

String

authzID)

Constructs an instance of

AuthorizeCallback

.

---

#### Constructor Summary

Constructs an instance of

AuthorizeCallback

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAuthenticationID

()

Returns the authentication id to check.

String

getAuthorizationID

()

Returns the authorization id to check.

String

getAuthorizedID

()

Returns the id of the authorized user.

boolean

isAuthorized

()

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

void

setAuthorized

​(boolean ok)

Sets whether the authorization is allowed.

void

setAuthorizedID

​(

String

id)

Sets the id of the authorized entity.

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

Returns the authentication id to check.

Returns the authorization id to check.

Returns the id of the authorized user.

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

Sets whether the authorization is allowed.

Sets the id of the authorized entity.

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

- AuthorizeCallback

```java
public AuthorizeCallback​(
String
authnID,

String
authzID)
```

Constructs an instance of

AuthorizeCallback

.

**Parameters:** authnID

- The (authenticated) authentication id.
**Parameters:** authzID

- The authorization id.

============ METHOD DETAIL ==========

- Method Detail

- getAuthenticationID

```java
public
String
getAuthenticationID()
```

Returns the authentication id to check.

**Returns:** The authentication id to check.

- getAuthorizationID

```java
public
String
getAuthorizationID()
```

Returns the authorization id to check.

**Returns:** The authentication id to check.

- isAuthorized

```java
public boolean isAuthorized()
```

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

**Returns:** true

if authorization is allowed;

false

otherwise
**See Also:** setAuthorized(boolean)

,

getAuthorizedID()

- setAuthorized

```java
public void setAuthorized​(boolean ok)
```

Sets whether the authorization is allowed.

**Parameters:** ok

-

true

if authorization is allowed;

false

otherwise
**See Also:** isAuthorized()

,

setAuthorizedID(java.lang.String)

- getAuthorizedID

```java
public
String
getAuthorizedID()
```

Returns the id of the authorized user.

**Returns:** The id of the authorized user.

null

means the
authorization failed.
**See Also:** setAuthorized(boolean)

,

setAuthorizedID(java.lang.String)

- setAuthorizedID

```java
public void setAuthorizedID​(
String
id)
```

Sets the id of the authorized entity. Called by handler only when the id
is different from getAuthorizationID(). For example, the id
might need to be canonicalized for the environment in which it
will be used.

**Parameters:** id

- The id of the authorized user.
**See Also:** setAuthorized(boolean)

,

getAuthorizedID()

Constructor Detail

- AuthorizeCallback

```java
public AuthorizeCallback​(
String
authnID,

String
authzID)
```

Constructs an instance of

AuthorizeCallback

.

**Parameters:** authnID

- The (authenticated) authentication id.
**Parameters:** authzID

- The authorization id.

---

#### Constructor Detail

AuthorizeCallback

```java
public AuthorizeCallback​(
String
authnID,

String
authzID)
```

Constructs an instance of

AuthorizeCallback

.

**Parameters:** authnID

- The (authenticated) authentication id.
**Parameters:** authzID

- The authorization id.

---

#### AuthorizeCallback

public AuthorizeCallback​(

String

authnID,

String

authzID)

Constructs an instance of

AuthorizeCallback

.

Method Detail

- getAuthenticationID

```java
public
String
getAuthenticationID()
```

Returns the authentication id to check.

**Returns:** The authentication id to check.

- getAuthorizationID

```java
public
String
getAuthorizationID()
```

Returns the authorization id to check.

**Returns:** The authentication id to check.

- isAuthorized

```java
public boolean isAuthorized()
```

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

**Returns:** true

if authorization is allowed;

false

otherwise
**See Also:** setAuthorized(boolean)

,

getAuthorizedID()

- setAuthorized

```java
public void setAuthorized​(boolean ok)
```

Sets whether the authorization is allowed.

**Parameters:** ok

-

true

if authorization is allowed;

false

otherwise
**See Also:** isAuthorized()

,

setAuthorizedID(java.lang.String)

- getAuthorizedID

```java
public
String
getAuthorizedID()
```

Returns the id of the authorized user.

**Returns:** The id of the authorized user.

null

means the
authorization failed.
**See Also:** setAuthorized(boolean)

,

setAuthorizedID(java.lang.String)

- setAuthorizedID

```java
public void setAuthorizedID​(
String
id)
```

Sets the id of the authorized entity. Called by handler only when the id
is different from getAuthorizationID(). For example, the id
might need to be canonicalized for the environment in which it
will be used.

**Parameters:** id

- The id of the authorized user.
**See Also:** setAuthorized(boolean)

,

getAuthorizedID()

---

#### Method Detail

getAuthenticationID

```java
public
String
getAuthenticationID()
```

Returns the authentication id to check.

**Returns:** The authentication id to check.

---

#### getAuthenticationID

public

String

getAuthenticationID()

Returns the authentication id to check.

getAuthorizationID

```java
public
String
getAuthorizationID()
```

Returns the authorization id to check.

**Returns:** The authentication id to check.

---

#### getAuthorizationID

public

String

getAuthorizationID()

Returns the authorization id to check.

isAuthorized

```java
public boolean isAuthorized()
```

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

**Returns:** true

if authorization is allowed;

false

otherwise
**See Also:** setAuthorized(boolean)

,

getAuthorizedID()

---

#### isAuthorized

public boolean isAuthorized()

Determines whether the authentication id is allowed to
act on behalf of the authorization id.

setAuthorized

```java
public void setAuthorized​(boolean ok)
```

Sets whether the authorization is allowed.

**Parameters:** ok

-

true

if authorization is allowed;

false

otherwise
**See Also:** isAuthorized()

,

setAuthorizedID(java.lang.String)

---

#### setAuthorized

public void setAuthorized​(boolean ok)

Sets whether the authorization is allowed.

getAuthorizedID

```java
public
String
getAuthorizedID()
```

Returns the id of the authorized user.

**Returns:** The id of the authorized user.

null

means the
authorization failed.
**See Also:** setAuthorized(boolean)

,

setAuthorizedID(java.lang.String)

---

#### getAuthorizedID

public

String

getAuthorizedID()

Returns the id of the authorized user.

setAuthorizedID

```java
public void setAuthorizedID​(
String
id)
```

Sets the id of the authorized entity. Called by handler only when the id
is different from getAuthorizationID(). For example, the id
might need to be canonicalized for the environment in which it
will be used.

**Parameters:** id

- The id of the authorized user.
**See Also:** setAuthorized(boolean)

,

getAuthorizedID()

---

#### setAuthorizedID

public void setAuthorizedID​(

String

id)

Sets the id of the authorized entity. Called by handler only when the id
is different from getAuthorizationID(). For example, the id
might need to be canonicalized for the environment in which it
will be used.

---

