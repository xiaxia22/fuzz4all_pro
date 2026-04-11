# Class MediaSizeName

**Source:** `java.desktop\javax\print\attribute\standard\MediaSizeName.html`

### Class Description

```java
public class
MediaSizeName

extends
Media
```

Class

MediaSizeName

is a subclass of

Media

.

This attribute can be used instead of specifying

MediaName

or

MediaTray

.

Class

MediaSizeName

currently declares a few standard media name
values.

IPP Compatibility:

MediaSizeName

is a representation class for
values of the IPP "media" attribute which names media sizes. The names of the
media sizes correspond to those in the IPP 1.1 RFC

RFC 2911

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
MediaSizeName
ISO_A0

A0 size.

---

#### public static final
MediaSizeName
ISO_A1

A1 size.

---

#### public static final
MediaSizeName
ISO_A2

A2 size.

---

#### public static final
MediaSizeName
ISO_A3

A3 size.

---

#### public static final
MediaSizeName
ISO_A4

A4 size.

---

#### public static final
MediaSizeName
ISO_A5

A5 size.

---

#### public static final
MediaSizeName
ISO_A6

A6 size.

---

#### public static final
MediaSizeName
ISO_A7

A7 size.

---

#### public static final
MediaSizeName
ISO_A8

A8 size.

---

#### public static final
MediaSizeName
ISO_A9

A9 size.

---

#### public static final
MediaSizeName
ISO_A10

A10 size.

---

#### public static final
MediaSizeName
ISO_B0

ISO B0 size.

---

#### public static final
MediaSizeName
ISO_B1

ISO B1 size.

---

#### public static final
MediaSizeName
ISO_B2

ISO B2 size.

---

#### public static final
MediaSizeName
ISO_B3

ISO B3 size.

---

#### public static final
MediaSizeName
ISO_B4

ISO B4 size.

---

#### public static final
MediaSizeName
ISO_B5

ISO B5 size.

---

#### public static final
MediaSizeName
ISO_B6

ISO B6 size.

---

#### public static final
MediaSizeName
ISO_B7

ISO B7 size.

---

#### public static final
MediaSizeName
ISO_B8

ISO B8 size.

---

#### public static final
MediaSizeName
ISO_B9

ISO B9 size.

---

#### public static final
MediaSizeName
ISO_B10

ISO B10 size.

---

#### public static final
MediaSizeName
JIS_B0

JIS B0 size.

---

#### public static final
MediaSizeName
JIS_B1

JIS B1 size.

---

#### public static final
MediaSizeName
JIS_B2

JIS B2 size.

---

#### public static final
MediaSizeName
JIS_B3

JIS B3 size.

---

#### public static final
MediaSizeName
JIS_B4

JIS B4 size.

---

#### public static final
MediaSizeName
JIS_B5

JIS B5 size.

---

#### public static final
MediaSizeName
JIS_B6

JIS B6 size.

---

#### public static final
MediaSizeName
JIS_B7

JIS B7 size.

---

#### public static final
MediaSizeName
JIS_B8

JIS B8 size.

---

#### public static final
MediaSizeName
JIS_B9

JIS B9 size.

---

#### public static final
MediaSizeName
JIS_B10

JIS B10 size.

---

#### public static final
MediaSizeName
ISO_C0

ISO C0 size.

---

#### public static final
MediaSizeName
ISO_C1

ISO C1 size.

---

#### public static final
MediaSizeName
ISO_C2

ISO C2 size.

---

#### public static final
MediaSizeName
ISO_C3

ISO C3 size.

---

#### public static final
MediaSizeName
ISO_C4

ISO C4 size.

---

#### public static final
MediaSizeName
ISO_C5

ISO C5 size.

---

#### public static final
MediaSizeName
ISO_C6

letter size.

---

#### public static final
MediaSizeName
NA_LETTER

letter size.

---

#### public static final
MediaSizeName
NA_LEGAL

legal size.

---

#### public static final
MediaSizeName
EXECUTIVE

executive size.

---

#### public static final
MediaSizeName
LEDGER

ledger size.

---

#### public static final
MediaSizeName
TABLOID

tabloid size.

---

#### public static final
MediaSizeName
INVOICE

invoice size.

---

#### public static final
MediaSizeName
FOLIO

folio size.

---

#### public static final
MediaSizeName
QUARTO

quarto size.

---

#### public static final
MediaSizeName
JAPANESE_POSTCARD

Japanese Postcard size.

---

#### public static final
MediaSizeName
JAPANESE_DOUBLE_POSTCARD

Japanese Double Postcard size.

---

#### public static final
MediaSizeName
A

A size.

---

#### public static final
MediaSizeName
B

B size.

---

#### public static final
MediaSizeName
C

C size.

---

#### public static final
MediaSizeName
D

D size.

---

#### public static final
MediaSizeName
E

E size.

---

#### public static final
MediaSizeName
ISO_DESIGNATED_LONG

ISO designated long size.

---

#### public static final
MediaSizeName
ITALY_ENVELOPE

Italy envelope size.

---

#### public static final
MediaSizeName
MONARCH_ENVELOPE

monarch envelope size.

---

#### public static final
MediaSizeName
PERSONAL_ENVELOPE

personal envelope size.

---

#### public static final
MediaSizeName
NA_NUMBER_9_ENVELOPE

number 9 envelope size.

---

#### public static final
MediaSizeName
NA_NUMBER_10_ENVELOPE

number 10 envelope size.

---

#### public static final
MediaSizeName
NA_NUMBER_11_ENVELOPE

number 11 envelope size.

---

#### public static final
MediaSizeName
NA_NUMBER_12_ENVELOPE

number 12 envelope size.

---

#### public static final
MediaSizeName
NA_NUMBER_14_ENVELOPE

number 14 envelope size.

---

#### public static final
MediaSizeName
NA_6X9_ENVELOPE

6x9 North American envelope size.

---

#### public static final
MediaSizeName
NA_7X9_ENVELOPE

7x9 North American envelope size.

---

#### public static final
MediaSizeName
NA_9X11_ENVELOPE

9x11 North American envelope size.

---

#### public static final
MediaSizeName
NA_9X12_ENVELOPE

9x12 North American envelope size.

---

#### public static final
MediaSizeName
NA_10X13_ENVELOPE

10x13 North American envelope size.

---

#### public static final
MediaSizeName
NA_10X14_ENVELOPE

10x14North American envelope size.

---

#### public static final
MediaSizeName
NA_10X15_ENVELOPE

10x15 North American envelope size.

---

