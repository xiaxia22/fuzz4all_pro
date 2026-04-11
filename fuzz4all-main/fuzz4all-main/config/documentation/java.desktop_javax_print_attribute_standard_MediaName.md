# Class MediaName

**Source:** `java.desktop\javax\print\attribute\standard\MediaName.html`

### Class Description

```java
public class
MediaName

extends
Media

implements
Attribute
```

Class

MediaName

is a subclass of

Media

, a printing attribute
class (an enumeration) that specifies the media for a print job as a name.

This attribute can be used instead of specifying

MediaSize

or

MediaTray

.

Class

MediaName

currently declares a few standard media names.
Implementation- or site-defined names for a media name attribute may also be
created by defining a subclass of class

MediaName

.

IPP Compatibility:

MediaName

is a representation class for
values of the IPP "media" attribute which names media.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

#### public static final
MediaName
NA_LETTER_WHITE

white letter paper.

---

#### public static final
MediaName
NA_LETTER_TRANSPARENT

letter transparency.

---

#### public static final
MediaName
ISO_A4_WHITE

white A4 paper.

---

#### public static final
MediaName
ISO_A4_TRANSPARENT

A4 transparency.

---

### Constructor Details

#### protected MediaName​(int value)

Constructs a new media name enumeration value with the given integer
value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

MediaTray

.

**Overrides:**
- getStringTable

in class

EnumSyntax

**Returns:**
- the string table

---

#### protected
EnumSyntax
[] getEnumValueTable()

Returns the enumeration value table for class

MediaTray

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the enumeration value table

---

### Additional Sections

#### Class MediaName

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Media
- - javax.print.attribute.standard.MediaName

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Media
- - javax.print.attribute.standard.MediaName

javax.print.attribute.standard.Media

- javax.print.attribute.standard.MediaName

javax.print.attribute.standard.MediaName

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public class
MediaName

extends
Media

