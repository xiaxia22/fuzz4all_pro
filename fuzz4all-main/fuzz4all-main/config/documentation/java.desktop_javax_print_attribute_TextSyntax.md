# Class TextSyntax

**Source:** `java.desktop\javax\print\attribute\TextSyntax.html`

### Class Description

```java
public abstract class
TextSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

TextSyntax

is an abstract base class providing the common
implementation of all attributes whose value is a string. The text attribute
includes a locale to indicate the natural language. Thus, a text attribute
always represents a localized string. Once constructed, a text attribute's
value is immutable.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TextSyntax​(
String
value,

Locale
locale)

Constructs a

TextAttribute

with the specified string and locale.

**Parameters:**
- value

- text string
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale for as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

value

is

null

---

### Method Details

#### public
String
getValue()

Returns this text attribute's text string.

**Returns:**
- the text string

---

#### public
Locale
getLocale()

Returns this text attribute's text string's natural language (locale).

**Returns:**
- the locale

---

#### public int hashCode()

Returns a hashcode for this text attribute.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashcode value for this object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
object)

Returns whether this text attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

TextSyntax

.

This text attribute's underlying string and

object

's
underlying string are equal.

This text attribute's locale and

object

's locale are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this text
attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a

String

identifying this text attribute. The

String

is the attribute's underlying text string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

identifying this object

---

### Additional Sections

#### Class TextSyntax

java.lang.Object

- javax.print.attribute.TextSyntax

javax.print.attribute.TextSyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** DocumentName

,

JobMessageFromOperator

,

JobName

,

JobOriginatingUserName

,

OutputDeviceAssigned

,

PrinterInfo

,

PrinterLocation

,

PrinterMakeAndModel

,

PrinterMessageFromOperator

,

PrinterName

,

RequestingUserName

```java
public abstract class
TextSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

TextSyntax

is an abstract base class providing the common
implementation of all attributes whose value is a string. The text attribute
includes a locale to indicate the natural language. Thus, a text attribute
always represents a localized string. Once constructed, a text attribute's
value is immutable.

**See Also:** Serialized Form

public abstract class

TextSyntax

extends

Object

implements

Serializable

,

Cloneable

Class

TextSyntax

is an abstract base class providing the common
implementation of all attributes whose value is a string. The text attribute
includes a locale to indicate the natural language. Thus, a text attribute
always represents a localized string. Once constructed, a text attribute's
value is immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TextSyntax

​(

String

value,

Locale

locale)

Constructs a

TextAttribute

with the specified string and locale.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this text attribute is equivalent to the passed in
object.

Locale

getLocale

()

Returns this text attribute's text string's natural language (locale).

String

getValue

()

Returns this text attribute's text string.

int

hashCode

()

Returns a hashcode for this text attribute.

String

toString

()

Returns a

String

identifying this text attribute.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

TextSyntax

​(

String

value,

Locale

locale)

Constructs a

TextAttribute

with the specified string and locale.

---

#### Constructor Summary

Constructs a

TextAttribute

with the specified string and locale.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this text attribute is equivalent to the passed in
object.

Locale

getLocale

()

Returns this text attribute's text string's natural language (locale).

String

getValue

()

Returns this text attribute's text string.

int

hashCode

()

Returns a hashcode for this text attribute.

String

toString

()

Returns a

String

identifying this text attribute.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns whether this text attribute is equivalent to the passed in
object.

Returns this text attribute's text string's natural language (locale).

Returns this text attribute's text string.

Returns a hashcode for this text attribute.

Returns a

String

identifying this text attribute.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- TextSyntax

```java
protected TextSyntax​(
String
value,

Locale
locale)
```

Constructs a

TextAttribute

with the specified string and locale.

**Parameters:** value

- text string
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale for as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

value

is

null

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public
String
getValue()
```

Returns this text attribute's text string.

**Returns:** the text string

- getLocale

```java
public
Locale
getLocale()
```

Returns this text attribute's text string's natural language (locale).

**Returns:** the locale

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this text attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this text attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

TextSyntax

.

This text attribute's underlying string and

object

's
underlying string are equal.

This text attribute's locale and

object

's locale are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this text
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a

String

identifying this text attribute. The

String

is the attribute's underlying text string.

**Overrides:** toString

in class

Object
**Returns:** a

String

identifying this object

Constructor Detail

- TextSyntax

```java
protected TextSyntax​(
String
value,

Locale
locale)
```

Constructs a

TextAttribute

with the specified string and locale.

**Parameters:** value

- text string
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale for as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

value

is

null

---

#### Constructor Detail

TextSyntax

```java
protected TextSyntax​(
String
value,

Locale
locale)
```

Constructs a

TextAttribute

with the specified string and locale.

**Parameters:** value

- text string
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale for as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

value

is

null

---

#### TextSyntax

protected TextSyntax​(

String

value,

Locale

locale)

Constructs a

TextAttribute

with the specified string and locale.

Method Detail

- getValue

```java
public
String
getValue()
```

Returns this text attribute's text string.

**Returns:** the text string

- getLocale

```java
public
Locale
getLocale()
```

Returns this text attribute's text string's natural language (locale).

**Returns:** the locale

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this text attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this text attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

TextSyntax

.

This text attribute's underlying string and

object

's
underlying string are equal.

This text attribute's locale and

object

's locale are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this text
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a

String

identifying this text attribute. The

String

is the attribute's underlying text string.

**Overrides:** toString

in class

Object
**Returns:** a

String

identifying this object

---

#### Method Detail

getValue

```java
public
String
getValue()
```

Returns this text attribute's text string.

**Returns:** the text string

---

#### getValue

public

String

getValue()

Returns this text attribute's text string.

getLocale

```java
public
Locale
getLocale()
```

Returns this text attribute's text string's natural language (locale).

**Returns:** the locale

---

#### getLocale

public

Locale

getLocale()

Returns this text attribute's text string's natural language (locale).

hashCode

```java
public int hashCode()
```

Returns a hashcode for this text attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hashcode value for this object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this text attribute.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this text attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

TextSyntax

.

This text attribute's underlying string and

object

's
underlying string are equal.

This text attribute's locale and

object

's locale are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this text
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Returns whether this text attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

TextSyntax

.

This text attribute's underlying string and

object

's
underlying string are equal.

This text attribute's locale and

object

's locale are equal.

object

is not

null

.

object

is an instance of class

TextSyntax

.

This text attribute's underlying string and

object

's
underlying string are equal.

This text attribute's locale and

object

's locale are equal.

toString

```java
public
String
toString()
```

Returns a

String

identifying this text attribute. The

String

is the attribute's underlying text string.

**Overrides:** toString

in class

Object
**Returns:** a

String

identifying this object

---

#### toString

public

String

toString()

Returns a

String

identifying this text attribute. The

String

is the attribute's underlying text string.

---