#### public static final
MediaSizeName
NA_5X7

5x7 North American paper.

---

#### public static final
MediaSizeName
NA_8X10

8x10 North American paper.

---

### Constructor Details

#### protected MediaSizeName​(int value)

Construct a new media size enumeration value with the given integer
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

MediaSizeName

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

MediaSizeName

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the value table

---

### Additional Sections

#### Class MediaSizeName

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Media
- - javax.print.attribute.standard.MediaSizeName

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Media
- - javax.print.attribute.standard.MediaSizeName

javax.print.attribute.standard.Media

- javax.print.attribute.standard.MediaSizeName

javax.print.attribute.standard.MediaSizeName

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
MediaSizeName

extends
Media
```

Class

MediaSizeName

is a subclass of

Media

.

This attribute can be used instead of specifying

MediaName

or

MediaTray

.

Class

MediaSizeName

currently declares a few standard media name
values.

IPP Compatibility:

MediaSizeName

is a representation class for
values of the IPP "media" attribute which names media sizes. The names of the
media sizes correspond to those in the IPP 1.1 RFC

RFC 2911

**See Also:** Serialized Form

public class

MediaSizeName

extends

Media

Class

MediaSizeName

is a subclass of

Media

.

This attribute can be used instead of specifying

MediaName

or

MediaTray

.

Class

MediaSizeName

currently declares a few standard media name
values.

IPP Compatibility:

MediaSizeName

is a representation class for
values of the IPP "media" attribute which names media sizes. The names of the
media sizes correspond to those in the IPP 1.1 RFC

RFC 2911

This attribute can be used instead of specifying

MediaName

or

MediaTray

.

Class

MediaSizeName

currently declares a few standard media name
values.

IPP Compatibility:

MediaSizeName

is a representation class for
values of the IPP "media" attribute which names media sizes. The names of the
media sizes correspond to those in the IPP 1.1 RFC

RFC 2911

Class

MediaSizeName

currently declares a few standard media name
values.

IPP Compatibility:

MediaSizeName

is a representation class for
values of the IPP "media" attribute which names media sizes. The names of the
media sizes correspond to those in the IPP 1.1 RFC

RFC 2911

IPP Compatibility:

MediaSizeName

is a representation class for
values of the IPP "media" attribute which names media sizes. The names of the
media sizes correspond to those in the IPP 1.1 RFC

RFC 2911

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

MediaSizeName

A

A size.

static

MediaSizeName

B

B size.

static

MediaSizeName

C

C size.

static

MediaSizeName

D

D size.

static

MediaSizeName

E

E size.

static

MediaSizeName

EXECUTIVE

executive size.

static

MediaSizeName

FOLIO

folio size.

static

MediaSizeName

INVOICE

invoice size.

static

MediaSizeName

ISO_A0

A0 size.

static

MediaSizeName

ISO_A1

A1 size.

static

MediaSizeName

ISO_A10

A10 size.

static

MediaSizeName

ISO_A2

A2 size.

static

MediaSizeName

ISO_A3

A3 size.

static

MediaSizeName

ISO_A4

A4 size.

static

MediaSizeName

ISO_A5

A5 size.

static

MediaSizeName

ISO_A6

A6 size.

static

MediaSizeName

ISO_A7

A7 size.

static

MediaSizeName

ISO_A8

A8 size.

static

MediaSizeName

ISO_A9

A9 size.

static

MediaSizeName

ISO_B0

ISO B0 size.

static

MediaSizeName

ISO_B1

ISO B1 size.

static

MediaSizeName

ISO_B10

ISO B10 size.

static

MediaSizeName

ISO_B2

ISO B2 size.

static

MediaSizeName

ISO_B3

ISO B3 size.

static

MediaSizeName

ISO_B4

ISO B4 size.

static

MediaSizeName

ISO_B5

ISO B5 size.

static

MediaSizeName

ISO_B6

ISO B6 size.

static

MediaSizeName

ISO_B7

ISO B7 size.

static

MediaSizeName

ISO_B8

ISO B8 size.

static

MediaSizeName

ISO_B9

ISO B9 size.

static

MediaSizeName

ISO_C0

ISO C0 size.

static

MediaSizeName

ISO_C1

ISO C1 size.

static

MediaSizeName

ISO_C2

ISO C2 size.

static

MediaSizeName

ISO_C3

ISO C3 size.

static

MediaSizeName

ISO_C4

ISO C4 size.

static

MediaSizeName

ISO_C5

ISO C5 size.

static

MediaSizeName

ISO_C6

letter size.

static

MediaSizeName

ISO_DESIGNATED_LONG

ISO designated long size.

static

MediaSizeName

ITALY_ENVELOPE

Italy envelope size.

static

MediaSizeName

JAPANESE_DOUBLE_POSTCARD

Japanese Double Postcard size.

static

MediaSizeName

JAPANESE_POSTCARD

Japanese Postcard size.

static

MediaSizeName

JIS_B0

JIS B0 size.

static

MediaSizeName

JIS_B1

JIS B1 size.

static

MediaSizeName

JIS_B10

JIS B10 size.

static

MediaSizeName

JIS_B2

JIS B2 size.

static

MediaSizeName

JIS_B3

JIS B3 size.

static

MediaSizeName

JIS_B4

JIS B4 size.

static

MediaSizeName

JIS_B5

JIS B5 size.

static

MediaSizeName

JIS_B6

JIS B6 size.

static

MediaSizeName

JIS_B7

JIS B7 size.

static

MediaSizeName

JIS_B8

JIS B8 size.

static

MediaSizeName

JIS_B9

JIS B9 size.

static

MediaSizeName

LEDGER

ledger size.

static

MediaSizeName

MONARCH_ENVELOPE

monarch envelope size.

static

MediaSizeName

NA_10X13_ENVELOPE

10x13 North American envelope size.

static

MediaSizeName

NA_10X14_ENVELOPE

10x14North American envelope size.

static

MediaSizeName

NA_10X15_ENVELOPE

10x15 North American envelope size.

static

MediaSizeName

NA_5X7

5x7 North American paper.

static

MediaSizeName

NA_6X9_ENVELOPE

6x9 North American envelope size.

static

MediaSizeName

NA_7X9_ENVELOPE

7x9 North American envelope size.

static

MediaSizeName

NA_8X10

8x10 North American paper.

static

MediaSizeName

NA_9X11_ENVELOPE

9x11 North American envelope size.

static

MediaSizeName

NA_9X12_ENVELOPE

9x12 North American envelope size.

static

MediaSizeName

NA_LEGAL

legal size.

static

MediaSizeName

NA_LETTER

letter size.

static

MediaSizeName

NA_NUMBER_10_ENVELOPE

number 10 envelope size.

static

MediaSizeName

NA_NUMBER_11_ENVELOPE

number 11 envelope size.

static

MediaSizeName

NA_NUMBER_12_ENVELOPE

number 12 envelope size.

static

MediaSizeName

NA_NUMBER_14_ENVELOPE

number 14 envelope size.

static

MediaSizeName

NA_NUMBER_9_ENVELOPE

number 9 envelope size.

static

MediaSizeName

PERSONAL_ENVELOPE

personal envelope size.

static

MediaSizeName

QUARTO

quarto size.

static

MediaSizeName

TABLOID

tabloid size.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MediaSizeName

​(int value)

Construct a new media size enumeration value with the given integer
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

MediaSizeName

.

protected

String

[]

getStringTable

()

Returns the string table for class

MediaSizeName

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

Field Summary

Fields

Modifier and Type

Field

Description

static

MediaSizeName

A

A size.

static

MediaSizeName

B

B size.

static

MediaSizeName

C

C size.

static

MediaSizeName

D

D size.

static

MediaSizeName

E

E size.

static

MediaSizeName

EXECUTIVE

executive size.

static

MediaSizeName

FOLIO

folio size.

static

MediaSizeName

INVOICE

invoice size.

static

MediaSizeName

ISO_A0

A0 size.

static

MediaSizeName

ISO_A1

A1 size.

static

MediaSizeName

ISO_A10

A10 size.

static

MediaSizeName

ISO_A2

A2 size.

static

MediaSizeName

ISO_A3

A3 size.

static

MediaSizeName

ISO_A4

A4 size.

static

MediaSizeName

ISO_A5

A5 size.

static

MediaSizeName

ISO_A6

A6 size.

static

MediaSizeName

ISO_A7

A7 size.

static

MediaSizeName

ISO_A8

A8 size.

static

MediaSizeName

ISO_A9

A9 size.

static

MediaSizeName

ISO_B0

ISO B0 size.

static

MediaSizeName

ISO_B1

ISO B1 size.

static

MediaSizeName

ISO_B10

ISO B10 size.

static

MediaSizeName

ISO_B2

ISO B2 size.

static

MediaSizeName

ISO_B3

ISO B3 size.

static

MediaSizeName

ISO_B4

ISO B4 size.

static

MediaSizeName

ISO_B5

ISO B5 size.

static

MediaSizeName

ISO_B6

ISO B6 size.

static

MediaSizeName

ISO_B7

ISO B7 size.

static

MediaSizeName

ISO_B8

ISO B8 size.

static

MediaSizeName

ISO_B9

ISO B9 size.

static

MediaSizeName

ISO_C0

ISO C0 size.

static

MediaSizeName

ISO_C1

ISO C1 size.

static

MediaSizeName

ISO_C2

ISO C2 size.

static

MediaSizeName

ISO_C3

ISO C3 size.

static

MediaSizeName

ISO_C4

ISO C4 size.

static

MediaSizeName

ISO_C5

ISO C5 size.

static

MediaSizeName

ISO_C6

letter size.

static

MediaSizeName

ISO_DESIGNATED_LONG

ISO designated long size.

static

MediaSizeName

ITALY_ENVELOPE

Italy envelope size.

static

MediaSizeName

JAPANESE_DOUBLE_POSTCARD

Japanese Double Postcard size.

static

MediaSizeName

JAPANESE_POSTCARD

Japanese Postcard size.

static

MediaSizeName

JIS_B0

JIS B0 size.

static

MediaSizeName

JIS_B1

JIS B1 size.

static

MediaSizeName

JIS_B10

JIS B10 size.

static

MediaSizeName

JIS_B2

JIS B2 size.

static

MediaSizeName

JIS_B3

JIS B3 size.

static

MediaSizeName

JIS_B4

JIS B4 size.

static

MediaSizeName

JIS_B5

JIS B5 size.

static

MediaSizeName

JIS_B6

JIS B6 size.

static

MediaSizeName

JIS_B7

JIS B7 size.

static

MediaSizeName

JIS_B8

JIS B8 size.

static

MediaSizeName

JIS_B9

JIS B9 size.

static

MediaSizeName

LEDGER

ledger size.

static

MediaSizeName

MONARCH_ENVELOPE

monarch envelope size.

static

MediaSizeName

NA_10X13_ENVELOPE

10x13 North American envelope size.

static

MediaSizeName

NA_10X14_ENVELOPE

10x14North American envelope size.

static

MediaSizeName

NA_10X15_ENVELOPE

10x15 North American envelope size.

static

MediaSizeName

NA_5X7

5x7 North American paper.

static

MediaSizeName

NA_6X9_ENVELOPE

6x9 North American envelope size.

static

MediaSizeName

NA_7X9_ENVELOPE

7x9 North American envelope size.

static

MediaSizeName

NA_8X10

8x10 North American paper.

static

MediaSizeName

NA_9X11_ENVELOPE

9x11 North American envelope size.

static

MediaSizeName

NA_9X12_ENVELOPE

9x12 North American envelope size.

static

MediaSizeName

NA_LEGAL

legal size.

static

MediaSizeName

NA_LETTER

letter size.

static

MediaSizeName

NA_NUMBER_10_ENVELOPE

number 10 envelope size.

static

MediaSizeName

NA_NUMBER_11_ENVELOPE

number 11 envelope size.

static

MediaSizeName

NA_NUMBER_12_ENVELOPE

number 12 envelope size.

static

MediaSizeName

NA_NUMBER_14_ENVELOPE

number 14 envelope size.

static

MediaSizeName

NA_NUMBER_9_ENVELOPE

number 9 envelope size.

static

MediaSizeName

PERSONAL_ENVELOPE

personal envelope size.

static

MediaSizeName

QUARTO

quarto size.

static

MediaSizeName

TABLOID

tabloid size.

---

#### Field Summary

A size.

B size.

C size.

D size.

E size.

executive size.

folio size.

invoice size.

A0 size.

A1 size.

A10 size.

A2 size.

A3 size.

A4 size.

A5 size.

A6 size.

A7 size.

A8 size.

A9 size.

ISO B0 size.

ISO B1 size.

ISO B10 size.

ISO B2 size.

ISO B3 size.

ISO B4 size.

ISO B5 size.

ISO B6 size.

ISO B7 size.

ISO B8 size.

ISO B9 size.

ISO C0 size.

ISO C1 size.

ISO C2 size.

ISO C3 size.

ISO C4 size.

ISO C5 size.

letter size.

ISO designated long size.

Italy envelope size.

Japanese Double Postcard size.

Japanese Postcard size.

JIS B0 size.

JIS B1 size.

JIS B10 size.

JIS B2 size.

JIS B3 size.

JIS B4 size.

JIS B5 size.

JIS B6 size.

JIS B7 size.

JIS B8 size.

JIS B9 size.

ledger size.

monarch envelope size.

10x13 North American envelope size.

10x14North American envelope size.

10x15 North American envelope size.

5x7 North American paper.

6x9 North American envelope size.

7x9 North American envelope size.

8x10 North American paper.

9x11 North American envelope size.

9x12 North American envelope size.

legal size.

number 10 envelope size.

number 11 envelope size.

number 12 envelope size.

number 14 envelope size.

number 9 envelope size.

personal envelope size.

quarto size.

tabloid size.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MediaSizeName

​(int value)

Construct a new media size enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new media size enumeration value with the given integer
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

MediaSizeName

.

protected

String

[]

getStringTable

()

Returns the string table for class

MediaSizeName

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

---

#### Method Summary

Returns the enumeration value table for class

MediaSizeName

.

Returns the string table for class

MediaSizeName

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

============ FIELD DETAIL ===========

- Field Detail

- ISO_A0

```java
public static final
MediaSizeName
ISO_A0
```

A0 size.

- ISO_A1

```java
public static final
MediaSizeName
ISO_A1
```

A1 size.

- ISO_A2

```java
public static final
MediaSizeName
ISO_A2
```

A2 size.

- ISO_A3

```java
public static final
MediaSizeName
ISO_A3
```

A3 size.

- ISO_A4

```java
public static final
MediaSizeName
ISO_A4
```

A4 size.

- ISO_A5

```java
public static final
MediaSizeName
ISO_A5
```

A5 size.

- ISO_A6

```java
public static final
MediaSizeName
ISO_A6
```

A6 size.

- ISO_A7

```java
public static final
MediaSizeName
ISO_A7
```

A7 size.

- ISO_A8

```java
public static final
MediaSizeName
ISO_A8
```

A8 size.

- ISO_A9

```java
public static final
MediaSizeName
ISO_A9
```

A9 size.

- ISO_A10

```java
public static final
MediaSizeName
ISO_A10
```

A10 size.

- ISO_B0

```java
public static final
MediaSizeName
ISO_B0
```

ISO B0 size.

- ISO_B1

```java
public static final
MediaSizeName
ISO_B1
```

ISO B1 size.

- ISO_B2

```java
public static final
MediaSizeName
ISO_B2
```

ISO B2 size.

- ISO_B3

```java
public static final
MediaSizeName
ISO_B3
```

ISO B3 size.

- ISO_B4

```java
public static final
MediaSizeName
ISO_B4
```

ISO B4 size.

- ISO_B5

```java
public static final
MediaSizeName
ISO_B5
```

ISO B5 size.

- ISO_B6

```java
public static final
MediaSizeName
ISO_B6
```

ISO B6 size.

- ISO_B7

```java
public static final
MediaSizeName
ISO_B7
```

ISO B7 size.

- ISO_B8

```java
public static final
MediaSizeName
ISO_B8
```

ISO B8 size.

- ISO_B9

```java
public static final
MediaSizeName
ISO_B9
```

ISO B9 size.

- ISO_B10

```java
public static final
MediaSizeName
ISO_B10
```

ISO B10 size.

- JIS_B0

```java
public static final
MediaSizeName
JIS_B0
```

JIS B0 size.

- JIS_B1

```java
public static final
MediaSizeName
JIS_B1
```

JIS B1 size.

- JIS_B2

```java
public static final
MediaSizeName
JIS_B2
```

JIS B2 size.

- JIS_B3

```java
public static final
MediaSizeName
JIS_B3
```

JIS B3 size.

- JIS_B4

```java
public static final
MediaSizeName
JIS_B4
```

JIS B4 size.

- JIS_B5

```java
public static final
MediaSizeName
JIS_B5
```

JIS B5 size.

- JIS_B6

```java
public static final
MediaSizeName
JIS_B6
```

JIS B6 size.

- JIS_B7

```java
public static final
MediaSizeName
JIS_B7
```

JIS B7 size.

- JIS_B8

```java
public static final
MediaSizeName
JIS_B8
```

JIS B8 size.

- JIS_B9

```java
public static final
MediaSizeName
JIS_B9
```

JIS B9 size.

- JIS_B10

```java
public static final
MediaSizeName
JIS_B10
```

JIS B10 size.

- ISO_C0

```java
public static final
MediaSizeName
ISO_C0
```

ISO C0 size.

- ISO_C1

```java
public static final
MediaSizeName
ISO_C1
```

ISO C1 size.

- ISO_C2

```java
public static final
MediaSizeName
ISO_C2
```

ISO C2 size.

- ISO_C3

```java
public static final
MediaSizeName
ISO_C3
```

ISO C3 size.

- ISO_C4

```java
public static final
MediaSizeName
ISO_C4
```

ISO C4 size.

- ISO_C5

```java
public static final
MediaSizeName
ISO_C5
```

ISO C5 size.

- ISO_C6

```java
public static final
MediaSizeName
ISO_C6
```

letter size.

- NA_LETTER

```java
public static final
MediaSizeName
NA_LETTER
```

letter size.

- NA_LEGAL

```java
public static final
MediaSizeName
NA_LEGAL
```

legal size.

- EXECUTIVE

```java
public static final
MediaSizeName
EXECUTIVE
```

executive size.

- LEDGER

```java
public static final
MediaSizeName
LEDGER
```

ledger size.

- TABLOID

```java
public static final
MediaSizeName
TABLOID
```

tabloid size.

- INVOICE

```java
public static final
MediaSizeName
INVOICE
```

invoice size.

- FOLIO

```java
public static final
MediaSizeName
FOLIO
```

folio size.

- QUARTO

```java
public static final
MediaSizeName
QUARTO
```

quarto size.

- JAPANESE_POSTCARD

```java
public static final
MediaSizeName
JAPANESE_POSTCARD
```

Japanese Postcard size.

- JAPANESE_DOUBLE_POSTCARD

```java
public static final
MediaSizeName
JAPANESE_DOUBLE_POSTCARD
```

Japanese Double Postcard size.

- A

```java
public static final
MediaSizeName
A
```

A size.

- B

```java
public static final
MediaSizeName
B
```

B size.

- C

```java
public static final
MediaSizeName
C
```

C size.

- D

```java
public static final
MediaSizeName
D
```

D size.

- E

```java
public static final
MediaSizeName
E
```

E size.

- ISO_DESIGNATED_LONG

```java
public static final
MediaSizeName
ISO_DESIGNATED_LONG
```

ISO designated long size.

- ITALY_ENVELOPE

```java
public static final
MediaSizeName
ITALY_ENVELOPE
```

Italy envelope size.

- MONARCH_ENVELOPE

```java
public static final
MediaSizeName
MONARCH_ENVELOPE
```

monarch envelope size.

- PERSONAL_ENVELOPE

```java
public static final
MediaSizeName
PERSONAL_ENVELOPE
```

personal envelope size.

- NA_NUMBER_9_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_9_ENVELOPE
```