implements
Attribute
```

Class

MediaName

is a subclass of

Media

, a printing attribute
class (an enumeration) that specifies the media for a print job as a name.

This attribute can be used instead of specifying

MediaSize

or

MediaTray

.

Class

MediaName

currently declares a few standard media names.
Implementation- or site-defined names for a media name attribute may also be
created by defining a subclass of class

MediaName

.

IPP Compatibility:

MediaName

is a representation class for
values of the IPP "media" attribute which names media.

**See Also:** Serialized Form

public class

MediaName

extends

Media

implements

Attribute

Class

MediaName

is a subclass of

Media

, a printing attribute
class (an enumeration) that specifies the media for a print job as a name.

This attribute can be used instead of specifying

MediaSize

or

MediaTray

.

Class

MediaName

currently declares a few standard media names.
Implementation- or site-defined names for a media name attribute may also be
created by defining a subclass of class

MediaName

.

IPP Compatibility:

MediaName

is a representation class for
values of the IPP "media" attribute which names media.

This attribute can be used instead of specifying

MediaSize

or

MediaTray

.

Class

MediaName

currently declares a few standard media names.
Implementation- or site-defined names for a media name attribute may also be
created by defining a subclass of class

MediaName

.

IPP Compatibility:

MediaName

is a representation class for
values of the IPP "media" attribute which names media.

Class

MediaName

currently declares a few standard media names.
Implementation- or site-defined names for a media name attribute may also be
created by defining a subclass of class

MediaName

.

IPP Compatibility:

MediaName

is a representation class for
values of the IPP "media" attribute which names media.

IPP Compatibility:

MediaName

is a representation class for
values of the IPP "media" attribute which names media.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

MediaName

ISO_A4_TRANSPARENT

A4 transparency.

static

MediaName

ISO_A4_WHITE

white A4 paper.

static

MediaName

NA_LETTER_TRANSPARENT

letter transparency.

static

MediaName

NA_LETTER_WHITE

white letter paper.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MediaName

​(int value)

Constructs a new media name enumeration value with the given integer
value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

MediaTray

.

protected

String

[]

getStringTable

()

Returns the string table for class

MediaTray

.

- Methods declared in class javax.print.attribute.standard.

Media

equals

,

getCategory

,

getName

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

Field Summary

Fields

Modifier and Type

Field

Description

static

MediaName

ISO_A4_TRANSPARENT

A4 transparency.

static

MediaName

ISO_A4_WHITE

white A4 paper.

static

MediaName

NA_LETTER_TRANSPARENT

letter transparency.

static

MediaName

NA_LETTER_WHITE

white letter paper.

---

#### Field Summary

A4 transparency.

white A4 paper.

letter transparency.

white letter paper.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MediaName

​(int value)

Constructs a new media name enumeration value with the given integer
value.

---

#### Constructor Summary

Constructs a new media name enumeration value with the given integer
value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

MediaTray

.

protected

String

[]

getStringTable

()

Returns the string table for class

MediaTray

.

- Methods declared in class javax.print.attribute.standard.

Media

equals

,

getCategory

,

getName

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

---

#### Method Summary

Returns the enumeration value table for class

MediaTray

.

Returns the string table for class

MediaTray

.

Methods declared in class javax.print.attribute.standard.

Media

equals

,

getCategory

,

getName

---

#### Methods declared in class javax.print.attribute.standard. Media

Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

---

#### Methods declared in class javax.print.attribute. EnumSyntax

Methods declared in class java.lang.

Object

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

Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

---

#### Methods declared in interface javax.print.attribute. Attribute

============ FIELD DETAIL ===========

- Field Detail

- NA_LETTER_WHITE

```java
public static final
MediaName
NA_LETTER_WHITE
```

white letter paper.

- NA_LETTER_TRANSPARENT

```java
public static final
MediaName
NA_LETTER_TRANSPARENT
```

letter transparency.

- ISO_A4_WHITE

```java
public static final
MediaName
ISO_A4_WHITE
```

white A4 paper.

- ISO_A4_TRANSPARENT

```java
public static final
MediaName
ISO_A4_TRANSPARENT
```

A4 transparency.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MediaName

```java
protected MediaName​(int value)
```

Constructs a new media name enumeration value with the given integer
value.

**Parameters:** value

- Integer value

============ METHOD DETAIL ==========

- Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

MediaTray

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

MediaTray

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the enumeration value table

Field Detail

- NA_LETTER_WHITE

```java
public static final
MediaName
NA_LETTER_WHITE
```

white letter paper.

- NA_LETTER_TRANSPARENT

```java
public static final
MediaName
NA_LETTER_TRANSPARENT
```

letter transparency.

- ISO_A4_WHITE

```java
public static final
MediaName
ISO_A4_WHITE
```

white A4 paper.

- ISO_A4_TRANSPARENT

```java
public static final
MediaName
ISO_A4_TRANSPARENT
```

A4 transparency.

---

#### Field Detail

NA_LETTER_WHITE

```java
public static final
MediaName
NA_LETTER_WHITE
```

white letter paper.

---

#### NA_LETTER_WHITE

public static final

MediaName

NA_LETTER_WHITE

white letter paper.

NA_LETTER_TRANSPARENT

```java
public static final
MediaName
NA_LETTER_TRANSPARENT
```

letter transparency.

---

#### NA_LETTER_TRANSPARENT

public static final

MediaName

NA_LETTER_TRANSPARENT

letter transparency.

ISO_A4_WHITE

```java
public static final
MediaName
ISO_A4_WHITE
```

white A4 paper.

---

#### ISO_A4_WHITE

public static final

MediaName

ISO_A4_WHITE

white A4 paper.

ISO_A4_TRANSPARENT

```java
public static final
MediaName
ISO_A4_TRANSPARENT
```

A4 transparency.

---

#### ISO_A4_TRANSPARENT

public static final

MediaName

ISO_A4_TRANSPARENT

A4 transparency.

Constructor Detail

- MediaName

```java
protected MediaName​(int value)
```

Constructs a new media name enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

MediaName

```java
protected MediaName​(int value)
```

Constructs a new media name enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### MediaName

protected MediaName​(int value)

Constructs a new media name enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

MediaTray

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

MediaTray

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the enumeration value table

---

#### Method Detail

getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

MediaTray

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

---

#### getStringTable

protected

String

[] getStringTable()

Returns the string table for class

MediaTray

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

MediaTray

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the enumeration value table

---

#### getEnumValueTable

protected

EnumSyntax

[] getEnumValueTable()

Returns the enumeration value table for class

MediaTray

.

---

