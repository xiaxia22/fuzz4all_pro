# Class MediaTray

**Source:** `java.desktop\javax\print\attribute\standard\MediaTray.html`

### Class Description

```java
public class
MediaTray

extends
Media

implements
Attribute
```

Class

MediaTray

is a subclass of

Media

. Class

MediaTray

is a printing attribute class, an enumeration, that
specifies the media tray or bin for the job. This attribute can be used
instead of specifying

MediaSize

or

MediaName

.

Class

MediaTray

declares keywords for standard media kind values.
Implementation- or site-defined names for a media kind attribute may also be
created by defining a subclass of class

MediaTray

.

IPP Compatibility:

MediaTray

is a representation class for
values of the IPP "media" attribute which name paper trays.

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
MediaTray
TOP

The top input tray in the printer.

---

#### public static final
MediaTray
MIDDLE

The middle input tray in the printer.

---

#### public static final
MediaTray
BOTTOM

The bottom input tray in the printer.

---

#### public static final
MediaTray
ENVELOPE

The envelope input tray in the printer.

---

#### public static final
MediaTray
MANUAL

The manual feed input tray in the printer.

---

#### public static final
MediaTray
LARGE_CAPACITY

The large capacity input tray in the printer.

---

#### public static final
MediaTray
MAIN

The main input tray in the printer.

---

#### public static final
MediaTray
SIDE

The side input tray.

---

### Constructor Details

#### protected MediaTray​(int value)

Construct a new media tray enumeration value with the given integer
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
- the value table

---

### Additional Sections

#### Class MediaTray

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Media
- - javax.print.attribute.standard.MediaTray

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Media
- - javax.print.attribute.standard.MediaTray

javax.print.attribute.standard.Media

- javax.print.attribute.standard.MediaTray

javax.print.attribute.standard.MediaTray

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
MediaTray

extends
Media