number 9 envelope size.

- NA_NUMBER_10_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_10_ENVELOPE
```

number 10 envelope size.

- NA_NUMBER_11_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_11_ENVELOPE
```

number 11 envelope size.

- NA_NUMBER_12_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_12_ENVELOPE
```

number 12 envelope size.

- NA_NUMBER_14_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_14_ENVELOPE
```

number 14 envelope size.

- NA_6X9_ENVELOPE

```java
public static final
MediaSizeName
NA_6X9_ENVELOPE
```

6x9 North American envelope size.

- NA_7X9_ENVELOPE

```java
public static final
MediaSizeName
NA_7X9_ENVELOPE
```

7x9 North American envelope size.

- NA_9X11_ENVELOPE

```java
public static final
MediaSizeName
NA_9X11_ENVELOPE
```

9x11 North American envelope size.

- NA_9X12_ENVELOPE

```java
public static final
MediaSizeName
NA_9X12_ENVELOPE
```

9x12 North American envelope size.

- NA_10X13_ENVELOPE

```java
public static final
MediaSizeName
NA_10X13_ENVELOPE
```

10x13 North American envelope size.

- NA_10X14_ENVELOPE

```java
public static final
MediaSizeName
NA_10X14_ENVELOPE
```

10x14North American envelope size.

