# Class SimpleDoc

**Source:** `java.desktop\javax\print\SimpleDoc.html`

### Class Description

```java
public final class
SimpleDoc

extends
Object

implements
Doc
```

This class is an implementation of interface

Doc

that can be used in
many common printing requests. It can handle all of the presently defined
"pre-defined" doc flavors defined as static variables in the

DocFlavor

class.

In particular this class implements certain required semantics of the

Doc

specification as follows:

- constructs a stream for the service if requested and appropriate.

ensures the same object is returned for each call on a method.

ensures multiple threads can access the

Doc

performs some validation of that the data matches the doc flavor.

Clients who want to re-use the doc object in other jobs, or need a

MultiDoc

will not want to use this class.

If the print data is a stream, or a print job requests data as a stream, then

SimpleDoc

does not monitor if the service properly closes the stream
after data transfer completion or job termination. Clients may prefer to use
provide their own implementation of doc that adds a listener to monitor job
completion and to validate that resources such as streams are freed (ie
closed).

**All Implemented Interfaces:** Doc

---

### Field Details

*No entries found.*

### Constructor Details

#### public SimpleDoc​(
Object
printData,

DocFlavor
flavor,

DocAttributeSet
attributes)

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

**Parameters:**
- printData

- the print data object
- flavor

- the

DocFlavor

object
- attributes

- a

DocAttributeSet

, which can be

null

**Throws:**
- IllegalArgumentException

- if

flavor

or

printData

is

null

, or the

printData

does not correspond to
the specified doc flavor--for example, the data is not of the
type specified as the representation in the

DocFlavor

---

### Method Details

#### public
DocFlavor
getDocFlavor()

Determines the doc flavor in which this doc object will supply its piece
of print data.

**Specified by:**
- getDocFlavor

in interface

Doc

**Returns:**
- doc flavor

---

#### public
DocAttributeSet
getAttributes()

Obtains the set of printing attributes for this doc object. If the
returned attribute set includes an instance of a particular attribute

X,

the printer must use that attribute value for this doc,
overriding any value of attribute

X

in the job's attribute set. If
the returned attribute set does not include an instance of a particular
attribute

X

or if

null

is returned, the printer must
consult the job's attribute set to obtain the value for attribute

X,

and if not found there, the printer must use an
implementation-dependent default value. The returned attribute set is
unmodifiable.

**Specified by:**
- getAttributes

in interface

Doc

**Returns:**
- unmodifiable set of printing attributes for this doc, or

null

to obtain all attribute values from the job's
attribute set

---

#### public
Object
getPrintData()
throws
IOException

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor. The

getPrintData()

method returns an instance of the
representation class whose name is given by

getDocFlavor()

.

getRepresentationClassName()

, and the return value can be cast from
class

Object

to that representation class.

**Specified by:**
- getPrintData

in interface

Doc

**Returns:**
- print data representation object

**Throws:**
- IOException

- if the representation class is a stream and there was
an I/O error while constructing the stream

---

#### public
Reader
getReaderForText()
throws
IOException

Obtains a reader for extracting character print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes, and return

null

otherwise:

- char[]

java.lang.String

java.io.Reader

The doc's print data representation object is used to construct and
return a

Reader

for reading the print data as a stream of
characters from the print data representation object. However, if the
print data representation object is itself a

Reader

then the
print data representation object is simply returned.

**Specified by:**
- getReaderForText

in interface

Doc

**Returns:**
- a

Reader

for reading the print data characters from this
doc. If a reader cannot be provided because this doc does not
meet the criteria stated above,

null

is returned.

**Throws:**
- IOException

- if there was an I/O error while creating the reader

---

#### public
InputStream
getStreamForBytes()
throws
IOException

Obtains an input stream for extracting byte print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes; otherwise this method returns

null

:

- byte[]

java.io.InputStream

The doc's print data representation object is obtained. Then, an input
stream for reading the print data from the print data representation
object as a stream of bytes is created and returned. However, if the
print data representation object is itself an input stream then the print
data representation object is simply returned.

**Specified by:**
- getStreamForBytes

in interface

Doc

**Returns:**
- an

InputStream

for reading the print data bytes from this
doc. If an input stream cannot be provided because this doc does
not meet the criteria stated above,

