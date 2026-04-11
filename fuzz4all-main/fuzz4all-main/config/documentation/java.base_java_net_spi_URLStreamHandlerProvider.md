# Class URLStreamHandlerProvider

**Source:** `java.base\java\net\spi\URLStreamHandlerProvider.html`

### Class Description

```java
public abstract class
URLStreamHandlerProvider

extends
Object

implements
URLStreamHandlerFactory
```

URL stream handler service-provider class.

A URL stream handler provider is a concrete subclass of this class that
has a zero-argument constructor. URL stream handler providers may be
installed in an instance of the Java platform by adding them to the
application class path.

A URL stream handler provider identifies itself with a
provider-configuration file named java.net.spi.URLStreamHandlerProvider in
the resource directory META-INF/services. The file should contain a list of
fully-qualified concrete URL stream handler provider class names, one per
line.

URL stream handler providers are located at runtime, as specified in the

URL constructor

.

**All Implemented Interfaces:** URLStreamHandlerFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### protected URLStreamHandlerProvider()

Initializes a new URL stream handler provider.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("setFactory")

.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class URLStreamHandlerProvider

java.lang.Object

- java.net.spi.URLStreamHandlerProvider

java.net.spi.URLStreamHandlerProvider

**All Implemented Interfaces:** URLStreamHandlerFactory

```java
public abstract class
URLStreamHandlerProvider

extends
Object

implements
URLStreamHandlerFactory
```

URL stream handler service-provider class.

A URL stream handler provider is a concrete subclass of this class that
has a zero-argument constructor. URL stream handler providers may be
installed in an instance of the Java platform by adding them to the
application class path.

A URL stream handler provider identifies itself with a
provider-configuration file named java.net.spi.URLStreamHandlerProvider in
the resource directory META-INF/services. The file should contain a list of
fully-qualified concrete URL stream handler provider class names, one per
line.

URL stream handler providers are located at runtime, as specified in the

URL constructor

.

**Since:** 9

public abstract class

URLStreamHandlerProvider

extends

Object

implements

URLStreamHandlerFactory

URL stream handler service-provider class.

A URL stream handler provider is a concrete subclass of this class that
has a zero-argument constructor. URL stream handler providers may be
installed in an instance of the Java platform by adding them to the
application class path.

A URL stream handler provider identifies itself with a
provider-configuration file named java.net.spi.URLStreamHandlerProvider in
the resource directory META-INF/services. The file should contain a list of
fully-qualified concrete URL stream handler provider class names, one per
line.

URL stream handler providers are located at runtime, as specified in the

URL constructor

.

A URL stream handler provider is a concrete subclass of this class that
has a zero-argument constructor. URL stream handler providers may be
installed in an instance of the Java platform by adding them to the
application class path.

A URL stream handler provider identifies itself with a
provider-configuration file named java.net.spi.URLStreamHandlerProvider in
the resource directory META-INF/services. The file should contain a list of
fully-qualified concrete URL stream handler provider class names, one per
line.

URL stream handler providers are located at runtime, as specified in the

URL constructor

.

A URL stream handler provider identifies itself with a
provider-configuration file named java.net.spi.URLStreamHandlerProvider in
the resource directory META-INF/services. The file should contain a list of
fully-qualified concrete URL stream handler provider class names, one per
line.

URL stream handler providers are located at runtime, as specified in the

URL constructor

.

URL stream handler providers are located at runtime, as specified in the

URL constructor

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

URLStreamHandlerProvider

()

Initializes a new URL stream handler provider.

========== METHOD SUMMARY ===========

- Method Summary

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

- Methods declared in interface java.net.

URLStreamHandlerFactory

createURLStreamHandler

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

URLStreamHandlerProvider

()

Initializes a new URL stream handler provider.

---

#### Constructor Summary

Initializes a new URL stream handler provider.

Method Summary

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

- Methods declared in interface java.net.

URLStreamHandlerFactory

createURLStreamHandler

---

#### Method Summary

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

Methods declared in interface java.net.

URLStreamHandlerFactory

createURLStreamHandler

---

#### Methods declared in interface java.net. URLStreamHandlerFactory

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- URLStreamHandlerProvider

```java
protected URLStreamHandlerProvider()
```

Initializes a new URL stream handler provider.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("setFactory")

.

Constructor Detail

- URLStreamHandlerProvider

```java
protected URLStreamHandlerProvider()
```

Initializes a new URL stream handler provider.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("setFactory")

.

---

#### Constructor Detail

URLStreamHandlerProvider

```java
protected URLStreamHandlerProvider()
```

Initializes a new URL stream handler provider.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("setFactory")

.

---

#### URLStreamHandlerProvider

protected URLStreamHandlerProvider()

Initializes a new URL stream handler provider.

---

