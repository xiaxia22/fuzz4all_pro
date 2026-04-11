# Class PropertyResourceBundle

**Source:** `java.base\java\util\PropertyResourceBundle.html`

### Class Description

```java
public class
PropertyResourceBundle

extends
ResourceBundle
```

PropertyResourceBundle

is a concrete subclass of

ResourceBundle

that manages resources for a locale
using a set of static strings from a property file. See

ResourceBundle

for more information about resource
bundles.

Unlike other types of resource bundle, you don't subclass

PropertyResourceBundle

. Instead, you supply properties
files containing the resource data.

ResourceBundle.getBundle

will automatically look for the appropriate properties file and create a

PropertyResourceBundle

that refers to it. See

ResourceBundle.getBundle

for a complete description of the search and instantiation strategy.

The following

example

shows a member of a resource
bundle family with the base name "MyResources".
The text defines the bundle "MyResources_de",
the German member of the bundle family.
This member is based on

PropertyResourceBundle

, and the text
therefore is the content of the file "MyResources_de.properties"
(a related

example

shows
how you can add bundles to this family that are implemented as subclasses
of

ListResourceBundle

).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
# MessageFormat pattern
s1=Die Platte \"{1}\" enthält {0}.

# location of {0} in pattern
s2=1

# sample disk name
s3=Meine Platte

# first ChoiceFormat choice
s4=keine Dateien

# second ChoiceFormat choice
s5=eine Datei

# third ChoiceFormat choice
s6={0,number} Dateien

# sample date
s7=3. März 1996
```

**API Note:** PropertyResourceBundle

can be constructed either
from an

InputStream

or a

Reader

, which represents a property file.
Constructing a

PropertyResourceBundle

instance from an

InputStream

requires that the input stream be encoded in

UTF-8

. By default, if a

MalformedInputException

or an

UnmappableCharacterException

occurs on reading the
input stream, then the

PropertyResourceBundle

instance resets to the state
before the exception, re-reads the input stream in

ISO-8859-1

, and
continues reading. If the system property

java.util.PropertyResourceBundle.encoding

is set to either
"ISO-8859-1" or "UTF-8", the input stream is solely read in that encoding,
and throws the exception if it encounters an invalid sequence.
If "ISO-8859-1" is specified, characters that cannot be represented in
ISO-8859-1 encoding must be represented by Unicode Escapes as defined in section
3.3 of

The Java™ Language Specification

whereas the other constructor which takes a

Reader

does not have that limitation.
Other encoding values are ignored for this system property.
The system property is read and evaluated when initializing this class.
Changing or removing the property has no effect after the initialization.
**Implementation Requirements:** The implementation of a

PropertyResourceBundle

subclass must be
thread-safe if it's simultaneously used by multiple threads. The default
implementations of the non-abstract methods in this class are thread-safe.
**Since:** 1.1
**See Also:** ResourceBundle

,

ListResourceBundle

,

Properties

---

### Field Details

*No entries found.*

### Constructor Details

#### public PropertyResourceBundle​(
InputStream
stream)
throws
IOException

Creates a property resource bundle from an

InputStream

. This constructor reads the property file in UTF-8 by default.
If a

MalformedInputException

or an

UnmappableCharacterException

occurs on reading the
input stream, then the PropertyResourceBundle instance resets to the state
before the exception, re-reads the input stream in

ISO-8859-1

and
continues reading. If the system property

java.util.PropertyResourceBundle.encoding

is set to either
"ISO-8859-1" or "UTF-8", the input stream is solely read in that encoding,
and throws the exception if it encounters an invalid sequence. Other
encoding values are ignored for this system property.
The system property is read and evaluated when initializing this class.
Changing or removing the property has no effect after the initialization.

**Parameters:**
- stream

- an InputStream that represents a property file
to read from.

**Throws:**
- IOException

- if an I/O error occurs
- NullPointerException

- if

stream

is null
- IllegalArgumentException

- if

stream

contains a
malformed Unicode escape sequence.
- MalformedInputException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an invalid UTF-8 byte sequence.
- UnmappableCharacterException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an unmappable UTF-8 byte sequence.

---

#### public PropertyResourceBundle​(
Reader
reader)
throws
IOException

Creates a property resource bundle from a

Reader

. Unlike the constructor

PropertyResourceBundle(InputStream)

,
there is no limitation as to the encoding of the input property file.

**Parameters:**
- reader

- a Reader that represents a property file to
read from.

**Throws:**
- IOException

- if an I/O error occurs
- NullPointerException

- if

reader

is null
- IllegalArgumentException

- if a malformed Unicode escape sequence appears
from

reader

.

**Since:**
- 1.6

---

### Method Details

#### public
Enumeration
<
String
> getKeys()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:**
- getKeys

in class

ResourceBundle

**Returns:**
- an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**See Also:**
- ResourceBundle.keySet()

---

#### protected
Set
<
String
> handleKeySet()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:**
- handleKeySet

in class

ResourceBundle

**Returns:**
- a

Set

of the keys contained only in this

ResourceBundle

**See Also:**
- ResourceBundle.keySet()

**Since:**
- 1.6

---

### Additional Sections

#### Class PropertyResourceBundle

java.lang.Object

- java.util.ResourceBundle
- - java.util.PropertyResourceBundle

java.util.ResourceBundle

- java.util.PropertyResourceBundle

java.util.PropertyResourceBundle

```java
public class
PropertyResourceBundle

