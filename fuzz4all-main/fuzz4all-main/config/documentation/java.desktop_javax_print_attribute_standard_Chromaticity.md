# Class Chromaticity

**Source:** `java.desktop\javax\print\attribute\standard\Chromaticity.html`

### Class Description

```java
public final class
Chromaticity

extends
EnumSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Chromaticity

is a printing attribute class, an enumeration,
that specifies monochrome or color printing. This is used by a print client
to specify how the print data should be generated or processed. It is not
descriptive of the color capabilities of the device. Query the service's

ColorSupported

attribute to determine if the device
can be verified to support color printing.

The table below shows the effects of specifying a Chromaticity attribute of

MONOCHROME

or

COLOR

for a monochrome or
color document.

Shows effects of specifying

MONOCHROME

or

COLOR

Chromaticity attributes

Chromaticity

Attribute

Effect on

Monochrome Document

Effect on

Color Document

MONOCHROME

Printed as is, in monochrome

Printed in monochrome, with colors converted to shades of gray

COLOR

Printed as is, in monochrome

Printed as is, in color

IPP Compatibility:

Chromaticity is not an IPP attribute at present.

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
Chromaticity
MONOCHROME

Monochrome printing.

---

#### public static final
Chromaticity
COLOR

Color printing.

---

### Constructor Details

#### protected Chromaticity​(int value)

Construct a new chromaticity enumeration value with the given integer
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

Chromaticity

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

Chromaticity

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

Chromaticity

, the category is the class

Chromaticity

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

Chromaticity

, the category name is

"chromaticity"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Chromaticity

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Chromaticity

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Chromaticity

javax.print.attribute.standard.Chromaticity

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
public final class
Chromaticity

extends
EnumSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Chromaticity

is a printing attribute class, an enumeration,
that specifies monochrome or color printing. This is used by a print client
to specify how the print data should be generated or processed. It is not
descriptive of the color capabilities of the device. Query the service's

ColorSupported

attribute to determine if the device
can be verified to support color printing.

The table below shows the effects of specifying a Chromaticity attribute of

MONOCHROME

or

COLOR

for a monochrome or
color document.

Shows effects of specifying

MONOCHROME

or

COLOR

Chromaticity attributes

Chromaticity

Attribute

Effect on

Monochrome Document

Effect on

Color Document

MONOCHROME

Printed as is, in monochrome

Printed in monochrome, with colors converted to shades of gray

COLOR

Printed as is, in monochrome

Printed as is, in color

IPP Compatibility:

Chromaticity is not an IPP attribute at present.

**See Also:** Serialized Form

public final class

Chromaticity

extends

EnumSyntax

implements

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

Class

Chromaticity

is a printing attribute class, an enumeration,
that specifies monochrome or color printing. This is used by a print client
to specify how the print data should be generated or processed. It is not
descriptive of the color capabilities of the device. Query the service's

ColorSupported

attribute to determine if the device
can be verified to support color printing.

The table below shows the effects of specifying a Chromaticity attribute of

MONOCHROME

or

COLOR

for a monochrome or
color document.

Shows effects of specifying

MONOCHROME

or

COLOR

Chromaticity attributes

Chromaticity

Attribute

Effect on

Monochrome Document

Effect on

Color Document

MONOCHROME

Printed as is, in monochrome

Printed in monochrome, with colors converted to shades of gray

COLOR

Printed as is, in monochrome

Printed as is, in color

IPP Compatibility:

Chromaticity is not an IPP attribute at present.

The table below shows the effects of specifying a Chromaticity attribute of

MONOCHROME

or

COLOR

for a monochrome or
color document.

Shows effects of specifying

MONOCHROME

or

COLOR

Chromaticity attributes

Chromaticity

Attribute

Effect on

Monochrome Document

Effect on

Color Document

MONOCHROME

Printed as is, in monochrome

Printed in monochrome, with colors converted to shades of gray

COLOR

Printed as is, in monochrome

Printed as is, in color

IPP Compatibility:

Chromaticity is not an IPP attribute at present.

IPP Compatibility:

Chromaticity is not an IPP attribute at present.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Chromaticity

COLOR

Color printing.

static

Chromaticity

MONOCHROME

Monochrome printing.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Chromaticity

​(int value)

Construct a new chromaticity enumeration value with the given integer
value.

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

Chromaticity

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

Chromaticity

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

Chromaticity

COLOR

Color printing.

static

Chromaticity

MONOCHROME

Monochrome printing.

---

#### Field Summary

Color printing.

Monochrome printing.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Chromaticity

​(int value)

Construct a new chromaticity enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new chromaticity enumeration value with the given integer
value.

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

Chromaticity

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

Chromaticity

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

Chromaticity

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

Chromaticity

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

- MONOCHROME

```java
public static final
Chromaticity
MONOCHROME
```

Monochrome printing.

- COLOR

```java
public static final
Chromaticity
COLOR
```

Color printing.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Chromaticity

```java
protected Chromaticity​(int value)
```

Construct a new chromaticity enumeration value with the given integer
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

Chromaticity

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

Chromaticity

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

Chromaticity

, the category is the class

Chromaticity

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

Chromaticity

, the category name is

"chromaticity"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- MONOCHROME

```java
public static final
Chromaticity
MONOCHROME
```

Monochrome printing.

- COLOR

```java
public static final
Chromaticity
COLOR
```

Color printing.

---

#### Field Detail

MONOCHROME

```java
public static final
Chromaticity
MONOCHROME
```

Monochrome printing.

---

#### MONOCHROME

public static final

Chromaticity

MONOCHROME

Monochrome printing.

COLOR

```java
public static final
Chromaticity
COLOR
```

Color printing.

---

#### COLOR

public static final

Chromaticity

COLOR

Color printing.

Constructor Detail

- Chromaticity

```java
protected Chromaticity​(int value)
```

Construct a new chromaticity enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

Chromaticity

```java
protected Chromaticity​(int value)
```

Construct a new chromaticity enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Chromaticity

protected Chromaticity​(int value)

Construct a new chromaticity enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Chromaticity

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

Chromaticity

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

Chromaticity

, the category is the class

Chromaticity

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

Chromaticity

, the category name is

"chromaticity"

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

Chromaticity

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

Chromaticity

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Chromaticity

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

Chromaticity

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

Chromaticity

, the category is the class

Chromaticity

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

Chromaticity

, the category is the class

Chromaticity

itself.

For class

Chromaticity

, the category is the class

Chromaticity

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

Chromaticity

, the category name is

"chromaticity"

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

Chromaticity

, the category name is

"chromaticity"

.

For class

Chromaticity

, the category name is

"chromaticity"

.

---

