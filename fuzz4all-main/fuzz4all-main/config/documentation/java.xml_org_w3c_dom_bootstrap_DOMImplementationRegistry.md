# Class DOMImplementationRegistry

**Source:** `java.xml\org\w3c\dom\bootstrap\DOMImplementationRegistry.html`

### Class Description

```java
public final class
DOMImplementationRegistry

extends
Object
```

A factory that enables applications to obtain instances of

DOMImplementation

.

Example:

```java
// get an instance of the DOMImplementation registry
DOMImplementationRegistry registry =
DOMImplementationRegistry.newInstance();
// get a DOM implementation the Level 3 XML module
DOMImplementation domImpl =
registry.getDOMImplementation("XML 3.0");
```

This provides an application with an implementation-independent starting
point. DOM implementations may modify this class to meet new security
standards or to provide *additional* fallbacks for the list of
DOMImplementationSources.

**Since:** 1.5, DOM Level 3
**See Also:** DOMImplementation

,

DOMImplementationSource

---

### Field Details

#### public static final
String
PROPERTY

The system property to specify the
DOMImplementationSource class names.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
DOMImplementationRegistry
newInstance()
throws
ClassNotFoundException
,

InstantiationException
,

IllegalAccessException
,

ClassCastException

Obtain a new instance of a

DOMImplementationRegistry

.

The

DOMImplementationRegistry

is initialized by the
application or the implementation, depending on the context, by
first checking the value of the Java system property

org.w3c.dom.DOMImplementationSourceList

and
the service provider whose contents are at
"

META_INF/services/org.w3c.dom.DOMImplementationSourceList

".
The value of this property is a white-space separated list of
names of availables classes implementing the

DOMImplementationSource

interface. Each class listed
in the class name list is instantiated and any exceptions
encountered are thrown to the application.

**Returns:**
- an initialized instance of DOMImplementationRegistry

**Throws:**
- ClassNotFoundException

- If any specified class can not be found
- InstantiationException

- If any specified class is an interface or abstract class
- IllegalAccessException

- If the default constructor of a specified class is not accessible
- ClassCastException

- If any specified class does not implement

DOMImplementationSource

---

#### public
DOMImplementation
getDOMImplementation​(
String
features)

Return the first implementation that has the desired
features, or

null

if none is found.

**Parameters:**
- features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"

**Returns:**
- An implementation that has the desired features,
or

null

if none found.

---

#### public
DOMImplementationList
getDOMImplementationList​(
String
features)

Return a list of implementations that support the
desired features.

**Parameters:**
- features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"

**Returns:**
- A list of DOMImplementations that support the desired features.

---

#### public void addSource​(
DOMImplementationSource
s)

Register an implementation.

**Parameters:**
- s

- The source to be registered, may not be

null

---

### Additional Sections

#### Class DOMImplementationRegistry

java.lang.Object

- org.w3c.dom.bootstrap.DOMImplementationRegistry

org.w3c.dom.bootstrap.DOMImplementationRegistry

```java
public final class
DOMImplementationRegistry

extends
Object
```

A factory that enables applications to obtain instances of

DOMImplementation

.

Example:

```java
// get an instance of the DOMImplementation registry
DOMImplementationRegistry registry =
DOMImplementationRegistry.newInstance();
// get a DOM implementation the Level 3 XML module
DOMImplementation domImpl =
registry.getDOMImplementation("XML 3.0");
```

This provides an application with an implementation-independent starting
point. DOM implementations may modify this class to meet new security
standards or to provide *additional* fallbacks for the list of
DOMImplementationSources.

**Since:** 1.5, DOM Level 3
**See Also:** DOMImplementation

,

DOMImplementationSource

public final class

DOMImplementationRegistry

extends

Object

A factory that enables applications to obtain instances of

DOMImplementation

.

Example:

```java
// get an instance of the DOMImplementation registry
DOMImplementationRegistry registry =
DOMImplementationRegistry.newInstance();
// get a DOM implementation the Level 3 XML module
DOMImplementation domImpl =
registry.getDOMImplementation("XML 3.0");
```

This provides an application with an implementation-independent starting
point. DOM implementations may modify this class to meet new security
standards or to provide *additional* fallbacks for the list of
DOMImplementationSources.

Example:

// get an instance of the DOMImplementation registry
DOMImplementationRegistry registry =
DOMImplementationRegistry.newInstance();
// get a DOM implementation the Level 3 XML module
DOMImplementation domImpl =
registry.getDOMImplementation("XML 3.0");

This provides an application with an implementation-independent starting
point. DOM implementations may modify this class to meet new security
standards or to provide *additional* fallbacks for the list of
DOMImplementationSources.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

PROPERTY

The system property to specify the
DOMImplementationSource class names.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addSource

​(

DOMImplementationSource

s)

Register an implementation.

DOMImplementation

getDOMImplementation

​(

String

features)

Return the first implementation that has the desired
features, or

null

if none is found.

DOMImplementationList

getDOMImplementationList

​(

String

features)

Return a list of implementations that support the
desired features.

static

DOMImplementationRegistry

newInstance

()

Obtain a new instance of a

DOMImplementationRegistry

.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

PROPERTY

The system property to specify the
DOMImplementationSource class names.

---

#### Field Summary

The system property to specify the
DOMImplementationSource class names.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addSource

​(

DOMImplementationSource

s)

Register an implementation.

DOMImplementation

getDOMImplementation

​(

String

features)

Return the first implementation that has the desired
features, or

null

if none is found.

DOMImplementationList

getDOMImplementationList

​(

String

features)

Return a list of implementations that support the
desired features.

static

DOMImplementationRegistry

newInstance

()

Obtain a new instance of a

DOMImplementationRegistry

.

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

Register an implementation.

Return the first implementation that has the desired
features, or

null

if none is found.

Return a list of implementations that support the
desired features.

Obtain a new instance of a

DOMImplementationRegistry

.

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

- PROPERTY

```java
public static final
String
PROPERTY
```

The system property to specify the
DOMImplementationSource class names.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- newInstance

```java
public static
DOMImplementationRegistry
newInstance()
throws
ClassNotFoundException
,

InstantiationException
,

IllegalAccessException
,

ClassCastException
```

Obtain a new instance of a

DOMImplementationRegistry

.

The

DOMImplementationRegistry

is initialized by the
application or the implementation, depending on the context, by
first checking the value of the Java system property

org.w3c.dom.DOMImplementationSourceList

and
the service provider whose contents are at
"

META_INF/services/org.w3c.dom.DOMImplementationSourceList

".
The value of this property is a white-space separated list of
names of availables classes implementing the

DOMImplementationSource

interface. Each class listed
in the class name list is instantiated and any exceptions
encountered are thrown to the application.

**Returns:** an initialized instance of DOMImplementationRegistry
**Throws:** ClassNotFoundException

- If any specified class can not be found
**Throws:** InstantiationException

- If any specified class is an interface or abstract class
**Throws:** IllegalAccessException

- If the default constructor of a specified class is not accessible
**Throws:** ClassCastException

- If any specified class does not implement

DOMImplementationSource

- getDOMImplementation

```java
public
DOMImplementation
getDOMImplementation​(
String
features)
```

Return the first implementation that has the desired
features, or

null

if none is found.

**Parameters:** features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"
**Returns:** An implementation that has the desired features,
or

null

if none found.

- getDOMImplementationList

```java
public
DOMImplementationList
getDOMImplementationList​(
String
features)
```

Return a list of implementations that support the
desired features.

**Parameters:** features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"
**Returns:** A list of DOMImplementations that support the desired features.

- addSource

```java
public void addSource​(
DOMImplementationSource
s)
```

Register an implementation.

**Parameters:** s

- The source to be registered, may not be

null

Field Detail

- PROPERTY

```java
public static final
String
PROPERTY
```

The system property to specify the
DOMImplementationSource class names.

**See Also:** Constant Field Values

---

#### Field Detail

PROPERTY

```java
public static final
String
PROPERTY
```

The system property to specify the
DOMImplementationSource class names.

**See Also:** Constant Field Values

---

#### PROPERTY

public static final

String

PROPERTY

The system property to specify the
DOMImplementationSource class names.

Method Detail

- newInstance

```java
public static
DOMImplementationRegistry
newInstance()
throws
ClassNotFoundException
,

InstantiationException
,

IllegalAccessException
,

ClassCastException
```

Obtain a new instance of a

DOMImplementationRegistry

.

The

DOMImplementationRegistry

is initialized by the
application or the implementation, depending on the context, by
first checking the value of the Java system property

org.w3c.dom.DOMImplementationSourceList

and
the service provider whose contents are at
"