- NA_10X15_ENVELOPE

```java
public static final
MediaSizeName
NA_10X15_ENVELOPE
```

10x15 North American envelope size.

- NA_5X7

```java
public static final
MediaSizeName
NA_5X7
```

5x7 North American paper.

- NA_8X10

```java
public static final
MediaSizeName
NA_8X10
```

8x10 North American paper.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MediaSizeName

```java
protected MediaSizeName​(int value)
```

Construct a new media size enumeration value with the given integer
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

MediaSizeName

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

MediaSizeName

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

Field Detail

- ISO_A0

```java
public static final
MediaSizeName
ISO_A0
```

A0 size.

- ISO_A1

```java
public static final
MediaSizeName
ISO_A1
```

A1 size.

- ISO_A2

```java
public static final
MediaSizeName
ISO_A2
```

A2 size.

- ISO_A3

```java
public static final
MediaSizeName
ISO_A3
```

A3 size.

- ISO_A4

```java
public static final
MediaSizeName
ISO_A4
```

A4 size.

- ISO_A5

```java
public static final
MediaSizeName
ISO_A5
```

A5 size.

- ISO_A6

```java
public static final
MediaSizeName
ISO_A6
```

A6 size.

- ISO_A7

```java
public static final
MediaSizeName
ISO_A7
```