extends
ResourceBundle
```

PropertyResourceBundle

is a concrete subclass of

ResourceBundle

that manages resources for a locale
using a set of static strings from a property file. See

ResourceBundle

for more information about resource
bundles.

Unlike other types of resource bundle, you don't subclass

PropertyResourceBundle

. Instead, you supply properties
files containing the resource data.

ResourceBundle.getBundle

will automatically look for the appropriate properties file and create a

PropertyResourceBundle

that refers to it. See

ResourceBundle.getBundle

for a complete description of the search and instantiation strategy.

The following

example

shows a member of a resource
bundle family with the base name "MyResources".
The text defines the bundle "MyResources_de",
the German member of the bundle family.
This member is based on

PropertyResourceBundle

, and the text
therefore is the content of the file "MyResources_de.properties"
(a related

example

shows
how you can add bundles to this family that are implemented as subclasses
of

ListResourceBundle

).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
# MessageFormat pattern
s1=Die Platte \"{1}\" enthält {0}.

# location of {0} in pattern
s2=1

# sample disk name
s3=Meine Platte

# first ChoiceFormat choice
s4=keine Dateien

# second ChoiceFormat choice
s5=eine Datei

# third ChoiceFormat choice
s6={0,number} Dateien

# sample date
s7=3. März 1996
```

**API Note:** PropertyResourceBundle

can be constructed either
from an

InputStream

or a

Reader

, which represents a property file.
Constructing a

PropertyResourceBundle

instance from an

InputStream

requires that the input stream be encoded in

UTF-8

. By default, if a

MalformedInputException

or an

UnmappableCharacterException

occurs on reading the
input stream, then the

PropertyResourceBundle

instance resets to the state
before the exception, re-reads the input stream in

ISO-8859-1

, and
continues reading. If the system property

java.util.PropertyResourceBundle.encoding

is set to either
"ISO-8859-1" or "UTF-8", the input stream is solely read in that encoding,
and throws the exception if it encounters an invalid sequence.
If "ISO-8859-1" is specified, characters that cannot be represented in
ISO-8859-1 encoding must be represented by Unicode Escapes as defined in section
3.3 of

The Java™ Language Specification

whereas the other constructor which takes a

Reader

does not have that limitation.
Other encoding values are ignored for this system property.
The system property is read and evaluated when initializing this class.
Changing or removing the property has no effect after the initialization.
**Implementation Requirements:** The implementation of a

PropertyResourceBundle

subclass must be
thread-safe if it's simultaneously used by multiple threads. The default
implementations of the non-abstract methods in this class are thread-safe.
**Since:** 1.1
**See Also:** ResourceBundle

,

ListResourceBundle

,

Properties

public class

PropertyResourceBundle

extends

ResourceBundle

PropertyResourceBundle

is a concrete subclass of

ResourceBundle

that manages resources for a locale
using a set of static strings from a property file. See

ResourceBundle

for more information about resource
bundles.

Unlike other types of resource bundle, you don't subclass

PropertyResourceBundle

. Instead, you supply properties
files containing the resource data.

ResourceBundle.getBundle

will automatically look for the appropriate properties file and create a

PropertyResourceBundle

