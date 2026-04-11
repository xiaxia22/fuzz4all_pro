# Interface LoaderHandler

**Source:** `java.rmi\java\rmi\server\LoaderHandler.html`

### Class Description

```java
@Deprecated

public interface
LoaderHandler
```

LoaderHandler

is an interface used internally by the RMI
runtime in previous implementation versions. It should never be accessed
by application code.

**Since:** 1.1

---

### Field Details

#### static final
String
packagePrefix

package of system

LoaderHandler

implementation.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

Class
<?> loadClass​(
String
name)
throws
MalformedURLException
,

ClassNotFoundException

Loads a class from the location specified by the

java.rmi.server.codebase

property.

**Parameters:**
- name

- the name of the class to load

**Returns:**
- the

Class

object representing the loaded class

**Throws:**
- MalformedURLException

- if the system property

java.rmi.server.codebase

contains an invalid URL
- ClassNotFoundException

- if a definition for the class could not
be found at the codebase location.

**Since:**
- 1.1

---

#### @Deprecated

Class
<?> loadClass​(
URL
codebase,

String
name)
throws
MalformedURLException
,

ClassNotFoundException

Loads a class from a URL.

**Parameters:**
- codebase

- the URL from which to load the class
- name

- the name of the class to load

**Returns:**
- the

Class

object representing the loaded class

**Throws:**
- MalformedURLException

- if the

codebase

paramater
contains an invalid URL
- ClassNotFoundException

- if a definition for the class could not
be found at the specified URL

**Since:**
- 1.1

---

#### @Deprecated

Object
getSecurityContext​(
ClassLoader
loader)

Returns the security context of the given class loader.

**Parameters:**
- loader

- a class loader from which to get the security context

**Returns:**
- the security context

**Since:**
- 1.1

---

### Additional Sections

#### Interface LoaderHandler

```java
@Deprecated

public interface
LoaderHandler
```

Deprecated.

no replacement

LoaderHandler

is an interface used internally by the RMI
runtime in previous implementation versions. It should never be accessed
by application code.

**Since:** 1.1

@Deprecated

public interface

LoaderHandler

LoaderHandler

is an interface used internally by the RMI
runtime in previous implementation versions. It should never be accessed
by application code.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

packagePrefix

Deprecated.

package of system

LoaderHandler

implementation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

getSecurityContext

​(

ClassLoader

loader)

Deprecated.

no replacement

Class

<?>

loadClass

​(

String

name)

Deprecated.

no replacement

Class

<?>

loadClass

​(

URL

codebase,

String

name)

Deprecated.

no replacement

Field Summary

Fields

Modifier and Type

Field

Description

static

String

packagePrefix

Deprecated.

package of system

LoaderHandler

implementation.

---

#### Field Summary

Deprecated.

package of system

LoaderHandler

implementation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

getSecurityContext

​(

ClassLoader

loader)

Deprecated.

no replacement

Class

<?>

loadClass

​(

String

name)

Deprecated.

no replacement

Class

<?>

loadClass

​(

URL

codebase,

String

name)

Deprecated.

no replacement

---

#### Method Summary

Deprecated.

no replacement

============ FIELD DETAIL ===========

- Field Detail

- packagePrefix

```java
static final
String
packagePrefix
```

Deprecated.

package of system

LoaderHandler

implementation.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- loadClass

```java
@Deprecated

Class
<?> loadClass​(
String
name)
throws
MalformedURLException
,

ClassNotFoundException
```

Deprecated.

no replacement

Loads a class from the location specified by the

java.rmi.server.codebase

property.

**Parameters:** name

- the name of the class to load
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if the system property

java.rmi.server.codebase

contains an invalid URL
**Throws:** ClassNotFoundException

- if a definition for the class could not
be found at the codebase location.
**Since:** 1.1

- loadClass

```java
@Deprecated

Class
<?> loadClass​(
URL
codebase,

String
name)
throws
MalformedURLException
,

ClassNotFoundException
```

Deprecated.

no replacement

Loads a class from a URL.

**Parameters:** codebase

- the URL from which to load the class
**Parameters:** name

- the name of the class to load
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if the