null

is returned.

**Throws:**
- IOException

- if there was an I/O error while creating the input
stream

---

### Additional Sections

#### Class SimpleDoc

java.lang.Object

- javax.print.SimpleDoc

javax.print.SimpleDoc

**All Implemented Interfaces:** Doc

```java
public final class
SimpleDoc

extends
Object

implements
Doc
```

This class is an implementation of interface

Doc

that can be used in
many common printing requests. It can handle all of the presently defined
"pre-defined" doc flavors defined as static variables in the

DocFlavor

class.

In particular this class implements certain required semantics of the

Doc

specification as follows:

- constructs a stream for the service if requested and appropriate.

ensures the same object is returned for each call on a method.

ensures multiple threads can access the

Doc

performs some validation of that the data matches the doc flavor.

Clients who want to re-use the doc object in other jobs, or need a

MultiDoc

will not want to use this class.

If the print data is a stream, or a print job requests data as a stream, then

SimpleDoc

does not monitor if the service properly closes the stream
after data transfer completion or job termination. Clients may prefer to use
provide their own implementation of doc that adds a listener to monitor job
completion and to validate that resources such as streams are freed (ie
closed).

public final class

SimpleDoc

extends

Object

implements

Doc

This class is an implementation of interface

Doc

that can be used in
many common printing requests. It can handle all of the presently defined
"pre-defined" doc flavors defined as static variables in the

DocFlavor

class.

In particular this class implements certain required semantics of the

Doc

specification as follows:

- constructs a stream for the service if requested and appropriate.

ensures the same object is returned for each call on a method.

ensures multiple threads can access the

Doc

performs some validation of that the data matches the doc flavor.

Clients who want to re-use the doc object in other jobs, or need a

MultiDoc

will not want to use this class.

If the print data is a stream, or a print job requests data as a stream, then

SimpleDoc

does not monitor if the service properly closes the stream
after data transfer completion or job termination. Clients may prefer to use
provide their own implementation of doc that adds a listener to monitor job
completion and to validate that resources such as streams are freed (ie
closed).

In particular this class implements certain required semantics of the

Doc

specification as follows:

- constructs a stream for the service if requested and appropriate.

ensures the same object is returned for each call on a method.

ensures multiple threads can access the

Doc

performs some validation of that the data matches the doc flavor.

Clients who want to re-use the doc object in other jobs, or need a

MultiDoc

will not want to use this class.

If the print data is a stream, or a print job requests data as a stream, then

SimpleDoc

does not monitor if the service properly closes the stream
after data transfer completion or job termination. Clients may prefer to use
provide their own implementation of doc that adds a listener to monitor job
completion and to validate that resources such as streams are freed (ie
closed).

constructs a stream for the service if requested and appropriate.

ensures the same object is returned for each call on a method.

ensures multiple threads can access the

Doc

performs some validation of that the data matches the doc flavor.

If the print data is a stream, or a print job requests data as a stream, then

SimpleDoc

does not monitor if the service properly closes the stream
after data transfer completion or job termination. Clients may prefer to use
provide their own implementation of doc that adds a listener to monitor job
completion and to validate that resources such as streams are freed (ie
closed).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleDoc

​(

Object

printData,

DocFlavor

flavor,

DocAttributeSet

attributes)

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DocAttributeSet

getAttributes

()

Obtains the set of printing attributes for this doc object.

DocFlavor

getDocFlavor

()

Determines the doc flavor in which this doc object will supply its piece
of print data.

Object

getPrintData

()

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor.

Reader

getReaderForText

()

Obtains a reader for extracting character print data from this doc.

InputStream

getStreamForBytes

()

Obtains an input stream for extracting byte print data from this doc.

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

SimpleDoc

​(

Object

printData,

DocFlavor

flavor,

DocAttributeSet

attributes)

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

---

#### Constructor Summary

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DocAttributeSet

getAttributes

()

Obtains the set of printing attributes for this doc object.

DocFlavor

getDocFlavor

()

Determines the doc flavor in which this doc object will supply its piece
of print data.

Object

getPrintData

()

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor.

Reader

getReaderForText

()

Obtains a reader for extracting character print data from this doc.

InputStream

getStreamForBytes

