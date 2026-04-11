# Class XMLReaderFactory

**Source:** `java.xml\org\xml\sax\helpers\XMLReaderFactory.html`

### Class Description

```java
@Deprecated
(
since
="9")
public final class
XMLReaderFactory

extends
Object
```

Factory for creating an XML reader.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class contains static methods for creating an XML reader
from an explicit class name, or based on runtime defaults:

```java
try {
XMLReader myReader = XMLReaderFactory.createXMLReader();
} catch (SAXException e) {
System.err.println(e.getMessage());
}
```

Note to Distributions bundled with parsers:

You should modify the implementation of the no-arguments

createXMLReader

to handle cases where the external
configuration mechanisms aren't set up. That method should do its
best to return a parser when one is in the class path, even when
nothing bound its class name to

org.xml.sax.driver

so
those configuration mechanisms would see it.

**Since:** 1.4, SAX 2.0

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
XMLReader
createXMLReader()
throws
SAXException

Obtains a new instance of a

XMLReader

.
This method uses the following ordered lookup procedure to find and load
the

XMLReader

implementation class:

- If the system property

org.xml.sax.driver

has a value, that is used as an XMLReader class name.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service

XMLReader

by using the

current thread's context class loader

.
If the context class loader is null, the

system class loader

will
be used.
- Deprecated. Look for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file available to the runtime.
- Otherwise, the system-default implementation is returned.

**Returns:**
- a new XMLReader.

**Throws:**
- SAXException

- If no default XMLReader class
can be identified and instantiated.

**See Also:**
- createXMLReader(java.lang.String)

**API Note:**
- The process that looks for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file does not
conform to the specification of the service-provider loading facility
as defined in

ServiceLoader

and therefore does not
support modularization. It is deprecated as of Java SE 9 and subject to
removal in a future release.

---

#### public static
XMLReader
createXMLReader​(
String
className)
throws
SAXException

Attempt to create an XML reader from a class name.

Given a class name, this method attempts to load
and instantiate the class as an XML reader.

Note that this method will not be usable in environments where
the caller (perhaps an applet) is not permitted to load classes
dynamically.

**Returns:**
- A new XML reader.

**Throws:**
- SAXException

- If the class cannot be
loaded, instantiated, and cast to XMLReader.

**See Also:**
- createXMLReader()

---

### Additional Sections

#### Class XMLReaderFactory

java.lang.Object

- org.xml.sax.helpers.XMLReaderFactory

org.xml.sax.helpers.XMLReaderFactory

```java
@Deprecated
(
since
="9")
public final class
XMLReaderFactory

extends
Object
```

Deprecated.

It is recommended to use

SAXParserFactory

instead.

Factory for creating an XML reader.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class contains static methods for creating an XML reader
from an explicit class name, or based on runtime defaults:

```java
try {
XMLReader myReader = XMLReaderFactory.createXMLReader();
} catch (SAXException e) {
System.err.println(e.getMessage());
}
```

Note to Distributions bundled with parsers:

You should modify the implementation of the no-arguments

createXMLReader

to handle cases where the external
configuration mechanisms aren't set up. That method should do its
best to return a parser when one is in the class path, even when
nothing bound its class name to

org.xml.sax.driver

so
those configuration mechanisms would see it.

**Since:** 1.4, SAX 2.0

@Deprecated

(

since

="9")
public final class

XMLReaderFactory

extends

Object

Factory for creating an XML reader.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class contains static methods for creating an XML reader
from an explicit class name, or based on runtime defaults:

```java
try {
XMLReader myReader = XMLReaderFactory.createXMLReader();
} catch (SAXException e) {
System.err.println(e.getMessage());
}
```

Note to Distributions bundled with parsers:

You should modify the implementation of the no-arguments

createXMLReader

to handle cases where the external
configuration mechanisms aren't set up. That method should do its
best to return a parser when one is in the class path, even when
nothing bound its class name to

org.xml.sax.driver

so
those configuration mechanisms would see it.

This class contains static methods for creating an XML reader
from an explicit class name, or based on runtime defaults:

```java
try {
XMLReader myReader = XMLReaderFactory.createXMLReader();
} catch (SAXException e) {
System.err.println(e.getMessage());
}
```

Note to Distributions bundled with parsers:

You should modify the implementation of the no-arguments

createXMLReader

to handle cases where the external
configuration mechanisms aren't set up. That method should do its
best to return a parser when one is in the class path, even when
nothing bound its class name to

org.xml.sax.driver

so
those configuration mechanisms would see it.

try {
XMLReader myReader = XMLReaderFactory.createXMLReader();
} catch (SAXException e) {
System.err.println(e.getMessage());
}

Note to Distributions bundled with parsers:

You should modify the implementation of the no-arguments

createXMLReader

to handle cases where the external
configuration mechanisms aren't set up. That method should do its
best to return a parser when one is in the class path, even when
nothing bound its class name to

org.xml.sax.driver

so
those configuration mechanisms would see it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

XMLReader

createXMLReader

()

Deprecated.

Obtains a new instance of a

XMLReader

.

static

XMLReader

createXMLReader

​(

String

className)

Deprecated.

Attempt to create an XML reader from a class name.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

XMLReader

createXMLReader

()

Deprecated.

Obtains a new instance of a

XMLReader

.

static

XMLReader

createXMLReader

​(

String

className)

Deprecated.

Attempt to create an XML reader from a class name.

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

Deprecated.

Obtains a new instance of a

XMLReader

.

Attempt to create an XML reader from a class name.

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

============ METHOD DETAIL ==========

- Method Detail

- createXMLReader

```java
public static
XMLReader
createXMLReader()
throws
SAXException
```

Deprecated.

Obtains a new instance of a

XMLReader

.
This method uses the following ordered lookup procedure to find and load
the

