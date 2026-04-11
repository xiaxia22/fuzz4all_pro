# Class HttpServerProvider

**Source:** `jdk.httpserver\com\sun\net\httpserver\spi\HttpServerProvider.html`

### Class Description

```java
public abstract class
HttpServerProvider

extends
Object
```

Service provider class for HttpServer.
Sub-classes of HttpServerProvider provide an implementation of

HttpServer

and associated classes. Applications do not normally use
this class. See

provider()

for how providers are found and loaded.

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpServerProvider()

Initializes a new instance of this class.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("httpServerProvider")

---

### Method Details

#### public abstract
HttpServer
createHttpServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException

creates a HttpServer from this provider

**Parameters:**
- addr

- the address to bind to. May be

null
- backlog

- the socket backlog. A value of

zero

means the systems default

**Throws:**
- IOException

---

#### public abstract
HttpsServer
createHttpsServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException

creates a HttpsServer from this provider

**Parameters:**
- addr

- the address to bind to. May be

null
- backlog

- the socket backlog. A value of

zero

means the systems default

**Throws:**
- IOException

---

#### public static
HttpServerProvider
provider()

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

com.sun.net.httpserver.HttpServerProvider

is defined then it
is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified unchecked error or exception is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

com.sun.net.httpserver.HttpServerProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified unchecked error
or exception is thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:**
- The system-wide default HttpServerProvider

---

### Additional Sections

#### Class HttpServerProvider

java.lang.Object

- com.sun.net.httpserver.spi.HttpServerProvider

com.sun.net.httpserver.spi.HttpServerProvider

```java
public abstract class
HttpServerProvider

extends
Object
```

Service provider class for HttpServer.
Sub-classes of HttpServerProvider provide an implementation of

HttpServer

and associated classes. Applications do not normally use
this class. See

provider()

for how providers are found and loaded.

public abstract class

HttpServerProvider

extends

Object

Service provider class for HttpServer.
Sub-classes of HttpServerProvider provide an implementation of

HttpServer

and associated classes. Applications do not normally use
this class. See

provider()

for how providers are found and loaded.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpServerProvider

()

Initializes a new instance of this class.

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

abstract

HttpServer

createHttpServer

​(

InetSocketAddress

addr,
int backlog)

creates a HttpServer from this provider

abstract

HttpsServer

createHttpsServer

​(

InetSocketAddress

addr,
int backlog)

creates a HttpsServer from this provider

static

HttpServerProvider

provider

()

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

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

HttpServerProvider

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

HttpServer

createHttpServer

​(

InetSocketAddress

addr,
int backlog)

creates a HttpServer from this provider

abstract

HttpsServer

createHttpsServer

​(

InetSocketAddress

addr,
int backlog)

creates a HttpsServer from this provider

static

HttpServerProvider

provider

()

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

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

creates a HttpServer from this provider

creates a HttpsServer from this provider

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

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

- HttpServerProvider

```java
protected HttpServerProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("httpServerProvider")

============ METHOD DETAIL ==========

- Method Detail

- createHttpServer

```java
public abstract
HttpServer
createHttpServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

creates a HttpServer from this provider

**Parameters:** addr

- the address to bind to. May be

null
**Parameters:** backlog

- the socket backlog. A value of

zero

means the systems default
**Throws:** IOException

- createHttpsServer

```java
public abstract
HttpsServer
createHttpsServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

creates a HttpsServer from this provider

**Parameters:** addr

- the address to bind to. May be

null
**Parameters:** backlog

- the socket backlog. A value of

zero

means the systems default
**Throws:** IOException

- provider

```java
public static
HttpServerProvider
provider()
```

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

com.sun.net.httpserver.HttpServerProvider

is defined then it
is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified unchecked error or exception is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

com.sun.net.httpserver.HttpServerProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified unchecked error
or exception is thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:** The system-wide default HttpServerProvider

Constructor Detail

- HttpServerProvider

```java
protected HttpServerProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("httpServerProvider")

---

#### Constructor Detail

HttpServerProvider

```java
protected HttpServerProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("httpServerProvider")

---

#### HttpServerProvider

protected HttpServerProvider()

Initializes a new instance of this class.

Method Detail

- createHttpServer

```java
public abstract
HttpServer
createHttpServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

creates a HttpServer from this provider

**Parameters:** addr

- the address to bind to. May be

null
**Parameters:** backlog

- the socket backlog. A value of

zero

means the systems default
**Throws:** IOException

- createHttpsServer

```java
public abstract
HttpsServer
createHttpsServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

creates a HttpsServer from this provider

**Parameters:** addr

- the address to bind to. May be

null
**Parameters:** backlog

- the socket backlog. A value of

zero

means the systems default
**Throws:** IOException

- provider

```java
public static
HttpServerProvider
provider()
```

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

com.sun.net.httpserver.HttpServerProvider

is defined then it
is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified unchecked error or exception is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

com.sun.net.httpserver.HttpServerProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified unchecked error
or exception is thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:** The system-wide default HttpServerProvider

---

#### Method Detail

createHttpServer

```java
public abstract
HttpServer
createHttpServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

creates a HttpServer from this provider

**Parameters:** addr

- the address to bind to. May be

null
**Parameters:** backlog

- the socket backlog. A value of

zero

means the systems default
**Throws:** IOException

---

#### createHttpServer

public abstract

HttpServer

createHttpServer​(

InetSocketAddress

addr,
int backlog)
throws

IOException

creates a HttpServer from this provider

createHttpsServer

```java
public abstract
HttpsServer
createHttpsServer​(
InetSocketAddress
addr,
int backlog)
throws
IOException
```

creates a HttpsServer from this provider

**Parameters:** addr

- the address to bind to. May be

null
**Parameters:** backlog

- the socket backlog. A value of

zero

means the systems default
**Throws:** IOException

---

#### createHttpsServer

public abstract

HttpsServer

createHttpsServer​(

InetSocketAddress

addr,
int backlog)
throws

IOException

creates a HttpsServer from this provider

provider

```java
public static
HttpServerProvider
provider()
```

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

com.sun.net.httpserver.HttpServerProvider

is defined then it
is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified unchecked error or exception is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

com.sun.net.httpserver.HttpServerProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified unchecked error
or exception is thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:** The system-wide default HttpServerProvider

---

#### provider

public static

HttpServerProvider

provider()

Returns the system wide default HttpServerProvider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

com.sun.net.httpserver.HttpServerProvider

is defined then it
is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified unchecked error or exception is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

com.sun.net.httpserver.HttpServerProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified unchecked error
or exception is thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

The first invocation of this method locates the default provider
object as follows:

If the system property

com.sun.net.httpserver.HttpServerProvider

is defined then it
is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified unchecked error or exception is thrown.

If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

com.sun.net.httpserver.HttpServerProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified unchecked error
or exception is thrown.

Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

If the system property

com.sun.net.httpserver.HttpServerProvider

is defined then it
is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified unchecked error or exception is thrown.

If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

com.sun.net.httpserver.HttpServerProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified unchecked error
or exception is thrown.

Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

---

