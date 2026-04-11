# Class ColorSupported

**Source:** `java.desktop\javax\print\attribute\standard\ColorSupported.html`

### Class Description

```java
public final class
ColorSupported

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

ColorSupported

is a printing attribute class, an enumeration,
that identifies whether the device is capable of any type of color printing
at all, including highlight color as well as full process color. All document
instructions having to do with color are embedded within the print data (none
are attributes attached to the job outside the print data).

Note: End users are able to determine the nature and details of the color
support by querying the

PrinterMoreInfoManufacturer

attribute.

Don't confuse the

ColorSupported

attribute with the

Chromaticity

attribute.

Chromaticity

is an attribute the client can specify for
a job to tell the printer whether to print a document in monochrome or color,
possibly causing the printer to print a color document in monochrome.

ColorSupported

is a printer description attribute that tells whether
the printer can print in color regardless of how the client specifies to
print any particular document.

IPP Compatibility:

The IPP boolean value is "true" for SUPPORTED and
"false" for NOT_SUPPORTED. The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

---

### Field Details

#### public static final
ColorSupported
NOT_SUPPORTED

The printer is not capable of any type of color printing.

---

#### public static final
ColorSupported
SUPPORTED

The printer is capable of some type of color printing, such as highlight
color or full process color.

---

### Constructor Details

#### protected ColorSupported​(int value)

Construct a new color supported enumeration value with the given integer
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

ColorSupported

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

ColorSupported

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

ColorSupported

, the category is class

ColorSupported

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

ColorSupported

, the category name is

"color-supported"

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class ColorSupported

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.ColorSupported

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.ColorSupported

javax.print.attribute.standard.ColorSupported

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
ColorSupported

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

ColorSupported

is a printing attribute class, an enumeration,
that identifies whether the device is capable of any type of color printing
at all, including highlight color as well as full process color. All document
instructions having to do with color are embedded within the print data (none
are attributes attached to the job outside the print data).

Note: End users are able to determine the nature and details of the color
support by querying the

PrinterMoreInfoManufacturer

attribute.

Don't confuse the

ColorSupported

attribute with the

Chromaticity

attribute.

Chromaticity

is an attribute the client can specify for
a job to tell the printer whether to print a document in monochrome or color,
possibly causing the printer to print a color document in monochrome.

ColorSupported

is a printer description attribute that tells whether
the printer can print in color regardless of how the client specifies to
print any particular document.

IPP Compatibility:

The IPP boolean value is "true" for SUPPORTED and
"false" for NOT_SUPPORTED. The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Serialized Form

public final class

ColorSupported

extends

EnumSyntax

implements

PrintServiceAttribute

Class

ColorSupported

is a printing attribute class, an enumeration,
that identifies whether the device is capable of any type of color printing
at all, including highlight color as well as full process color. All document
instructions having to do with color are embedded within the print data (none
are attributes attached to the job outside the print data).

Note: End users are able to determine the nature and details of the color
support by querying the

PrinterMoreInfoManufacturer

attribute.

Don't confuse the

ColorSupported

attribute with the

Chromaticity

attribute.

Chromaticity

is an attribute the client can specify for
a job to tell the printer whether to print a document in monochrome or color,
possibly causing the printer to print a color document in monochrome.

ColorSupported

is a printer description attribute that tells whether
the printer can print in color regardless of how the client specifies to
print any particular document.

IPP Compatibility:

The IPP boolean value is "true" for SUPPORTED and
"false" for NOT_SUPPORTED. The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

Note: End users are able to determine the nature and details of the color
support by querying the

PrinterMoreInfoManufacturer

attribute.

Don't confuse the

ColorSupported

attribute with the

Chromaticity

attribute.

Chromaticity

is an attribute the client can specify for
a job to tell the printer whether to print a document in monochrome or color,
possibly causing the printer to print a color document in monochrome.

ColorSupported

is a printer description attribute that tells whether
the printer can print in color regardless of how the client specifies to
print any particular document.

IPP Compatibility:

The IPP boolean value is "true" for SUPPORTED and
"false" for NOT_SUPPORTED. The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

Don't confuse the

ColorSupported

attribute with the

Chromaticity

attribute.

Chromaticity

is an attribute the client can specify for
a job to tell the printer whether to print a document in monochrome or color,
possibly causing the printer to print a color document in monochrome.

ColorSupported

is a printer description attribute that tells whether
the printer can print in color regardless of how the client specifies to
print any particular document.

IPP Compatibility:

The IPP boolean value is "true" for SUPPORTED and
"false" for NOT_SUPPORTED. The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

IPP Compatibility:

The IPP boolean value is "true" for SUPPORTED and
"false" for NOT_SUPPORTED. The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ColorSupported

NOT_SUPPORTED

The printer is not capable of any type of color printing.

static

ColorSupported

SUPPORTED

The printer is capable of some type of color printing, such as highlight
color or full process color.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ColorSupported

​(int value)

Construct a new color supported enumeration value with the given integer
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

ColorSupported

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

ColorSupported

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

ColorSupported

NOT_SUPPORTED

The printer is not capable of any type of color printing.

static

ColorSupported

SUPPORTED

The printer is capable of some type of color printing, such as highlight
color or full process color.

---

#### Field Summary

The printer is not capable of any type of color printing.

The printer is capable of some type of color printing, such as highlight
color or full process color.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ColorSupported

​(int value)

Construct a new color supported enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new color supported enumeration value with the given integer
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

ColorSupported

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

ColorSupported

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

ColorSupported

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

ColorSupported

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

- NOT_SUPPORTED

```java
public static final
ColorSupported
NOT_SUPPORTED
```

The printer is not capable of any type of color printing.

- SUPPORTED

```java
public static final
ColorSupported
SUPPORTED
```

The printer is capable of some type of color printing, such as highlight
color or full process color.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ColorSupported

```java
protected ColorSupported​(int value)
```

Construct a new color supported enumeration value with the given integer
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

ColorSupported

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

ColorSupported

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

ColorSupported

, the category is class

ColorSupported

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

ColorSupported

, the category name is

"color-supported"

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- NOT_SUPPORTED

```java
public static final
ColorSupported
NOT_SUPPORTED
```

The printer is not capable of any type of color printing.

- SUPPORTED

```java
public static final
ColorSupported
SUPPORTED
```

The printer is capable of some type of color printing, such as highlight
color or full process color.

---

#### Field Detail

NOT_SUPPORTED

```java
public static final
ColorSupported
NOT_SUPPORTED
```

The printer is not capable of any type of color printing.

---

#### NOT_SUPPORTED

public static final

ColorSupported

NOT_SUPPORTED

The printer is not capable of any type of color printing.

SUPPORTED

```java
public static final
ColorSupported
SUPPORTED
```

The printer is capable of some type of color printing, such as highlight
color or full process color.

---

#### SUPPORTED

public static final

ColorSupported

SUPPORTED

The printer is capable of some type of color printing, such as highlight
color or full process color.

Constructor Detail

- ColorSupported

```java
protected ColorSupported​(int value)
```

Construct a new color supported enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

ColorSupported

```java
protected ColorSupported​(int value)
```

Construct a new color supported enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### ColorSupported

protected ColorSupported​(int value)

Construct a new color supported enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

ColorSupported

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

ColorSupported

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

ColorSupported

, the category is class

ColorSupported

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

ColorSupported

, the category name is

"color-supported"

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

ColorSupported

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

ColorSupported

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

ColorSupported

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

ColorSupported

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

ColorSupported

, the category is class

ColorSupported

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

ColorSupported

, the category is class

ColorSupported

itself.

For class

ColorSupported

, the category is class

ColorSupported

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

ColorSupported

, the category name is

"color-supported"

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

ColorSupported

, the category name is

"color-supported"

For class

ColorSupported

, the category name is

"color-supported"

---