A7 size.

- ISO_A8

```java
public static final
MediaSizeName
ISO_A8
```

A8 size.

- ISO_A9

```java
public static final
MediaSizeName
ISO_A9
```

A9 size.

- ISO_A10

```java
public static final
MediaSizeName
ISO_A10
```

A10 size.

- ISO_B0

```java
public static final
MediaSizeName
ISO_B0
```

ISO B0 size.

- ISO_B1

```java
public static final
MediaSizeName
ISO_B1
```

ISO B1 size.

- ISO_B2

```java
public static final
MediaSizeName
ISO_B2
```

ISO B2 size.

- ISO_B3

```java
public static final
MediaSizeName
ISO_B3
```

ISO B3 size.

- ISO_B4

```java
public static final
MediaSizeName
ISO_B4
```

ISO B4 size.

- ISO_B5

```java
public static final
MediaSizeName
ISO_B5
```

ISO B5 size.

- ISO_B6

```java
public static final
MediaSizeName
ISO_B6
```

ISO B6 size.

- ISO_B7

```java
public static final
MediaSizeName
ISO_B7
```

ISO B7 size.

- ISO_B8

```java
public static final
MediaSizeName
ISO_B8
```

ISO B8 size.

- ISO_B9

```java
public static final
MediaSizeName
ISO_B9
```

ISO B9 size.

- ISO_B10

```java
public static final
MediaSizeName
ISO_B10
```

ISO B10 size.

- JIS_B0

```java
public static final
MediaSizeName
JIS_B0
```

JIS B0 size.

- JIS_B1

```java
public static final
MediaSizeName
JIS_B1
```

JIS B1 size.

- JIS_B2

```java
public static final
MediaSizeName
JIS_B2
```

JIS B2 size.

- JIS_B3

```java
public static final
MediaSizeName
JIS_B3
```

JIS B3 size.

- JIS_B4

```java
public static final
MediaSizeName
JIS_B4
```

JIS B4 size.

- JIS_B5

```java
public static final
MediaSizeName
JIS_B5
```

JIS B5 size.

- JIS_B6

```java
public static final
MediaSizeName
JIS_B6
```

JIS B6 size.

- JIS_B7

```java
public static final
MediaSizeName
JIS_B7
```

JIS B7 size.

- JIS_B8

```java
public static final
MediaSizeName
JIS_B8
```

JIS B8 size.

- JIS_B9

```java
public static final
MediaSizeName
JIS_B9
```

JIS B9 size.

- JIS_B10

```java
public static final
MediaSizeName
JIS_B10
```

JIS B10 size.

- ISO_C0

```java
public static final
MediaSizeName
ISO_C0
```

ISO C0 size.

- ISO_C1

```java
public static final
MediaSizeName
ISO_C1
```

ISO C1 size.

- ISO_C2

```java
public static final
MediaSizeName
ISO_C2
```

ISO C2 size.

- ISO_C3

```java
public static final
MediaSizeName
ISO_C3
```

ISO C3 size.

- ISO_C4

```java
public static final
MediaSizeName
ISO_C4
```

ISO C4 size.