()

Obtains an input stream for extracting byte print data from this doc.

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

Obtains the set of printing attributes for this doc object.

Determines the doc flavor in which this doc object will supply its piece
of print data.

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor.

Obtains a reader for extracting character print data from this doc.

Obtains an input stream for extracting byte print data from this doc.

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

- SimpleDoc

```java
public SimpleDoc​(
Object
printData,

DocFlavor
flavor,

DocAttributeSet
attributes)
```

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

**Parameters:** printData

- the print data object
**Parameters:** flavor

- the

DocFlavor

object
**Parameters:** attributes

- a

DocAttributeSet

, which can be

null
**Throws:** IllegalArgumentException

- if

flavor

or

printData

is

null

, or the

printData

does not correspond to
the specified doc flavor--for example, the data is not of the
type specified as the representation in the

DocFlavor

============ METHOD DETAIL ==========

- Method Detail

- getDocFlavor

```java
public
DocFlavor
getDocFlavor()
```

Determines the doc flavor in which this doc object will supply its piece
of print data.

**Specified by:** getDocFlavor

in interface

Doc
**Returns:** doc flavor

- getAttributes

```java
public
DocAttributeSet
getAttributes()
```

Obtains the set of printing attributes for this doc object. If the
returned attribute set includes an instance of a particular attribute

X,

the printer must use that attribute value for this doc,
overriding any value of attribute

X

in the job's attribute set. If
the returned attribute set does not include an instance of a particular
attribute

X

or if

null

is returned, the printer must
consult the job's attribute set to obtain the value for attribute

X,

and if not found there, the printer must use an
implementation-dependent default value. The returned attribute set is
unmodifiable.

**Specified by:** getAttributes

in interface

Doc
**Returns:** unmodifiable set of printing attributes for this doc, or

null

to obtain all attribute values from the job's
attribute set

- getPrintData

```java
public
Object
getPrintData()
throws
IOException
```

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor. The

getPrintData()

method returns an instance of the
representation class whose name is given by

getDocFlavor()

.

getRepresentationClassName()

, and the return value can be cast from
class

Object

to that representation class.

**Specified by:** getPrintData

in interface

Doc
**Returns:** print data representation object
**Throws:** IOException

- if the representation class is a stream and there was
an I/O error while constructing the stream

- getReaderForText

```java
public
Reader
getReaderForText()
throws
IOException
```

Obtains a reader for extracting character print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes, and return

null

otherwise:

- char[]

java.lang.String

java.io.Reader

The doc's print data representation object is used to construct and
return a

Reader

for reading the print data as a stream of
characters from the print data representation object. However, if the
print data representation object is itself a

Reader

then the
print data representation object is simply returned.

**Specified by:** getReaderForText

in interface

Doc
**Returns:** a

Reader

for reading the print data characters from this
doc. If a reader cannot be provided because this doc does not
meet the criteria stated above,

null

is returned.
**Throws:** IOException

- if there was an I/O error while creating the reader

- getStreamForBytes

```java
public
InputStream
getStreamForBytes()
throws
IOException
```

Obtains an input stream for extracting byte print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes; otherwise this method returns

null

:

- byte[]

java.io.InputStream

The doc's print data representation object is obtained. Then, an input
stream for reading the print data from the print data representation
object as a stream of bytes is created and returned. However, if the
print data representation object is itself an input stream then the print
data representation object is simply returned.

**Specified by:** getStreamForBytes

in interface

Doc
**Returns:** an

InputStream

for reading the print data bytes from this
doc. If an input stream cannot be provided because this doc does
not meet the criteria stated above,

null

is returned.
**Throws:** IOException

- if there was an I/O error while creating the input
stream

Constructor Detail

- SimpleDoc

```java
public SimpleDoc​(
Object
printData,

DocFlavor
flavor,

DocAttributeSet
attributes)
```

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

**Parameters:** printData

- the print data object
**Parameters:** flavor

- the

DocFlavor

object
**Parameters:** attributes

- a

DocAttributeSet

, which can be

null
**Throws:** IllegalArgumentException

- if

flavor

or

printData

is

null

, or the

printData

does not correspond to
the specified doc flavor--for example, the data is not of the
type specified as the representation in the

DocFlavor