implements
Attribute
```

Class

MediaTray

is a subclass of

Media

. Class

MediaTray

is a printing attribute class, an enumeration, that
specifies the media tray or bin for the job. This attribute can be used
instead of specifying

MediaSize

or

MediaName

.

Class

MediaTray

declares keywords for standard media kind values.
Implementation- or site-defined names for a media kind attribute may also be
created by defining a subclass of class

MediaTray

.

IPP Compatibility:

MediaTray

is a representation class for
values of the IPP "media" attribute which name paper trays.

**See Also:** Serialized Form

public class

MediaTray

extends

Media

implements

Attribute

Class

MediaTray

is a subclass of

Media

. Class

MediaTray

is a printing attribute class, an enumeration, that
specifies the media tray or bin for the job. This attribute can be used
instead of specifying

MediaSize

or

MediaName

.

Class

MediaTray

declares keywords for standard media kind values.
Implementation- or site-defined names for a media kind attribute may also be
created by defining a subclass of class

MediaTray

.

IPP Compatibility:

MediaTray

is a representation class for
values of the IPP "media" attribute which name paper trays.

Class

MediaTray

declares keywords for standard media kind values.
Implementation- or site-defined names for a media kind attribute may also be
created by defining a subclass of class

MediaTray

.

IPP Compatibility:

MediaTray

is a representation class for
values of the IPP "media" attribute which name paper trays.

IPP Compatibility:

MediaTray

is a representation class for
values of the IPP "media" attribute which name paper trays.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

MediaTray

BOTTOM

The bottom input tray in the printer.

static

MediaTray

ENVELOPE

The envelope input tray in the printer.

static

MediaTray

LARGE_CAPACITY

The large capacity input tray in the printer.

static

MediaTray

MAIN

The main input tray in the printer.

static

MediaTray

MANUAL

The manual feed input tray in the printer.

static

MediaTray

MIDDLE

The middle input tray in the printer.

static

MediaTray

SIDE

The side input tray.

static

MediaTray

TOP

The top input tray in the printer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MediaTray

​(int value)

Construct a new media tray enumeration value with the given integer
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

MediaTray

BOTTOM

The bottom input tray in the printer.

static

MediaTray

ENVELOPE

The envelope input tray in the printer.

static

MediaTray

LARGE_CAPACITY

The large capacity input tray in the printer.

static

MediaTray

MAIN

The main input tray in the printer.

static

MediaTray

MANUAL

The manual feed input tray in the printer.

static

MediaTray

MIDDLE

The middle input tray in the printer.

static

MediaTray

SIDE

The side input tray.

static

MediaTray

TOP

The top input tray in the printer.

---

#### Field Summary

The bottom input tray in the printer.

The envelope input tray in the printer.

The large capacity input tray in the printer.

The main input tray in the printer.

The manual feed input tray in the printer.

The middle input tray in the printer.

The side input tray.

The top input tray in the printer.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MediaTray

​(int value)

Construct a new media tray enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new media tray enumeration value with the given integer
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

- TOP

```java
public static final
MediaTray
TOP
```

The top input tray in the printer.

- MIDDLE

```java
public static final
MediaTray
MIDDLE
```

The middle input tray in the printer.

- BOTTOM

```java
public static final
MediaTray
BOTTOM
```

The bottom input tray in the printer.

- ENVELOPE

```java
public static final
MediaTray
ENVELOPE
```

The envelope input tray in the printer.

- MANUAL

```java
public static final
MediaTray
MANUAL
```

The manual feed input tray in the printer.

- LARGE_CAPACITY

```java
public static final
MediaTray
LARGE_CAPACITY
```

The large capacity input tray in the printer.

- MAIN

```java
public static final
MediaTray
MAIN
```

The main input tray in the printer.

- SIDE

```java
public static final
MediaTray
SIDE
```

The side input tray.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MediaTray

```java
protected MediaTray​(int value)
```

Construct a new media tray enumeration value with the given integer
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
**Returns:** the value table

Field Detail

- TOP

```java
public static final
MediaTray
TOP
```

The top input tray in the printer.

- MIDDLE

```java
public static final
MediaTray
MIDDLE
```

The middle input tray in the printer.

- BOTTOM

```java
public static final
MediaTray
BOTTOM
```

The bottom input tray in the printer.

- ENVELOPE

```java
public static final
MediaTray
ENVELOPE
```

The envelope input tray in the printer.

- MANUAL

```java
public static final
MediaTray
MANUAL
```

The manual feed input tray in the printer.

- LARGE_CAPACITY

```java
public static final
MediaTray
LARGE_CAPACITY
```

The large capacity input tray in the printer.

- MAIN

```java
public static final
MediaTray
MAIN
```

The main input tray in the printer.

- SIDE

```java
public static final
MediaTray
SIDE
```

The side input tray.

---

#### Field Detail

TOP

```java
public static final
MediaTray
TOP
```

The top input tray in the printer.

---

#### TOP

public static final

MediaTray

TOP

The top input tray in the printer.

MIDDLE

```java
public static final
MediaTray
MIDDLE
```

The middle input tray in the printer.

---

#### MIDDLE

public static final

MediaTray

MIDDLE

The middle input tray in the printer.

BOTTOM

```java
public static final
MediaTray
BOTTOM
```

The bottom input tray in the printer.

---

#### BOTTOM

public static final

MediaTray

BOTTOM

The bottom input tray in the printer.

ENVELOPE

```java
public static final
MediaTray
ENVELOPE
```

The envelope input tray in the printer.

---

#### ENVELOPE

public static final

MediaTray

ENVELOPE

The envelope input tray in the printer.

MANUAL

```java
public static final
MediaTray
MANUAL
```

The manual feed input tray in the printer.

---

#### MANUAL

public static final

MediaTray

MANUAL

The manual feed input tray in the printer.

LARGE_CAPACITY

```java
public static final
MediaTray
LARGE_CAPACITY
```

The large capacity input tray in the printer.

---

#### LARGE_CAPACITY

public static final

MediaTray

LARGE_CAPACITY

The large capacity input tray in the printer.

MAIN

```java
public static final
MediaTray
MAIN
```

The main input tray in the printer.

---

#### MAIN

public static final

MediaTray

MAIN

The main input tray in the printer.

SIDE

```java
public static final
MediaTray
SIDE
```

The side input tray.

---

#### SIDE

public static final

MediaTray

SIDE

The side input tray.

Constructor Detail

- MediaTray

```java
protected MediaTray​(int value)
```

Construct a new media tray enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

MediaTray

```java
protected MediaTray​(int value)
```

Construct a new media tray enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### MediaTray

protected MediaTray​(int value)

Construct a new media tray enumeration value with the given integer
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
**Returns:** the value table

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
**Returns:** the value table

---

#### getEnumValueTable

protected

EnumSyntax

[] getEnumValueTable()

Returns the enumeration value table for class

MediaTray

.

---