- ISO_C5

```java
public static final
MediaSizeName
ISO_C5
```

ISO C5 size.

- ISO_C6

```java
public static final
MediaSizeName
ISO_C6
```

letter size.

- NA_LETTER

```java
public static final
MediaSizeName
NA_LETTER
```

letter size.

- NA_LEGAL

```java
public static final
MediaSizeName
NA_LEGAL
```

legal size.

- EXECUTIVE

```java
public static final
MediaSizeName
EXECUTIVE
```

executive size.

- LEDGER

```java
public static final
MediaSizeName
LEDGER
```

ledger size.

- TABLOID

```java
public static final
MediaSizeName
TABLOID
```

tabloid size.

- INVOICE

```java
public static final
MediaSizeName
INVOICE
```

invoice size.

- FOLIO

```java
public static final
MediaSizeName
FOLIO
```

folio size.

- QUARTO

```java
public static final
MediaSizeName
QUARTO
```

quarto size.

- JAPANESE_POSTCARD

```java
public static final
MediaSizeName
JAPANESE_POSTCARD
```

Japanese Postcard size.

- JAPANESE_DOUBLE_POSTCARD

```java
public static final
MediaSizeName
JAPANESE_DOUBLE_POSTCARD
```

Japanese Double Postcard size.

- A

```java
public static final
MediaSizeName
A
```

A size.

- B

```java
public static final
MediaSizeName
B
```

B size.

- C

```java
public static final
MediaSizeName
C
```

C size.

- D

```java
public static final
MediaSizeName
D
```

D size.

- E

```java
public static final
MediaSizeName
E
```

E size.

- ISO_DESIGNATED_LONG

```java
public static final
MediaSizeName
ISO_DESIGNATED_LONG
```

ISO designated long size.

- ITALY_ENVELOPE

```java
public static final
MediaSizeName
ITALY_ENVELOPE
```

Italy envelope size.

- MONARCH_ENVELOPE

```java
public static final
MediaSizeName
MONARCH_ENVELOPE
```

monarch envelope size.

- PERSONAL_ENVELOPE

```java
public static final
MediaSizeName
PERSONAL_ENVELOPE
```

personal envelope size.

- NA_NUMBER_9_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_9_ENVELOPE
```

number 9 envelope size.

- NA_NUMBER_10_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_10_ENVELOPE
```

number 10 envelope size.

- NA_NUMBER_11_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_11_ENVELOPE
```

number 11 envelope size.

- NA_NUMBER_12_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_12_ENVELOPE
```

number 12 envelope size.