---

#### Constructor Detail

SimpleDoc

```java
public SimpleDoc​(
Object
printData,

DocFlavor
flavor,

DocAttributeSet
attributes)
```

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

**Parameters:** printData

- the print data object
**Parameters:** flavor

- the

DocFlavor

object
**Parameters:** attributes

- a

DocAttributeSet

, which can be

null
**Throws:** IllegalArgumentException

- if

flavor

or

printData

is

null

, or the

printData

does not correspond to
the specified doc flavor--for example, the data is not of the
type specified as the representation in the

DocFlavor

---

#### SimpleDoc

public SimpleDoc​(

Object

printData,

DocFlavor

flavor,

DocAttributeSet

attributes)

Constructs a

SimpleDoc

with the specified print data, doc flavor
and doc attribute set.

Method Detail

- getDocFlavor

```java
public
DocFlavor
getDocFlavor()
```

Determines the doc flavor in which this doc object will supply its piece
of print data.

**Specified by:** getDocFlavor

in interface

Doc
**Returns:** doc flavor

- getAttributes

```java
public
DocAttributeSet
getAttributes()
```

Obtains the set of printing attributes for this doc object. If the
returned attribute set includes an instance of a particular attribute

X,

the printer must use that attribute value for this doc,
overriding any value of attribute

X

in the job's attribute set. If
the returned attribute set does not include an instance of a particular
attribute

X

or if

null

is returned, the printer must
consult the job's attribute set to obtain the value for attribute

X,

and if not found there, the printer must use an
implementation-dependent default value. The returned attribute set is
unmodifiable.

**Specified by:** getAttributes

in interface

Doc
**Returns:** unmodifiable set of printing attributes for this doc, or

null

to obtain all attribute values from the job's
attribute set

- getPrintData

```java
public
Object
getPrintData()
throws
IOException
```

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor. The

getPrintData()

method returns an instance of the
representation class whose name is given by

getDocFlavor()

.

getRepresentationClassName()

, and the return value can be cast from
class

Object

to that representation class.

**Specified by:** getPrintData

in interface

Doc
**Returns:** print data representation object
**Throws:** IOException

- if the representation class is a stream and there was
an I/O error while constructing the stream

- getReaderForText

```java
public
Reader
getReaderForText()
throws
IOException
```

Obtains a reader for extracting character print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes, and return

null

otherwise:

- char[]

java.lang.String

java.io.Reader

The doc's print data representation object is used to construct and
return a

Reader

for reading the print data as a stream of
characters from the print data representation object. However, if the
print data representation object is itself a

Reader

then the
print data representation object is simply returned.

**Specified by:** getReaderForText

in interface

Doc
**Returns:** a

Reader

for reading the print data characters from this
doc. If a reader cannot be provided because this doc does not
meet the criteria stated above,

null

is returned.
**Throws:** IOException

- if there was an I/O error while creating the reader

- getStreamForBytes

```java
public
InputStream
getStreamForBytes()
throws
IOException
```

Obtains an input stream for extracting byte print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes; otherwise this method returns

null

:

- byte[]

java.io.InputStream

The doc's print data representation object is obtained. Then, an input
stream for reading the print data from the print data representation
object as a stream of bytes is created and returned. However, if the
print data representation object is itself an input stream then the print
data representation object is simply returned.

**Specified by:** getStreamForBytes

in interface

Doc
**Returns:** an

InputStream

for reading the print data bytes from this
doc. If an input stream cannot be provided because this doc does
not meet the criteria stated above,

null

is returned.
**Throws:** IOException

- if there was an I/O error while creating the input
stream

---

#### Method Detail

getDocFlavor

```java
public
DocFlavor
getDocFlavor()
```

Determines the doc flavor in which this doc object will supply its piece
of print data.

**Specified by:** getDocFlavor

in interface

Doc
**Returns:** doc flavor

---

#### getDocFlavor

public

DocFlavor

getDocFlavor()

Determines the doc flavor in which this doc object will supply its piece
of print data.

getAttributes

```java
public
DocAttributeSet
getAttributes()
```

Obtains the set of printing attributes for this doc object. If the
returned attribute set includes an instance of a particular attribute

X,

the printer must use that attribute value for this doc,
overriding any value of attribute