that refers to it. See

ResourceBundle.getBundle

for a complete description of the search and instantiation strategy.

The following

example

shows a member of a resource
bundle family with the base name "MyResources".
The text defines the bundle "MyResources_de",
the German member of the bundle family.
This member is based on

PropertyResourceBundle

, and the text
therefore is the content of the file "MyResources_de.properties"
(a related

example

shows
how you can add bundles to this family that are implemented as subclasses
of

ListResourceBundle

).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
# MessageFormat pattern
s1=Die Platte \"{1}\" enthält {0}.

# location of {0} in pattern
s2=1

# sample disk name
s3=Meine Platte

# first ChoiceFormat choice
s4=keine Dateien

# second ChoiceFormat choice
s5=eine Datei

# third ChoiceFormat choice
s6={0,number} Dateien

# sample date
s7=3. März 1996
```

Unlike other types of resource bundle, you don't subclass

PropertyResourceBundle

. Instead, you supply properties
files containing the resource data.

ResourceBundle.getBundle

will automatically look for the appropriate properties file and create a

PropertyResourceBundle

that refers to it. See

ResourceBundle.getBundle

for a complete description of the search and instantiation strategy.

The following

example

shows a member of a resource
bundle family with the base name "MyResources".
The text defines the bundle "MyResources_de",
the German member of the bundle family.
This member is based on

PropertyResourceBundle

, and the text
therefore is the content of the file "MyResources_de.properties"
(a related

example

shows
how you can add bundles to this family that are implemented as subclasses
of

ListResourceBundle

).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
# MessageFormat pattern
s1=Die Platte \"{1}\" enthält {0}.

# location of {0} in pattern
s2=1

# sample disk name
s3=Meine Platte

# first ChoiceFormat choice
s4=keine Dateien

# second ChoiceFormat choice
s5=eine Datei

# third ChoiceFormat choice
s6={0,number} Dateien

# sample date
s7=3. März 1996
```

The following

example

shows a member of a resource
bundle family with the base name "MyResources".
The text defines the bundle "MyResources_de",
the German member of the bundle family.
This member is based on

PropertyResourceBundle

, and the text
therefore is the content of the file "MyResources_de.properties"
(a related

example

shows
how you can add bundles to this family that are implemented as subclasses
of

ListResourceBundle

).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
# MessageFormat pattern
s1=Die Platte \"{1}\" enthält {0}.

# location of {0} in pattern
s2=1

# sample disk name
s3=Meine Platte

# first ChoiceFormat choice
s4=keine Dateien

# second ChoiceFormat choice
s5=eine Datei

# third ChoiceFormat choice
s6={0,number} Dateien

