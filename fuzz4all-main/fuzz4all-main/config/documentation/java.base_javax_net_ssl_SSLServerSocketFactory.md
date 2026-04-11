# Class SSLServerSocketFactory

**Source:** `java.base\javax\net\ssl\SSLServerSocketFactory.html`

### Class Description

```java
public abstract class
SSLServerSocketFactory

extends
ServerSocketFactory
```

SSLServerSocketFactory

s create

SSLServerSocket

s.

**Since:** 1.4
**See Also:** SSLSocket

,

SSLServerSocket

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SSLServerSocketFactory()

Constructor is used only by subclasses.

---

### Method Details

#### public static
ServerSocketFactory
getDefault()

Returns the default SSL server socket factory.

The first time this method is called, the security property
"ssl.ServerSocketFactory.provider" is examined. If it is non-null, a
class by that name is loaded and instantiated. If that is successful and
the object is an instance of SSLServerSocketFactory, it is made the
default SSL server socket factory.

Otherwise, this method returns

SSLContext.getDefault().getServerSocketFactory()

. If that
call fails, an inoperative factory is returned.

**Returns:**
- the default

ServerSocketFactory

**See Also:**
- SSLContext.getDefault()

---

#### public abstract
String
[] getDefaultCipherSuites()

Returns the list of cipher suites which are enabled by default.
Unless a different list is enabled, handshaking on an SSL connection
will use one of these cipher suites. The minimum quality of service
for these defaults requires confidentiality protection and server
authentication (that is, no anonymous cipher suites).

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:**
- array of the cipher suites enabled by default

**See Also:**
- getSupportedCipherSuites()

---

#### public abstract
String
[] getSupportedCipherSuites()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.
Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:**
- an array of cipher suite names

**See Also:**
- getDefaultCipherSuites()

---

### Additional Sections

#### Class SSLServerSocketFactory

java.lang.Object

- javax.net.ServerSocketFactory
- - javax.net.ssl.SSLServerSocketFactory

javax.net.ServerSocketFactory

- javax.net.ssl.SSLServerSocketFactory

javax.net.ssl.SSLServerSocketFactory

```java
public abstract class
SSLServerSocketFactory

extends
ServerSocketFactory
```

SSLServerSocketFactory

s create

SSLServerSocket

s.

**Since:** 1.4
**See Also:** SSLSocket

,

SSLServerSocket

public abstract class

SSLServerSocketFactory

extends

ServerSocketFactory

SSLServerSocketFactory

s create

SSLServerSocket

s.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SSLServerSocketFactory

()

Constructor is used only by subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

ServerSocketFactory

getDefault

()

Returns the default SSL server socket factory.

abstract

String

[]

getDefaultCipherSuites

()

Returns the list of cipher suites which are enabled by default.

abstract

String

[]

getSupportedCipherSuites

()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.

- Methods declared in class javax.net.

ServerSocketFactory

createServerSocket

,

createServerSocket

,

createServerSocket

,

createServerSocket

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

Modifier

Constructor

Description

protected

SSLServerSocketFactory

()

Constructor is used only by subclasses.

---

#### Constructor Summary

Constructor is used only by subclasses.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

ServerSocketFactory

getDefault

()

Returns the default SSL server socket factory.

abstract

String

[]

getDefaultCipherSuites

()

Returns the list of cipher suites which are enabled by default.

abstract

String

[]

getSupportedCipherSuites

()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.

- Methods declared in class javax.net.

ServerSocketFactory

createServerSocket

,

createServerSocket

,

createServerSocket

,

createServerSocket

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

Returns the default SSL server socket factory.

Returns the list of cipher suites which are enabled by default.

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.

Methods declared in class javax.net.

ServerSocketFactory

createServerSocket

,

createServerSocket

,

createServerSocket

,

createServerSocket

---

#### Methods declared in class javax.net. ServerSocketFactory

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

- SSLServerSocketFactory

```java
protected SSLServerSocketFactory()
```

Constructor is used only by subclasses.

============ METHOD DETAIL ==========

- Method Detail

- getDefault

```java
public static
ServerSocketFactory
getDefault()
```

Returns the default SSL server socket factory.

The first time this method is called, the security property
"ssl.ServerSocketFactory.provider" is examined. If it is non-null, a
class by that name is loaded and instantiated. If that is successful and
the object is an instance of SSLServerSocketFactory, it is made the
default SSL server socket factory.

Otherwise, this method returns

SSLContext.getDefault().getServerSocketFactory()

. If that
call fails, an inoperative factory is returned.

**Returns:** the default

ServerSocketFactory
**See Also:** SSLContext.getDefault()