- NA_NUMBER_14_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_14_ENVELOPE
```

number 14 envelope size.

- NA_6X9_ENVELOPE

```java
public static final
MediaSizeName
NA_6X9_ENVELOPE
```

6x9 North American envelope size.

- NA_7X9_ENVELOPE

```java
public static final
MediaSizeName
NA_7X9_ENVELOPE
```

7x9 North American envelope size.

- NA_9X11_ENVELOPE

```java
public static final
MediaSizeName
NA_9X11_ENVELOPE
```

9x11 North American envelope size.

- NA_9X12_ENVELOPE

```java
public static final
MediaSizeName
NA_9X12_ENVELOPE
```

9x12 North American envelope size.

- NA_10X13_ENVELOPE

```java
public static final
MediaSizeName
NA_10X13_ENVELOPE
```

10x13 North American envelope size.

- NA_10X14_ENVELOPE

```java
public static final
MediaSizeName
NA_10X14_ENVELOPE
```

10x14North American envelope size.

- NA_10X15_ENVELOPE

```java
public static final
MediaSizeName
NA_10X15_ENVELOPE
```

10x15 North American envelope size.

- NA_5X7

```java
public static final
MediaSizeName
NA_5X7
```

5x7 North American paper.

- NA_8X10

```java
public static final
MediaSizeName
NA_8X10
```

8x10 North American paper.

---

#### Field Detail

ISO_A0

```java
public static final
MediaSizeName
ISO_A0
```

A0 size.

---

#### ISO_A0

public static final

MediaSizeName

ISO_A0

A0 size.

ISO_A1

```java
public static final
MediaSizeName
ISO_A1
```

A1 size.

---

#### ISO_A1

public static final

MediaSizeName

ISO_A1

A1 size.

ISO_A2

```java
public static final
MediaSizeName
ISO_A2
```

A2 size.

---

#### ISO_A2

public static final

MediaSizeName

ISO_A2

A2 size.

ISO_A3

```java
public static final
MediaSizeName
ISO_A3
```

A3 size.

---

#### ISO_A3

public static final

MediaSizeName

ISO_A3

A3 size.

ISO_A4

```java
public static final
MediaSizeName
ISO_A4
```

A4 size.

---

#### ISO_A4

public static final

MediaSizeName

ISO_A4

A4 size.

ISO_A5

```java
public static final
MediaSizeName
ISO_A5
```

A5 size.

---

#### ISO_A5

public static final

MediaSizeName

ISO_A5

A5 size.

ISO_A6

```java
public static final
MediaSizeName
ISO_A6
```

A6 size.

---

#### ISO_A6

public static final

MediaSizeName

ISO_A6

A6 size.

ISO_A7

```java
public static final
MediaSizeName
ISO_A7
```

A7 size.

---

#### ISO_A7

public static final

MediaSizeName

ISO_A7

A7 size.

ISO_A8

```java
public static final
MediaSizeName
ISO_A8
```

A8 size.

---

#### ISO_A8

public static final

MediaSizeName

ISO_A8

A8 size.

ISO_A9

```java
public static final
MediaSizeName
ISO_A9
```

A9 size.

---

#### ISO_A9

public static final

MediaSizeName

ISO_A9

A9 size.

ISO_A10

```java
public static final
MediaSizeName
ISO_A10
```

A10 size.

---

#### ISO_A10

public static final

MediaSizeName

ISO_A10

A10 size.

ISO_B0

```java
public static final
MediaSizeName
ISO_B0
```

ISO B0 size.

---

#### ISO_B0

public static final

MediaSizeName

ISO_B0

ISO B0 size.

ISO_B1

```java
public static final
MediaSizeName
ISO_B1
```

ISO B1 size.

---

#### ISO_B1

public static final

MediaSizeName

ISO_B1

ISO B1 size.

ISO_B2

```java
public static final
MediaSizeName
ISO_B2
```

ISO B2 size.

---

#### ISO_B2

public static final

MediaSizeName

ISO_B2

ISO B2 size.

ISO_B3

```java
public static final
MediaSizeName
ISO_B3
```

ISO B3 size.

---

#### ISO_B3

public static final

MediaSizeName

ISO_B3

ISO B3 size.

ISO_B4

```java
public static final
MediaSizeName
ISO_B4
```

ISO B4 size.

---

#### ISO_B4

public static final

MediaSizeName

ISO_B4

ISO B4 size.

ISO_B5

```java
public static final
MediaSizeName
ISO_B5
```

ISO B5 size.

---

#### ISO_B5

public static final

MediaSizeName

ISO_B5

ISO B5 size.

ISO_B6

```java
public static final
MediaSizeName
ISO_B6
```

ISO B6 size.

---

#### ISO_B6

public static final

MediaSizeName

ISO_B6

ISO B6 size.

ISO_B7

```java
public static final
MediaSizeName
ISO_B7
```

ISO B7 size.

---

#### ISO_B7

public static final

MediaSizeName

ISO_B7

ISO B7 size.

ISO_B8

```java
public static final
MediaSizeName
ISO_B8
```

ISO B8 size.

---

#### ISO_B8

public static final

MediaSizeName

ISO_B8

ISO B8 size.

ISO_B9

```java
public static final
MediaSizeName
ISO_B9
```

ISO B9 size.

---

#### ISO_B9

public static final

MediaSizeName

ISO_B9

ISO B9 size.

ISO_B10

```java
public static final
MediaSizeName
ISO_B10
```

ISO B10 size.

---

#### ISO_B10

public static final

MediaSizeName

ISO_B10

ISO B10 size.

JIS_B0

```java
public static final
MediaSizeName
JIS_B0
```

JIS B0 size.

---

#### JIS_B0

public static final

MediaSizeName

JIS_B0

JIS B0 size.

JIS_B1

```java
public static final
MediaSizeName
JIS_B1
```

JIS B1 size.

---

#### JIS_B1

public static final

MediaSizeName

JIS_B1

JIS B1 size.

JIS_B2

```java
public static final
MediaSizeName
JIS_B2
```

JIS B2 size.

---

#### JIS_B2

public static final

MediaSizeName

JIS_B2

JIS B2 size.

JIS_B3

```java
public static final
MediaSizeName
JIS_B3
```

JIS B3 size.

---

#### JIS_B3

public static final

MediaSizeName

JIS_B3

JIS B3 size.

JIS_B4

```java
public static final
MediaSizeName
JIS_B4
```

JIS B4 size.

---

#### JIS_B4

public static final

MediaSizeName

JIS_B4

JIS B4 size.

JIS_B5

```java
public static final
MediaSizeName
JIS_B5
```

JIS B5 size.

---

#### JIS_B5

public static final

MediaSizeName

JIS_B5

JIS B5 size.

JIS_B6

```java
public static final
MediaSizeName
JIS_B6
```

JIS B6 size.

---

#### JIS_B6

public static final

MediaSizeName

JIS_B6

JIS B6 size.

JIS_B7

```java
public static final
MediaSizeName
JIS_B7
```

JIS B7 size.

---

#### JIS_B7

public static final

MediaSizeName

JIS_B7

JIS B7 size.

JIS_B8

```java
public static final
MediaSizeName
JIS_B8
```

JIS B8 size.

---

#### JIS_B8

public static final

MediaSizeName

JIS_B8

JIS B8 size.

JIS_B9

```java
public static final
MediaSizeName
JIS_B9
```

JIS B9 size.

---

#### JIS_B9

public static final

MediaSizeName

JIS_B9

JIS B9 size.

JIS_B10

```java
public static final
MediaSizeName
JIS_B10
```

JIS B10 size.

---

#### JIS_B10

public static final

MediaSizeName

JIS_B10

JIS B10 size.

ISO_C0

```java
public static final
MediaSizeName
ISO_C0
```

ISO C0 size.

---

#### ISO_C0

public static final

MediaSizeName

ISO_C0

ISO C0 size.

ISO_C1

```java
public static final
MediaSizeName
ISO_C1
```

ISO C1 size.

---

#### ISO_C1

public static final

MediaSizeName

ISO_C1

ISO C1 size.

ISO_C2

```java
public static final
MediaSizeName
ISO_C2
```

ISO C2 size.

---

#### ISO_C2

public static final

MediaSizeName

ISO_C2

ISO C2 size.

ISO_C3

```java
public static final
MediaSizeName
ISO_C3
```

ISO C3 size.

---

#### ISO_C3

public static final

MediaSizeName

ISO_C3

ISO C3 size.

ISO_C4

```java
public static final
MediaSizeName
ISO_C4
```

ISO C4 size.

---

#### ISO_C4

public static final

MediaSizeName

ISO_C4

ISO C4 size.

ISO_C5

```java
public static final
MediaSizeName
ISO_C5
```

ISO C5 size.

---

#### ISO_C5

public static final

MediaSizeName

ISO_C5

ISO C5 size.

ISO_C6

```java
public static final
MediaSizeName
ISO_C6
```

letter size.

---

#### ISO_C6

public static final

MediaSizeName

ISO_C6

letter size.

NA_LETTER

```java
public static final
MediaSizeName
NA_LETTER
```

letter size.

---

#### NA_LETTER

public static final

MediaSizeName

NA_LETTER

letter size.

NA_LEGAL

```java
public static final
MediaSizeName
NA_LEGAL
```

legal size.

---

#### NA_LEGAL

public static final

MediaSizeName

NA_LEGAL

legal size.

EXECUTIVE

```java
public static final
MediaSizeName
EXECUTIVE
```

executive size.

---

#### EXECUTIVE

public static final

MediaSizeName

EXECUTIVE

executive size.

LEDGER

```java
public static final
MediaSizeName
LEDGER
```

ledger size.

---

#### LEDGER

public static final

MediaSizeName

LEDGER

ledger size.

TABLOID

```java
public static final
MediaSizeName
TABLOID
```

tabloid size.

---

#### TABLOID

public static final

MediaSizeName

TABLOID

tabloid size.

INVOICE

```java
public static final
MediaSizeName
INVOICE
```

invoice size.

---

#### INVOICE

public static final

MediaSizeName

INVOICE

invoice size.

FOLIO

```java
public static final
MediaSizeName
FOLIO
```

folio size.

---

#### FOLIO

public static final

MediaSizeName

FOLIO

folio size.

QUARTO

```java
public static final
MediaSizeName
QUARTO
```

quarto size.

---

#### QUARTO

public static final

MediaSizeName

QUARTO

quarto size.

JAPANESE_POSTCARD

```java
public static final
MediaSizeName
JAPANESE_POSTCARD
```

Japanese Postcard size.

---

#### JAPANESE_POSTCARD

public static final

MediaSizeName

JAPANESE_POSTCARD

Japanese Postcard size.

JAPANESE_DOUBLE_POSTCARD

```java
public static final
MediaSizeName
JAPANESE_DOUBLE_POSTCARD
```

Japanese Double Postcard size.

---

#### JAPANESE_DOUBLE_POSTCARD

public static final

MediaSizeName

JAPANESE_DOUBLE_POSTCARD

Japanese Double Postcard size.

A

```java
public static final
MediaSizeName
A
```

A size.

---

#### A

public static final

MediaSizeName

A

A size.

B

```java
public static final
MediaSizeName
B
```

B size.

---

#### B

public static final

MediaSizeName

B

B size.

C

```java
public static final
MediaSizeName
C
```

C size.

---

#### C

public static final

MediaSizeName

C

C size.

D

```java
public static final
MediaSizeName
D
```

D size.

---

#### D

public static final

MediaSizeName

D

D size.

E

```java
public static final
MediaSizeName
E
```

E size.

---

#### E

public static final

MediaSizeName

E

E size.

ISO_DESIGNATED_LONG

```java
public static final
MediaSizeName
ISO_DESIGNATED_LONG
```

ISO designated long size.

---

#### ISO_DESIGNATED_LONG

public static final

MediaSizeName

ISO_DESIGNATED_LONG

ISO designated long size.

ITALY_ENVELOPE

```java
public static final
MediaSizeName
ITALY_ENVELOPE
```

Italy envelope size.

---

#### ITALY_ENVELOPE

public static final

MediaSizeName

ITALY_ENVELOPE

Italy envelope size.

MONARCH_ENVELOPE

```java
public static final
MediaSizeName
MONARCH_ENVELOPE
```

monarch envelope size.

---

#### MONARCH_ENVELOPE

public static final

MediaSizeName

MONARCH_ENVELOPE

monarch envelope size.

PERSONAL_ENVELOPE

```java
public static final
MediaSizeName
PERSONAL_ENVELOPE
```

personal envelope size.

---

#### PERSONAL_ENVELOPE

public static final

MediaSizeName

PERSONAL_ENVELOPE

personal envelope size.

NA_NUMBER_9_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_9_ENVELOPE
```