X

in the job's attribute set. If
the returned attribute set does not include an instance of a particular
attribute

X

or if

null

is returned, the printer must
consult the job's attribute set to obtain the value for attribute

X,

and if not found there, the printer must use an
implementation-dependent default value. The returned attribute set is
unmodifiable.

**Specified by:** getAttributes

in interface

Doc
**Returns:** unmodifiable set of printing attributes for this doc, or

null

to obtain all attribute values from the job's
attribute set

---

#### getAttributes

public

DocAttributeSet

getAttributes()

Obtains the set of printing attributes for this doc object. If the
returned attribute set includes an instance of a particular attribute

X,

the printer must use that attribute value for this doc,
overriding any value of attribute

X

in the job's attribute set. If
the returned attribute set does not include an instance of a particular
attribute

X

or if

null

is returned, the printer must
consult the job's attribute set to obtain the value for attribute

X,

and if not found there, the printer must use an
implementation-dependent default value. The returned attribute set is
unmodifiable.

getPrintData

```java
public
Object
getPrintData()
throws
IOException
```

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor. The

getPrintData()

method returns an instance of the
representation class whose name is given by

getDocFlavor()

.

getRepresentationClassName()

, and the return value can be cast from
class

Object

to that representation class.

**Specified by:** getPrintData

in interface

Doc
**Returns:** print data representation object
**Throws:** IOException

- if the representation class is a stream and there was
an I/O error while constructing the stream

---

#### getPrintData

public

Object

getPrintData()
throws

IOException

Obtains the print data representation object that contains this doc
object's piece of print data in the format corresponding to the supported
doc flavor. The

getPrintData()

method returns an instance of the
representation class whose name is given by

getDocFlavor()

.

getRepresentationClassName()

, and the return value can be cast from
class

Object

to that representation class.

getReaderForText

```java
public
Reader
getReaderForText()
throws
IOException
```

Obtains a reader for extracting character print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes, and return

null

otherwise:

- char[]

java.lang.String

java.io.Reader

The doc's print data representation object is used to construct and
return a

Reader

for reading the print data as a stream of
characters from the print data representation object. However, if the
print data representation object is itself a

Reader

then the
print data representation object is simply returned.

**Specified by:** getReaderForText

in interface

Doc
**Returns:** a

Reader

for reading the print data characters from this
doc. If a reader cannot be provided because this doc does not
meet the criteria stated above,

null

is returned.
**Throws:** IOException

- if there was an I/O error while creating the reader

---

#### getReaderForText

public

Reader

getReaderForText()
throws

IOException

Obtains a reader for extracting character print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes, and return

null

otherwise:

- char[]

java.lang.String

java.io.Reader

The doc's print data representation object is used to construct and
return a

Reader

for reading the print data as a stream of
characters from the print data representation object. However, if the
print data representation object is itself a

Reader

then the
print data representation object is simply returned.

char[]

java.lang.String

java.io.Reader

getStreamForBytes

```java
public
InputStream
getStreamForBytes()
throws
IOException
```

Obtains an input stream for extracting byte print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes; otherwise this method returns

null

:

- byte[]

java.io.InputStream

The doc's print data representation object is obtained. Then, an input
stream for reading the print data from the print data representation
object as a stream of bytes is created and returned. However, if the
print data representation object is itself an input stream then the print
data representation object is simply returned.

**Specified by:** getStreamForBytes

in interface

Doc
**Returns:** an

InputStream

for reading the print data bytes from this
doc. If an input stream cannot be provided because this doc does
not meet the criteria stated above,

null

is returned.
**Throws:** IOException

- if there was an I/O error while creating the input
stream

---

#### getStreamForBytes

public

InputStream

getStreamForBytes()
throws

IOException

Obtains an input stream for extracting byte print data from this doc. The

Doc

implementation is required to support this method if the

DocFlavor

has one of the following print data representation
classes; otherwise this method returns

null

:

- byte[]

java.io.InputStream

The doc's print data representation object is obtained. Then, an input
stream for reading the print data from the print data representation
object as a stream of bytes is created and returned. However, if the
print data representation object is itself an input stream then the print
data representation object is simply returned.

byte[]

java.io.InputStream

---