- getDefaultCipherSuites

```java
public abstract
String
[] getDefaultCipherSuites()
```

Returns the list of cipher suites which are enabled by default.
Unless a different list is enabled, handshaking on an SSL connection
will use one of these cipher suites. The minimum quality of service
for these defaults requires confidentiality protection and server
authentication (that is, no anonymous cipher suites).

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** array of the cipher suites enabled by default
**See Also:** getSupportedCipherSuites()

- getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.
Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getDefaultCipherSuites()

Constructor Detail

- SSLServerSocketFactory

```java
protected SSLServerSocketFactory()
```

Constructor is used only by subclasses.

---

#### Constructor Detail

SSLServerSocketFactory

```java
protected SSLServerSocketFactory()
```

Constructor is used only by subclasses.

---

#### SSLServerSocketFactory

protected SSLServerSocketFactory()

Constructor is used only by subclasses.

Method Detail

- getDefault

```java
public static
ServerSocketFactory
getDefault()
```

Returns the default SSL server socket factory.

The first time this method is called, the security property
"ssl.ServerSocketFactory.provider" is examined. If it is non-null, a
class by that name is loaded and instantiated. If that is successful and
the object is an instance of SSLServerSocketFactory, it is made the
default SSL server socket factory.

Otherwise, this method returns

SSLContext.getDefault().getServerSocketFactory()

. If that
call fails, an inoperative factory is returned.

**Returns:** the default

ServerSocketFactory
**See Also:** SSLContext.getDefault()

- getDefaultCipherSuites

```java
public abstract
String
[] getDefaultCipherSuites()
```

Returns the list of cipher suites which are enabled by default.
Unless a different list is enabled, handshaking on an SSL connection
will use one of these cipher suites. The minimum quality of service
for these defaults requires confidentiality protection and server
authentication (that is, no anonymous cipher suites).

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** array of the cipher suites enabled by default
**See Also:** getSupportedCipherSuites()

- getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.
Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getDefaultCipherSuites()

---

#### Method Detail

getDefault

```java
public static
ServerSocketFactory
getDefault()
```

Returns the default SSL server socket factory.

The first time this method is called, the security property
"ssl.ServerSocketFactory.provider" is examined. If it is non-null, a
class by that name is loaded and instantiated. If that is successful and
the object is an instance of SSLServerSocketFactory, it is made the
default SSL server socket factory.

Otherwise, this method returns

SSLContext.getDefault().getServerSocketFactory()

. If that
call fails, an inoperative factory is returned.

**Returns:** the default

ServerSocketFactory
**See Also:** SSLContext.getDefault()

---

#### getDefault

public static

ServerSocketFactory

getDefault()

Returns the default SSL server socket factory.

The first time this method is called, the security property
"ssl.ServerSocketFactory.provider" is examined. If it is non-null, a
class by that name is loaded and instantiated. If that is successful and
the object is an instance of SSLServerSocketFactory, it is made the
default SSL server socket factory.

Otherwise, this method returns

SSLContext.getDefault().getServerSocketFactory()

. If that
call fails, an inoperative factory is returned.

The first time this method is called, the security property
"ssl.ServerSocketFactory.provider" is examined. If it is non-null, a
class by that name is loaded and instantiated. If that is successful and
the object is an instance of SSLServerSocketFactory, it is made the
default SSL server socket factory.

Otherwise, this method returns

SSLContext.getDefault().getServerSocketFactory()

. If that
call fails, an inoperative factory is returned.

Otherwise, this method returns

SSLContext.getDefault().getServerSocketFactory()

. If that
call fails, an inoperative factory is returned.

getDefaultCipherSuites

```java
public abstract
String
[] getDefaultCipherSuites()
```

Returns the list of cipher suites which are enabled by default.
Unless a different list is enabled, handshaking on an SSL connection
will use one of these cipher suites. The minimum quality of service
for these defaults requires confidentiality protection and server
authentication (that is, no anonymous cipher suites).

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** array of the cipher suites enabled by default
**See Also:** getSupportedCipherSuites()

---

#### getDefaultCipherSuites

public abstract

String

[] getDefaultCipherSuites()

Returns the list of cipher suites which are enabled by default.
Unless a different list is enabled, handshaking on an SSL connection
will use one of these cipher suites. The minimum quality of service
for these defaults requires confidentiality protection and server
authentication (that is, no anonymous cipher suites).

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.
Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getDefaultCipherSuites()

---

#### getSupportedCipherSuites

public abstract

String

[] getSupportedCipherSuites()

Returns the names of the cipher suites which could be enabled for use
on an SSL connection created by this factory.
Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites are useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

---

