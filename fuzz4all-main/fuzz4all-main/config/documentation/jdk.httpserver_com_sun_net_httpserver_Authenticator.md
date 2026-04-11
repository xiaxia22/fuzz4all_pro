# Class Authenticator

**Source:** `jdk.httpserver\com\sun\net\httpserver\Authenticator.html`

### Class Description

```java
public abstract class
Authenticator

extends
Object
```

Authenticator represents an implementation of an HTTP authentication
mechanism. Sub-classes provide implementations of specific mechanisms
such as Digest or Basic auth. Instances are invoked to provide verification
of the authentication information provided in all incoming requests.
Note. This implies that any caching of credentials or other authentication
information must be done outside of this class.

**Direct Known Subclasses:** BasicAuthenticator

---

### Field Details

*No entries found.*

### Constructor Details

#### public Authenticator()

*No description found.*

---

### Method Details

#### public abstract
Authenticator.Result
authenticate​(
HttpExchange
exch)

called to authenticate each incoming request. The implementation
must return a Failure, Success or Retry object as appropriate :-

Failure means the authentication has completed, but has failed
due to invalid credentials.

Sucess means that the authentication
has succeeded, and a Principal object representing the user
can be retrieved by calling Sucess.getPrincipal() .

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

---

### Additional Sections

#### Class Authenticator

java.lang.Object

- com.sun.net.httpserver.Authenticator

com.sun.net.httpserver.Authenticator

**Direct Known Subclasses:** BasicAuthenticator

```java
public abstract class
Authenticator

extends
Object
```

Authenticator represents an implementation of an HTTP authentication
mechanism. Sub-classes provide implementations of specific mechanisms
such as Digest or Basic auth. Instances are invoked to provide verification
of the authentication information provided in all incoming requests.
Note. This implies that any caching of credentials or other authentication
information must be done outside of this class.

public abstract class

Authenticator

extends

Object

Authenticator represents an implementation of an HTTP authentication
mechanism. Sub-classes provide implementations of specific mechanisms
such as Digest or Basic auth. Instances are invoked to provide verification
of the authentication information provided in all incoming requests.
Note. This implies that any caching of credentials or other authentication
information must be done outside of this class.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Authenticator.Failure

Indicates an authentication failure.

static class

Authenticator.Result

Base class for return type from authenticate() method

static class

Authenticator.Retry

Indicates an authentication must be retried.

static class

Authenticator.Success

Indicates an authentication has succeeded and the
authenticated user principal can be acquired by calling
getPrincipal().

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Authenticator

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Authenticator.Result

authenticate

​(

HttpExchange

exch)

called to authenticate each incoming request.

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

Nested Classes

Modifier and Type

Class

Description

static class

Authenticator.Failure

Indicates an authentication failure.

static class

Authenticator.Result

Base class for return type from authenticate() method

static class

Authenticator.Retry

Indicates an authentication must be retried.

static class

Authenticator.Success

Indicates an authentication has succeeded and the
authenticated user principal can be acquired by calling
getPrincipal().

---

#### Nested Class Summary

Indicates an authentication failure.

Base class for return type from authenticate() method

Indicates an authentication must be retried.

Indicates an authentication has succeeded and the
authenticated user principal can be acquired by calling
getPrincipal().

Constructor Summary

Constructors

Constructor

Description

Authenticator

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Authenticator.Result

authenticate

​(

HttpExchange

exch)

called to authenticate each incoming request.

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

called to authenticate each incoming request.

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

- Authenticator

```java
public Authenticator()
```

============ METHOD DETAIL ==========

- Method Detail

- authenticate

```java
public abstract
Authenticator.Result
authenticate​(
HttpExchange
exch)
```

called to authenticate each incoming request. The implementation
must return a Failure, Success or Retry object as appropriate :-

Failure means the authentication has completed, but has failed
due to invalid credentials.

Sucess means that the authentication
has succeeded, and a Principal object representing the user
can be retrieved by calling Sucess.getPrincipal() .

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

Constructor Detail

- Authenticator

```java
public Authenticator()
```

---

#### Constructor Detail

Authenticator

```java
public Authenticator()
```

---

#### Authenticator

public Authenticator()

Method Detail

- authenticate

```java
public abstract
Authenticator.Result
authenticate​(
HttpExchange
exch)
```

called to authenticate each incoming request. The implementation
must return a Failure, Success or Retry object as appropriate :-

Failure means the authentication has completed, but has failed
due to invalid credentials.

Sucess means that the authentication
has succeeded, and a Principal object representing the user
can be retrieved by calling Sucess.getPrincipal() .

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

---

#### Method Detail

authenticate

```java
public abstract
Authenticator.Result
authenticate​(
HttpExchange
exch)
```

called to authenticate each incoming request. The implementation
must return a Failure, Success or Retry object as appropriate :-

Failure means the authentication has completed, but has failed
due to invalid credentials.

Sucess means that the authentication
has succeeded, and a Principal object representing the user
can be retrieved by calling Sucess.getPrincipal() .

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

---

#### authenticate

public abstract

Authenticator.Result

authenticate​(

HttpExchange

exch)

called to authenticate each incoming request. The implementation
must return a Failure, Success or Retry object as appropriate :-

Failure means the authentication has completed, but has failed
due to invalid credentials.

Sucess means that the authentication
has succeeded, and a Principal object representing the user
can be retrieved by calling Sucess.getPrincipal() .

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

Failure means the authentication has completed, but has failed
due to invalid credentials.

Sucess means that the authentication
has succeeded, and a Principal object representing the user
can be retrieved by calling Sucess.getPrincipal() .

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

Sucess means that the authentication
has succeeded, and a Principal object representing the user
can be retrieved by calling Sucess.getPrincipal() .

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

Retry means that another HTTP exchange is required. Any response
headers needing to be sent back to the client are set in the
given HttpExchange. The response code to be returned must be provided
in the Retry object. Retry may occur multiple times.

---