# sample date
s7=3. März 1996
```

# MessageFormat pattern
s1=Die Platte \"{1}\" enthält {0}.

# location of {0} in pattern
s2=1

# sample disk name
s3=Meine Platte

# first ChoiceFormat choice
s4=keine Dateien

# second ChoiceFormat choice
s5=eine Datei

# third ChoiceFormat choice
s6={0,number} Dateien

# sample date
s7=3. März 1996

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.util.

ResourceBundle

ResourceBundle.Control

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

ResourceBundle

parent

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PropertyResourceBundle

​(

InputStream

stream)

Creates a property resource bundle from an

InputStream

.

PropertyResourceBundle

​(

Reader

reader)

Creates a property resource bundle from a

Reader

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Enumeration

<

String

>

getKeys

()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

protected

Set

<

String

>

handleKeySet

()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

- Methods declared in class java.util.

ResourceBundle

clearCache

,

clearCache

,

containsKey

,

getBaseBundleName

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getLocale

,

getObject

,

getString

,

getStringArray

,

handleGetObject

,

keySet

,

setParent

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

- Nested classes/interfaces declared in class java.util.

ResourceBundle

ResourceBundle.Control

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.util.

ResourceBundle

ResourceBundle.Control

---

#### Nested classes/interfaces declared in class java.util. ResourceBundle

Field Summary

- Fields declared in class java.util.

ResourceBundle

parent

---

#### Field Summary

Fields declared in class java.util.

ResourceBundle

parent

---

#### Fields declared in class java.util. ResourceBundle

Constructor Summary

Constructors

Constructor

Description

PropertyResourceBundle

​(

InputStream

stream)

Creates a property resource bundle from an

InputStream

.

PropertyResourceBundle

​(

Reader

reader)

Creates a property resource bundle from a

Reader

.

---

#### Constructor Summary

Creates a property resource bundle from an

InputStream

.

Creates a property resource bundle from a

Reader

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Enumeration

<

String

>

getKeys

()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

protected

Set

<

String

>

handleKeySet

()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

- Methods declared in class java.util.

ResourceBundle

clearCache

,

clearCache

,

containsKey

,

getBaseBundleName

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getLocale

,

getObject

,

getString

,

getStringArray

,

handleGetObject

,

keySet

,

setParent

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

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

Methods declared in class java.util.

ResourceBundle

clearCache

,

clearCache

,

containsKey

,

getBaseBundleName

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getLocale

,

getObject

,

getString

,

getStringArray

,

handleGetObject

,

keySet

,

setParent

---

#### Methods declared in class java.util. ResourceBundle

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

- PropertyResourceBundle

```java
public PropertyResourceBundle​(
InputStream
stream)
throws
IOException
```

Creates a property resource bundle from an

InputStream

. This constructor reads the property file in UTF-8 by default.
If a

MalformedInputException

or an

UnmappableCharacterException

occurs on reading the
input stream, then the PropertyResourceBundle instance resets to the state
before the exception, re-reads the input stream in

ISO-8859-1

and
continues reading. If the system property

java.util.PropertyResourceBundle.encoding

is set to either
"ISO-8859-1" or "UTF-8", the input stream is solely read in that encoding,
and throws the exception if it encounters an invalid sequence. Other
encoding values are ignored for this system property.
The system property is read and evaluated when initializing this class.
Changing or removing the property has no effect after the initialization.

**Parameters:** stream

- an InputStream that represents a property file
to read from.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

stream

is null
**Throws:** IllegalArgumentException

- if

stream

contains a
malformed Unicode escape sequence.
**Throws:** MalformedInputException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an invalid UTF-8 byte sequence.
**Throws:** UnmappableCharacterException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an unmappable UTF-8 byte sequence.

- PropertyResourceBundle

```java
public PropertyResourceBundle​(
Reader
reader)
throws
IOException
```

Creates a property resource bundle from a

Reader

. Unlike the constructor

PropertyResourceBundle(InputStream)

,
there is no limitation as to the encoding of the input property file.

**Parameters:** reader

- a Reader that represents a property file to
read from.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

reader

is null
**Throws:** IllegalArgumentException

- if a malformed Unicode escape sequence appears
from

reader

.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getKeys

```java
public
Enumeration
<
String
> getKeys()
```

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:** getKeys

in class

ResourceBundle
**Returns:** an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.
**See Also:** ResourceBundle.keySet()

- handleKeySet

```java
protected
Set
<
String
> handleKeySet()
```

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:** handleKeySet

in class

ResourceBundle
**Returns:** a

Set

of the keys contained only in this

ResourceBundle
**Since:** 1.6
**See Also:** ResourceBundle.keySet()

Constructor Detail

- PropertyResourceBundle

```java
public PropertyResourceBundle​(
InputStream
stream)
throws
IOException
```

Creates a property resource bundle from an

InputStream

. This constructor reads the property file in UTF-8 by default.
If a

MalformedInputException

or an

UnmappableCharacterException

occurs on reading the
input stream, then the PropertyResourceBundle instance resets to the state
before the exception, re-reads the input stream in

ISO-8859-1

and
continues reading. If the system property

java.util.PropertyResourceBundle.encoding

is set to either
"ISO-8859-1" or "UTF-8", the input stream is solely read in that encoding,
and throws the exception if it encounters an invalid sequence. Other
encoding values are ignored for this system property.
The system property is read and evaluated when initializing this class.
Changing or removing the property has no effect after the initialization.

**Parameters:** stream

- an InputStream that represents a property file
to read from.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

stream

is null
**Throws:** IllegalArgumentException

- if

stream

contains a
malformed Unicode escape sequence.
**Throws:** MalformedInputException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an invalid UTF-8 byte sequence.
**Throws:** UnmappableCharacterException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an unmappable UTF-8 byte sequence.

- PropertyResourceBundle

```java
public PropertyResourceBundle​(
Reader
reader)
throws
IOException
```

Creates a property resource bundle from a

Reader

. Unlike the constructor

PropertyResourceBundle(InputStream)

,
there is no limitation as to the encoding of the input property file.

**Parameters:** reader

- a Reader that represents a property file to
read from.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

reader

is null
**Throws:** IllegalArgumentException

- if a malformed Unicode escape sequence appears
from

reader

.
**Since:** 1.6

---

#### Constructor Detail

PropertyResourceBundle

```java
public PropertyResourceBundle​(
InputStream
stream)
throws
IOException
```

Creates a property resource bundle from an

InputStream

. This constructor reads the property file in UTF-8 by default.
If a

MalformedInputException

or an

UnmappableCharacterException

occurs on reading the
input stream, then the PropertyResourceBundle instance resets to the state
before the exception, re-reads the input stream in

ISO-8859-1

and
continues reading. If the system property

java.util.PropertyResourceBundle.encoding

is set to either
"ISO-8859-1" or "UTF-8", the input stream is solely read in that encoding,
and throws the exception if it encounters an invalid sequence. Other
encoding values are ignored for this system property.
The system property is read and evaluated when initializing this class.
Changing or removing the property has no effect after the initialization.

**Parameters:** stream

- an InputStream that represents a property file
to read from.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

stream

is null
**Throws:** IllegalArgumentException

- if

stream

contains a
malformed Unicode escape sequence.
**Throws:** MalformedInputException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an invalid UTF-8 byte sequence.
**Throws:** UnmappableCharacterException

- if the system property

java.util.PropertyResourceBundle.encoding

is set to "UTF-8"
and

stream

contains an unmappable UTF-8 byte sequence.

---

#### PropertyResourceBundle

public PropertyResourceBundle​(

InputStream

stream)
throws

IOException

Creates a property resource bundle from an

InputStream

. This constructor reads the property file in UTF-8 by default.
If a

MalformedInputException

or an

UnmappableCharacterException

occurs on reading the
input stream, then the PropertyResourceBundle instance resets to the state
before the exception, re-reads the input stream in

ISO-8859-1

and
continues reading. If the system property

java.util.PropertyResourceBundle.encoding

is set to either
"ISO-8859-1" or "UTF-8", the input stream is solely read in that encoding,
and throws the exception if it encounters an invalid sequence. Other
encoding values are ignored for this system property.
The system property is read and evaluated when initializing this class.
Changing or removing the property has no effect after the initialization.

PropertyResourceBundle

```java
public PropertyResourceBundle​(
Reader
reader)
throws
IOException
```

Creates a property resource bundle from a

Reader

. Unlike the constructor

PropertyResourceBundle(InputStream)

,
there is no limitation as to the encoding of the input property file.

**Parameters:** reader

- a Reader that represents a property file to
read from.
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

reader

is null
**Throws:** IllegalArgumentException

- if a malformed Unicode escape sequence appears
from

reader

.
**Since:** 1.6

---

#### PropertyResourceBundle

public PropertyResourceBundle​(

Reader

reader)
throws

IOException

Creates a property resource bundle from a

Reader

. Unlike the constructor

PropertyResourceBundle(InputStream)

,
there is no limitation as to the encoding of the input property file.

Method Detail

- getKeys

```java
public
Enumeration
<
String
> getKeys()
```

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:** getKeys

in class

ResourceBundle
**Returns:** an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.
**See Also:** ResourceBundle.keySet()

- handleKeySet

```java
protected
Set
<
String
> handleKeySet()
```

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:** handleKeySet

in class

ResourceBundle
**Returns:** a

Set

of the keys contained only in this

ResourceBundle
**Since:** 1.6
**See Also:** ResourceBundle.keySet()

---

#### Method Detail

getKeys

```java
public
Enumeration
<
String
> getKeys()
```

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:** getKeys

in class

ResourceBundle
**Returns:** an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.
**See Also:** ResourceBundle.keySet()

---

#### getKeys

public

Enumeration

<

String

> getKeys()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

handleKeySet

```java
protected
Set
<
String
> handleKeySet()
```

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:** handleKeySet

in class

ResourceBundle
**Returns:** a

Set

of the keys contained only in this

ResourceBundle
**Since:** 1.6
**See Also:** ResourceBundle.keySet()

---

#### handleKeySet

protected

Set

<

String

> handleKeySet()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

---