XMLReader

implementation class:

- If the system property

org.xml.sax.driver

has a value, that is used as an XMLReader class name.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service

XMLReader

by using the

current thread's context class loader

.
If the context class loader is null, the

system class loader

will
be used.
- Deprecated. Look for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file available to the runtime.
- Otherwise, the system-default implementation is returned.

**API Note:** The process that looks for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file does not
conform to the specification of the service-provider loading facility
as defined in

ServiceLoader

and therefore does not
support modularization. It is deprecated as of Java SE 9 and subject to
removal in a future release.
**Returns:** a new XMLReader.
**Throws:** SAXException

- If no default XMLReader class
can be identified and instantiated.
**See Also:** createXMLReader(java.lang.String)

- createXMLReader

```java
public static
XMLReader
createXMLReader​(
String
className)
throws
SAXException
```

Deprecated.

Attempt to create an XML reader from a class name.

Given a class name, this method attempts to load
and instantiate the class as an XML reader.

Note that this method will not be usable in environments where
the caller (perhaps an applet) is not permitted to load classes
dynamically.

**Returns:** A new XML reader.
**Throws:** SAXException

- If the class cannot be
loaded, instantiated, and cast to XMLReader.
**See Also:** createXMLReader()

Method Detail

- createXMLReader

```java
public static
XMLReader
createXMLReader()
throws
SAXException
```

Deprecated.

Obtains a new instance of a

XMLReader

.
This method uses the following ordered lookup procedure to find and load
the

XMLReader

implementation class:

- If the system property

org.xml.sax.driver

has a value, that is used as an XMLReader class name.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service

XMLReader

by using the

current thread's context class loader

.
If the context class loader is null, the

system class loader

will
be used.
- Deprecated. Look for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file available to the runtime.
- Otherwise, the system-default implementation is returned.

**API Note:** The process that looks for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file does not
conform to the specification of the service-provider loading facility
as defined in

ServiceLoader

and therefore does not
support modularization. It is deprecated as of Java SE 9 and subject to
removal in a future release.
**Returns:** a new XMLReader.
**Throws:** SAXException

- If no default XMLReader class
can be identified and instantiated.
**See Also:** createXMLReader(java.lang.String)

- createXMLReader

```java
public static
XMLReader
createXMLReader​(
String
className)
throws
SAXException
```

Deprecated.

Attempt to create an XML reader from a class name.

Given a class name, this method attempts to load
and instantiate the class as an XML reader.

Note that this method will not be usable in environments where
the caller (perhaps an applet) is not permitted to load classes
dynamically.

**Returns:** A new XML reader.
**Throws:** SAXException

- If the class cannot be
loaded, instantiated, and cast to XMLReader.
**See Also:** createXMLReader()

---

#### Method Detail

createXMLReader

```java
public static
XMLReader
createXMLReader()
throws
SAXException
```

Deprecated.

Obtains a new instance of a

XMLReader

.
This method uses the following ordered lookup procedure to find and load
the

XMLReader

implementation class:

- If the system property

org.xml.sax.driver

has a value, that is used as an XMLReader class name.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service

XMLReader

by using the

current thread's context class loader

.
If the context class loader is null, the

system class loader

will
be used.
- Deprecated. Look for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file available to the runtime.
- Otherwise, the system-default implementation is returned.

**API Note:** The process that looks for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file does not
conform to the specification of the service-provider loading facility
as defined in

ServiceLoader

and therefore does not
support modularization. It is deprecated as of Java SE 9 and subject to
removal in a future release.
**Returns:** a new XMLReader.
**Throws:** SAXException

- If no default XMLReader class
can be identified and instantiated.
**See Also:** createXMLReader(java.lang.String)

---

#### createXMLReader

public static

XMLReader

createXMLReader()
throws

SAXException

Obtains a new instance of a

XMLReader

.
This method uses the following ordered lookup procedure to find and load
the

XMLReader

implementation class:

- If the system property

org.xml.sax.driver

has a value, that is used as an XMLReader class name.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service

XMLReader

by using the

current thread's context class loader

.
If the context class loader is null, the

system class loader

will
be used.
- Deprecated. Look for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file available to the runtime.
- Otherwise, the system-default implementation is returned.

If the system property

org.xml.sax.driver

has a value, that is used as an XMLReader class name.

Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service

XMLReader

by using the

current thread's context class loader

.
If the context class loader is null, the

system class loader

will
be used.

Deprecated. Look for a class name in the

META-INF/services/org.xml.sax.driver

file in a jar file available to the runtime.

Otherwise, the system-default implementation is returned.

Otherwise, the system-default implementation is returned.

createXMLReader

```java
public static
XMLReader
createXMLReader​(
String
className)
throws
SAXException
```

Deprecated.

Attempt to create an XML reader from a class name.

Given a class name, this method attempts to load
and instantiate the class as an XML reader.

Note that this method will not be usable in environments where
the caller (perhaps an applet) is not permitted to load classes
dynamically.

**Returns:** A new XML reader.
**Throws:** SAXException

- If the class cannot be
loaded, instantiated, and cast to XMLReader.
**See Also:** createXMLReader()

---

#### createXMLReader

public static

XMLReader

createXMLReader​(

String

className)
throws

SAXException

Attempt to create an XML reader from a class name.

Given a class name, this method attempts to load
and instantiate the class as an XML reader.

Note that this method will not be usable in environments where
the caller (perhaps an applet) is not permitted to load classes
dynamically.

Given a class name, this method attempts to load
and instantiate the class as an XML reader.

Note that this method will not be usable in environments where
the caller (perhaps an applet) is not permitted to load classes
dynamically.

Note that this method will not be usable in environments where
the caller (perhaps an applet) is not permitted to load classes
dynamically.

---

