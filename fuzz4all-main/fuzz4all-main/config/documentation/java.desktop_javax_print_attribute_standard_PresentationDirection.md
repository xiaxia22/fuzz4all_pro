# Class PresentationDirection

**Source:** `java.desktop\javax\print\attribute\standard\PresentationDirection.html`

### Class Description

```java
public final class
PresentationDirection

extends
EnumSyntax

implements
PrintJobAttribute
,
PrintRequestAttribute
```

Class

PresentationDirection

is a printing attribute class, an
enumeration, that is used in conjunction with the

NumberUp

attribute to indicate the layout of multiple print-stream pages to impose
upon a single side of an instance of a selected medium. This is useful to
mirror the text layout conventions of different scripts. For example, English
is "toright-tobottom", Hebrew is "toleft-tobottom" and Japanese is usually
"tobottom-toleft".

IPP Compatibility:

This attribute is not an IPP 1.1 attribute; it is
an attribute in the Production Printing Extension
(

PDF

) of IPP 1.1. The category name returned by

getName()

is the
IPP attribute name. The enumeration's integer value is the IPP enum value.
The

toString()

method returns the IPP string representation of the
attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

#### public static final
PresentationDirection
TOBOTTOM_TORIGHT

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

---

#### public static final
PresentationDirection
TOBOTTOM_TOLEFT

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

---

#### public static final
PresentationDirection
TOTOP_TORIGHT

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

---

#### public static final
PresentationDirection
TOTOP_TOLEFT

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

---

#### public static final
PresentationDirection
TORIGHT_TOBOTTOM

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

---

#### public static final
PresentationDirection
TORIGHT_TOTOP

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

---

#### public static final
PresentationDirection
TOLEFT_TOBOTTOM

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

---

#### public static final
PresentationDirection
TOLEFT_TOTOP

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

---

### Constructor Details

*No entries found.*

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

PresentationDirection

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

PresentationDirection

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the value table

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PresentationDirection

the category is class

PresentationDirection

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

PresentationDirection

the category name is

"presentation-direction"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PresentationDirection

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.PresentationDirection

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.PresentationDirection

javax.print.attribute.standard.PresentationDirection

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public final class
PresentationDirection

extends
EnumSyntax