META_INF/services/org.w3c.dom.DOMImplementationSourceList

".
The value of this property is a white-space separated list of
names of availables classes implementing the

DOMImplementationSource

interface. Each class listed
in the class name list is instantiated and any exceptions
encountered are thrown to the application.

**Returns:** an initialized instance of DOMImplementationRegistry
**Throws:** ClassNotFoundException

- If any specified class can not be found
**Throws:** InstantiationException

- If any specified class is an interface or abstract class
**Throws:** IllegalAccessException

- If the default constructor of a specified class is not accessible
**Throws:** ClassCastException

- If any specified class does not implement

DOMImplementationSource

- getDOMImplementation

```java
public
DOMImplementation
getDOMImplementation​(
String
features)
```

Return the first implementation that has the desired
features, or

null

if none is found.

**Parameters:** features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"
**Returns:** An implementation that has the desired features,
or

null

if none found.

- getDOMImplementationList

```java
public
DOMImplementationList
getDOMImplementationList​(
String
features)
```

Return a list of implementations that support the
desired features.

**Parameters:** features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"
**Returns:** A list of DOMImplementations that support the desired features.

- addSource

```java
public void addSource​(
DOMImplementationSource
s)
```

Register an implementation.

**Parameters:** s

- The source to be registered, may not be

null

---

#### Method Detail

newInstance

```java
public static
DOMImplementationRegistry
newInstance()
throws
ClassNotFoundException
,

InstantiationException
,

IllegalAccessException
,

ClassCastException
```

Obtain a new instance of a

DOMImplementationRegistry

.

The

DOMImplementationRegistry

is initialized by the
application or the implementation, depending on the context, by
first checking the value of the Java system property

org.w3c.dom.DOMImplementationSourceList

and
the service provider whose contents are at
"

META_INF/services/org.w3c.dom.DOMImplementationSourceList

".
The value of this property is a white-space separated list of
names of availables classes implementing the

DOMImplementationSource

interface. Each class listed
in the class name list is instantiated and any exceptions
encountered are thrown to the application.

**Returns:** an initialized instance of DOMImplementationRegistry
**Throws:** ClassNotFoundException

- If any specified class can not be found
**Throws:** InstantiationException

- If any specified class is an interface or abstract class
**Throws:** IllegalAccessException

- If the default constructor of a specified class is not accessible
**Throws:** ClassCastException

- If any specified class does not implement

DOMImplementationSource

---

#### newInstance

public static

DOMImplementationRegistry

newInstance()
throws

ClassNotFoundException

,

InstantiationException

,

IllegalAccessException

,

ClassCastException

Obtain a new instance of a

DOMImplementationRegistry

.

The

DOMImplementationRegistry

is initialized by the
application or the implementation, depending on the context, by
first checking the value of the Java system property

org.w3c.dom.DOMImplementationSourceList

and
the service provider whose contents are at
"

META_INF/services/org.w3c.dom.DOMImplementationSourceList

".
The value of this property is a white-space separated list of
names of availables classes implementing the

DOMImplementationSource

interface. Each class listed
in the class name list is instantiated and any exceptions
encountered are thrown to the application.

getDOMImplementation

```java
public
DOMImplementation
getDOMImplementation​(
String
features)
```

Return the first implementation that has the desired
features, or

null

if none is found.

**Parameters:** features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"
**Returns:** An implementation that has the desired features,
or

null

if none found.

---

#### getDOMImplementation

public

DOMImplementation

getDOMImplementation​(

String

features)

Return the first implementation that has the desired
features, or

null

if none is found.

getDOMImplementationList

```java
public
DOMImplementationList
getDOMImplementationList​(
String
features)
```

Return a list of implementations that support the
desired features.

**Parameters:** features

- A string that specifies which features are required. This is
a space separated list in which each feature is specified by
its name optionally followed by a space and a version number.
This is something like: "XML 1.0 Traversal +Events 2.0"
**Returns:** A list of DOMImplementations that support the desired features.

---

#### getDOMImplementationList

public

DOMImplementationList

getDOMImplementationList​(

String

features)

Return a list of implementations that support the
desired features.

addSource

```java
public void addSource​(
DOMImplementationSource
s)
```

Register an implementation.

**Parameters:** s

- The source to be registered, may not be

null

---

#### addSource

public void addSource​(

DOMImplementationSource

s)

Register an implementation.

---

