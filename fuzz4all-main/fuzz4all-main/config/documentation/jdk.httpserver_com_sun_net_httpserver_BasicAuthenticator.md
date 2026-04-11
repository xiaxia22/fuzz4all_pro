# Class BasicAuthenticator

**Source:** `jdk.httpserver\com\sun\net\httpserver\BasicAuthenticator.html`

### Class Description

```java
public abstract class
BasicAuthenticator

extends
Authenticator
```

BasicAuthenticator provides an implementation of HTTP Basic
authentication. It is an abstract class and must be extended
to provide an implementation of

checkCredentials(String,String)

which is called to verify each incoming request.

---

### Field Details

#### protected
String
realm

*No description found.*

---

### Constructor Details

#### public BasicAuthenticator​(
String
realm)

Creates a BasicAuthenticator for the given HTTP realm

**Parameters:**
- realm

- The HTTP Basic authentication realm

**Throws:**
- NullPointerException

- if the realm is an empty string

---

### Method Details

#### public
String
getRealm()

returns the realm this BasicAuthenticator was created with

**Returns:**
- the authenticator's realm string.

---

#### public abstract boolean checkCredentials​(
String
username,

String
password)

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm. Any caching of credentials
must be done by the implementation of this method

**Parameters:**
- username

- the username from the request
- password

- the password from the request

**Returns:**
- true

if the credentials are valid,

false

otherwise.

---

### Additional Sections

#### Class BasicAuthenticator

java.lang.Object

- com.sun.net.httpserver.Authenticator
- - com.sun.net.httpserver.BasicAuthenticator

com.sun.net.httpserver.Authenticator

- com.sun.net.httpserver.BasicAuthenticator

com.sun.net.httpserver.BasicAuthenticator

```java
public abstract class
BasicAuthenticator

extends
Authenticator
```

BasicAuthenticator provides an implementation of HTTP Basic
authentication. It is an abstract class and must be extended
to provide an implementation of

checkCredentials(String,String)

which is called to verify each incoming request.

public abstract class

BasicAuthenticator

extends

Authenticator

BasicAuthenticator provides an implementation of HTTP Basic
authentication. It is an abstract class and must be extended
to provide an implementation of

checkCredentials(String,String)

which is called to verify each incoming request.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class com.sun.net.httpserver.

Authenticator

Authenticator.Failure

,

Authenticator.Result

,

Authenticator.Retry

,

Authenticator.Success

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

realm

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicAuthenticator

​(

String

realm)

Creates a BasicAuthenticator for the given HTTP realm

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

checkCredentials

​(

String

username,

String

password)

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm.

String

getRealm

()

returns the realm this BasicAuthenticator was created with

- Methods declared in class com.sun.net.httpserver.

Authenticator

authenticate

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

Nested Class Summary

- Nested classes/interfaces declared in class com.sun.net.httpserver.

Authenticator

Authenticator.Failure

,

Authenticator.Result

,

Authenticator.Retry

,

Authenticator.Success

---

#### Nested Class Summary

Nested classes/interfaces declared in class com.sun.net.httpserver.

Authenticator

Authenticator.Failure

,

Authenticator.Result

,

Authenticator.Retry

,

Authenticator.Success

---

#### Nested classes/interfaces declared in class com.sun.net.httpserver. Authenticator

Field Summary

Fields

Modifier and Type

Field

Description

protected

String

realm

---

#### Field Summary

Constructor Summary

Constructors

Constructor

Description

BasicAuthenticator

​(

String

realm)

Creates a BasicAuthenticator for the given HTTP realm

---

#### Constructor Summary

Creates a BasicAuthenticator for the given HTTP realm

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

checkCredentials

​(

String

username,

String

password)

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm.

String

getRealm

()

returns the realm this BasicAuthenticator was created with

- Methods declared in class com.sun.net.httpserver.

Authenticator

authenticate

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

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm.

returns the realm this BasicAuthenticator was created with

Methods declared in class com.sun.net.httpserver.

Authenticator

authenticate

---

#### Methods declared in class com.sun.net.httpserver. Authenticator

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

============ FIELD DETAIL ===========

- Field Detail

- realm

```java
protected
String
realm
```

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicAuthenticator

```java
public BasicAuthenticator​(
String
realm)
```

Creates a BasicAuthenticator for the given HTTP realm

**Parameters:** realm

- The HTTP Basic authentication realm
**Throws:** NullPointerException

- if the realm is an empty string

============ METHOD DETAIL ==========

- Method Detail

- getRealm

```java
public
String
getRealm()
```

returns the realm this BasicAuthenticator was created with

**Returns:** the authenticator's realm string.

- checkCredentials

```java
public abstract boolean checkCredentials​(
String
username,

String
password)
```

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm. Any caching of credentials
must be done by the implementation of this method

**Parameters:** username

- the username from the request
**Parameters:** password

- the password from the request
**Returns:** true

if the credentials are valid,

false

otherwise.

Field Detail

- realm

```java
protected
String
realm
```

---

#### Field Detail

realm

```java
protected
String
realm
```

---

#### realm

protected

String

realm

Constructor Detail

- BasicAuthenticator

```java
public BasicAuthenticator​(
String
realm)
```

Creates a BasicAuthenticator for the given HTTP realm

**Parameters:** realm

- The HTTP Basic authentication realm
**Throws:** NullPointerException

- if the realm is an empty string

---

#### Constructor Detail

BasicAuthenticator

```java
public BasicAuthenticator​(
String
realm)
```

Creates a BasicAuthenticator for the given HTTP realm

**Parameters:** realm

- The HTTP Basic authentication realm
**Throws:** NullPointerException

- if the realm is an empty string

---

#### BasicAuthenticator

public BasicAuthenticator​(

String

realm)

Creates a BasicAuthenticator for the given HTTP realm

Method Detail

- getRealm

```java
public
String
getRealm()
```

returns the realm this BasicAuthenticator was created with

**Returns:** the authenticator's realm string.

- checkCredentials

```java
public abstract boolean checkCredentials​(
String
username,

String
password)
```

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm. Any caching of credentials
must be done by the implementation of this method

**Parameters:** username

- the username from the request
**Parameters:** password

- the password from the request
**Returns:** true

if the credentials are valid,

false

otherwise.

---

#### Method Detail

getRealm

```java
public
String
getRealm()
```

returns the realm this BasicAuthenticator was created with

**Returns:** the authenticator's realm string.

---

#### getRealm

public

String

getRealm()

returns the realm this BasicAuthenticator was created with

checkCredentials

```java
public abstract boolean checkCredentials​(
String
username,

String
password)
```

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm. Any caching of credentials
must be done by the implementation of this method

**Parameters:** username

- the username from the request
**Parameters:** password

- the password from the request
**Returns:** true

if the credentials are valid,

false

otherwise.

---

#### checkCredentials

public abstract boolean checkCredentials​(

String

username,

String

password)

called for each incoming request to verify the
given name and password in the context of this
Authenticator's realm. Any caching of credentials
must be done by the implementation of this method

---