implements
PrintJobAttribute
,
PrintRequestAttribute
```

Class

PresentationDirection

is a printing attribute class, an
enumeration, that is used in conjunction with the

NumberUp

attribute to indicate the layout of multiple print-stream pages to impose
upon a single side of an instance of a selected medium. This is useful to
mirror the text layout conventions of different scripts. For example, English
is "toright-tobottom", Hebrew is "toleft-tobottom" and Japanese is usually
"tobottom-toleft".

IPP Compatibility:

This attribute is not an IPP 1.1 attribute; it is
an attribute in the Production Printing Extension
(

PDF

) of IPP 1.1. The category name returned by

getName()

is the
IPP attribute name. The enumeration's integer value is the IPP enum value.
The

toString()

method returns the IPP string representation of the
attribute value.

**See Also:** Serialized Form

public final class

PresentationDirection

extends

EnumSyntax

implements

PrintJobAttribute

,

PrintRequestAttribute

Class

PresentationDirection

is a printing attribute class, an
enumeration, that is used in conjunction with the

NumberUp

attribute to indicate the layout of multiple print-stream pages to impose
upon a single side of an instance of a selected medium. This is useful to
mirror the text layout conventions of different scripts. For example, English
is "toright-tobottom", Hebrew is "toleft-tobottom" and Japanese is usually
"tobottom-toleft".

IPP Compatibility:

This attribute is not an IPP 1.1 attribute; it is
an attribute in the Production Printing Extension
(

PDF

) of IPP 1.1. The category name returned by

getName()

is the
IPP attribute name. The enumeration's integer value is the IPP enum value.
The

toString()

method returns the IPP string representation of the
attribute value.

IPP Compatibility:

This attribute is not an IPP 1.1 attribute; it is
an attribute in the Production Printing Extension
(

PDF

) of IPP 1.1. The category name returned by

getName()

is the
IPP attribute name. The enumeration's integer value is the IPP enum value.
The

toString()

method returns the IPP string representation of the
attribute value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

PresentationDirection

TOBOTTOM_TOLEFT

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

static

PresentationDirection

TOBOTTOM_TORIGHT

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

static

PresentationDirection

TOLEFT_TOBOTTOM

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

static

PresentationDirection

TOLEFT_TOTOP

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

static

PresentationDirection

TORIGHT_TOBOTTOM

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

static

PresentationDirection

TORIGHT_TOTOP

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

static

PresentationDirection

TOTOP_TOLEFT

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

static

PresentationDirection

TOTOP_TORIGHT

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

PresentationDirection

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

PresentationDirection

.

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

equals

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

Field Summary

Fields

Modifier and Type

Field

Description

static

PresentationDirection

TOBOTTOM_TOLEFT

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

static

PresentationDirection

TOBOTTOM_TORIGHT

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

static

PresentationDirection

TOLEFT_TOBOTTOM

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

static

PresentationDirection

TOLEFT_TOTOP

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

static

PresentationDirection

TORIGHT_TOBOTTOM

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

static

PresentationDirection

TORIGHT_TOTOP

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

static

PresentationDirection

TOTOP_TOLEFT

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

static

PresentationDirection

TOTOP_TORIGHT

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

---

#### Field Summary

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

PresentationDirection

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

PresentationDirection

.

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

equals

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

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Returns the enumeration value table for class

PresentationDirection

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

PresentationDirection

.

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

equals

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

============ FIELD DETAIL ===========

- Field Detail

- TOBOTTOM_TORIGHT

```java
public static final
PresentationDirection
TOBOTTOM_TORIGHT
```

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

- TOBOTTOM_TOLEFT

```java
public static final
PresentationDirection
TOBOTTOM_TOLEFT
```

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

- TOTOP_TORIGHT

```java
public static final
PresentationDirection
TOTOP_TORIGHT
```

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

- TOTOP_TOLEFT

```java
public static final
PresentationDirection
TOTOP_TOLEFT
```

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

- TORIGHT_TOBOTTOM

```java
public static final
PresentationDirection
TORIGHT_TOBOTTOM
```

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

- TORIGHT_TOTOP

```java
public static final
PresentationDirection
TORIGHT_TOTOP
```

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

- TOLEFT_TOBOTTOM

```java
public static final
PresentationDirection
TOLEFT_TOBOTTOM
```

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

- TOLEFT_TOTOP

```java
public static final
PresentationDirection
TOLEFT_TOTOP
```

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

============ METHOD DETAIL ==========

- Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PresentationDirection

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

PresentationDirection

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PresentationDirection

the category is class

PresentationDirection

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

PresentationDirection

the category name is

"presentation-direction"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- TOBOTTOM_TORIGHT

```java
public static final
PresentationDirection
TOBOTTOM_TORIGHT
```

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

- TOBOTTOM_TOLEFT

```java
public static final
PresentationDirection
TOBOTTOM_TOLEFT
```

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

- TOTOP_TORIGHT

```java
public static final
PresentationDirection
TOTOP_TORIGHT
```

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

- TOTOP_TOLEFT

```java
public static final
PresentationDirection
TOTOP_TOLEFT
```

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

- TORIGHT_TOBOTTOM

```java
public static final
PresentationDirection
TORIGHT_TOBOTTOM
```

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

- TORIGHT_TOTOP

```java
public static final
PresentationDirection
TORIGHT_TOTOP
```

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

- TOLEFT_TOBOTTOM

```java
public static final
PresentationDirection
TOLEFT_TOBOTTOM
```

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

- TOLEFT_TOTOP

```java
public static final
PresentationDirection
TOLEFT_TOTOP
```

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

---

#### Field Detail

TOBOTTOM_TORIGHT

```java
public static final
PresentationDirection
TOBOTTOM_TORIGHT
```

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

---

#### TOBOTTOM_TORIGHT

public static final

PresentationDirection

TOBOTTOM_TORIGHT

Pages are laid out in columns starting at the top left, proceeding
towards the bottom & right.

TOBOTTOM_TOLEFT

```java
public static final
PresentationDirection
TOBOTTOM_TOLEFT
```

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

---

#### TOBOTTOM_TOLEFT

public static final

PresentationDirection

TOBOTTOM_TOLEFT

Pages are laid out in columns starting at the top right, proceeding
towards the bottom & left.

TOTOP_TORIGHT

```java
public static final
PresentationDirection
TOTOP_TORIGHT
```

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

---

#### TOTOP_TORIGHT

public static final

PresentationDirection

TOTOP_TORIGHT

Pages are laid out in columns starting at the bottom left, proceeding
towards the top & right.

TOTOP_TOLEFT

```java
public static final
PresentationDirection
TOTOP_TOLEFT
```

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

---

#### TOTOP_TOLEFT

public static final

PresentationDirection

TOTOP_TOLEFT

Pages are laid out in columns starting at the bottom right, proceeding
towards the top & left.

TORIGHT_TOBOTTOM

```java
public static final
PresentationDirection
TORIGHT_TOBOTTOM
```

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

---

#### TORIGHT_TOBOTTOM

public static final

PresentationDirection

TORIGHT_TOBOTTOM

Pages are laid out in rows starting at the top left, proceeding towards
the right & bottom.

TORIGHT_TOTOP

```java
public static final
PresentationDirection
TORIGHT_TOTOP
```

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

---

#### TORIGHT_TOTOP

public static final

PresentationDirection

TORIGHT_TOTOP

Pages are laid out in rows starting at the bottom left, proceeding
towards the right & top.

TOLEFT_TOBOTTOM

```java
public static final
PresentationDirection
TOLEFT_TOBOTTOM
```

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

---

#### TOLEFT_TOBOTTOM

public static final

PresentationDirection

TOLEFT_TOBOTTOM

Pages are laid out in rows starting at the top right, proceeding towards
the left & bottom.

TOLEFT_TOTOP

```java
public static final
PresentationDirection
TOLEFT_TOTOP
```

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

---

#### TOLEFT_TOTOP

public static final

PresentationDirection

TOLEFT_TOTOP

Pages are laid out in rows starting at the bottom right, proceeding
towards the left & top.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PresentationDirection

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

PresentationDirection

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PresentationDirection

the category is class

PresentationDirection

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

PresentationDirection

the category name is

"presentation-direction"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PresentationDirection

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

PresentationDirection

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

PresentationDirection

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

PresentationDirection

.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PresentationDirection

the category is class

PresentationDirection

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PresentationDirection

the category is class

PresentationDirection

itself.

For class

PresentationDirection

the category is class

PresentationDirection

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

PresentationDirection

the category name is

"presentation-direction"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

PresentationDirection

the category name is

"presentation-direction"

.

For class

PresentationDirection

the category name is

"presentation-direction"

.

---