number 9 envelope size.

---

#### NA_NUMBER_9_ENVELOPE

public static final

MediaSizeName

NA_NUMBER_9_ENVELOPE

number 9 envelope size.

NA_NUMBER_10_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_10_ENVELOPE
```

number 10 envelope size.

---

#### NA_NUMBER_10_ENVELOPE

public static final

MediaSizeName

NA_NUMBER_10_ENVELOPE

number 10 envelope size.

NA_NUMBER_11_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_11_ENVELOPE
```

number 11 envelope size.

---

#### NA_NUMBER_11_ENVELOPE

public static final

MediaSizeName

NA_NUMBER_11_ENVELOPE

number 11 envelope size.

NA_NUMBER_12_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_12_ENVELOPE
```

number 12 envelope size.

---

#### NA_NUMBER_12_ENVELOPE

public static final

MediaSizeName

NA_NUMBER_12_ENVELOPE

number 12 envelope size.

NA_NUMBER_14_ENVELOPE

```java
public static final
MediaSizeName
NA_NUMBER_14_ENVELOPE
```

number 14 envelope size.

---

#### NA_NUMBER_14_ENVELOPE

public static final

MediaSizeName

NA_NUMBER_14_ENVELOPE

number 14 envelope size.

NA_6X9_ENVELOPE

```java
public static final
MediaSizeName
NA_6X9_ENVELOPE
```

6x9 North American envelope size.

---

#### NA_6X9_ENVELOPE

public static final

MediaSizeName

NA_6X9_ENVELOPE

6x9 North American envelope size.

NA_7X9_ENVELOPE

```java
public static final
MediaSizeName
NA_7X9_ENVELOPE
```

7x9 North American envelope size.

---

#### NA_7X9_ENVELOPE

public static final

MediaSizeName

NA_7X9_ENVELOPE

7x9 North American envelope size.

NA_9X11_ENVELOPE

```java
public static final
MediaSizeName
NA_9X11_ENVELOPE
```

9x11 North American envelope size.

---

#### NA_9X11_ENVELOPE

public static final

MediaSizeName

NA_9X11_ENVELOPE

9x11 North American envelope size.

NA_9X12_ENVELOPE

```java
public static final
MediaSizeName
NA_9X12_ENVELOPE
```

9x12 North American envelope size.

---

#### NA_9X12_ENVELOPE

public static final

MediaSizeName

NA_9X12_ENVELOPE

9x12 North American envelope size.

NA_10X13_ENVELOPE

```java
public static final
MediaSizeName
NA_10X13_ENVELOPE
```

10x13 North American envelope size.

---

#### NA_10X13_ENVELOPE

public static final

MediaSizeName

NA_10X13_ENVELOPE

10x13 North American envelope size.

NA_10X14_ENVELOPE

```java
public static final
MediaSizeName
NA_10X14_ENVELOPE
```

10x14North American envelope size.

---

#### NA_10X14_ENVELOPE

public static final

MediaSizeName

NA_10X14_ENVELOPE

10x14North American envelope size.

NA_10X15_ENVELOPE

```java
public static final
MediaSizeName
NA_10X15_ENVELOPE
```

10x15 North American envelope size.

---

#### NA_10X15_ENVELOPE

public static final

MediaSizeName

NA_10X15_ENVELOPE

10x15 North American envelope size.

NA_5X7

```java
public static final
MediaSizeName
NA_5X7
```

5x7 North American paper.

---

#### NA_5X7

public static final

MediaSizeName

NA_5X7

5x7 North American paper.

NA_8X10

```java
public static final
MediaSizeName
NA_8X10
```

8x10 North American paper.

---

#### NA_8X10

public static final

MediaSizeName

NA_8X10

8x10 North American paper.

Constructor Detail

- MediaSizeName

```java
protected MediaSizeName​(int value)
```

Construct a new media size enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

MediaSizeName

```java
protected MediaSizeName​(int value)
```

Construct a new media size enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### MediaSizeName

protected MediaSizeName​(int value)

Construct a new media size enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

MediaSizeName

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

MediaSizeName

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

MediaSizeName

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

MediaSizeName

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

MediaSizeName

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

MediaSizeName

.

---