codebase

paramater
contains an invalid URL
**Throws:** ClassNotFoundException

- if a definition for the class could not
be found at the specified URL
**Since:** 1.1

- getSecurityContext

```java
@Deprecated

Object
getSecurityContext​(
ClassLoader
loader)
```

Deprecated.

no replacement

Returns the security context of the given class loader.

**Parameters:** loader

- a class loader from which to get the security context
**Returns:** the security context
**Since:** 1.1

Field Detail

- packagePrefix

```java
static final
String
packagePrefix
```

Deprecated.

package of system

LoaderHandler

implementation.

**See Also:** Constant Field Values

---

#### Field Detail

packagePrefix

```java
static final
String
packagePrefix
```

Deprecated.

package of system

LoaderHandler

implementation.

**See Also:** Constant Field Values

---

#### packagePrefix

static final

String

packagePrefix

package of system

LoaderHandler

implementation.

Method Detail

- loadClass

```java
@Deprecated

Class
<?> loadClass​(
String
name)
throws
MalformedURLException
,

ClassNotFoundException
```

Deprecated.

no replacement

Loads a class from the location specified by the

java.rmi.server.codebase

property.

**Parameters:** name

- the name of the class to load
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if the system property

java.rmi.server.codebase

contains an invalid URL
**Throws:** ClassNotFoundException

- if a definition for the class could not
be found at the codebase location.
**Since:** 1.1

- loadClass

```java
@Deprecated

Class
<?> loadClass​(
URL
codebase,

String
name)
throws
MalformedURLException
,

ClassNotFoundException
```

Deprecated.

no replacement

Loads a class from a URL.

**Parameters:** codebase

- the URL from which to load the class
**Parameters:** name

- the name of the class to load
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if the

codebase

paramater
contains an invalid URL
**Throws:** ClassNotFoundException

- if a definition for the class could not
be found at the specified URL
**Since:** 1.1

- getSecurityContext

```java
@Deprecated

Object
getSecurityContext​(
ClassLoader
loader)
```

Deprecated.

no replacement

Returns the security context of the given class loader.

**Parameters:** loader

- a class loader from which to get the security context
**Returns:** the security context
**Since:** 1.1

---

#### Method Detail

loadClass

```java
@Deprecated

Class
<?> loadClass​(
String
name)
throws
MalformedURLException
,

ClassNotFoundException
```

Deprecated.

no replacement

Loads a class from the location specified by the

java.rmi.server.codebase

property.

**Parameters:** name

- the name of the class to load
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if the system property

java.rmi.server.codebase

contains an invalid URL
**Throws:** ClassNotFoundException

- if a definition for the class could not
be found at the codebase location.
**Since:** 1.1

---

#### loadClass

@Deprecated

Class

<?> loadClass​(

String

name)
throws

MalformedURLException

,

ClassNotFoundException

Loads a class from the location specified by the

java.rmi.server.codebase

property.

loadClass

```java
@Deprecated

Class
<?> loadClass​(
URL
codebase,

String
name)
throws
MalformedURLException
,

ClassNotFoundException
```

Deprecated.

no replacement

Loads a class from a URL.

**Parameters:** codebase

- the URL from which to load the class
**Parameters:** name

- the name of the class to load
**Returns:** the

Class

object representing the loaded class
**Throws:** MalformedURLException

- if the

codebase

paramater
contains an invalid URL
**Throws:** ClassNotFoundException

- if a definition for the class could not
be found at the specified URL
**Since:** 1.1

---

#### loadClass

@Deprecated

Class

<?> loadClass​(

URL

codebase,

String

name)
throws

MalformedURLException

,

ClassNotFoundException

Loads a class from a URL.

getSecurityContext

```java
@Deprecated

Object
getSecurityContext​(
ClassLoader
loader)
```

Deprecated.

no replacement

Returns the security context of the given class loader.

**Parameters:** loader

- a class loader from which to get the security context
**Returns:** the security context
**Since:** 1.1

---

#### getSecurityContext

@Deprecated

Object

getSecurityContext​(

ClassLoader

loader)

Returns the security context of the given class loader.

---

