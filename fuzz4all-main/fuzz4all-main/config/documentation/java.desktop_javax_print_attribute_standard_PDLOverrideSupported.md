# Class PDLOverrideSupported

**Source:** `java.desktop\javax\print\attribute\standard\PDLOverrideSupported.html`

### Class Description

```java
public class
PDLOverrideSupported

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

PDLOverrideSupported

is a printing attribute class, an
enumeration, that expresses the printer's ability to attempt to override
processing instructions embedded in documents' print data with processing
instructions specified as attributes outside the print data.

IPP Compatibility:

The category name returned by

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
PDLOverrideSupported
NOT_ATTEMPTED

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

---

#### public static final
PDLOverrideSupported
ATTEMPTED

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

---

### Constructor Details

#### protected PDLOverrideSupported​(int value)

Construct a new PDL override supported enumeration value with the given
integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

PDLOverrideSupported

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

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category is class

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category name is

"pdl-override-supported"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PDLOverrideSupported

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.PDLOverrideSupported

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.PDLOverrideSupported

javax.print.attribute.standard.PDLOverrideSupported

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public class
PDLOverrideSupported

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

PDLOverrideSupported

is a printing attribute class, an
enumeration, that expresses the printer's ability to attempt to override
processing instructions embedded in documents' print data with processing
instructions specified as attributes outside the print data.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Serialized Form

public class

PDLOverrideSupported

extends

EnumSyntax

implements

PrintServiceAttribute

Class

PDLOverrideSupported

is a printing attribute class, an
enumeration, that expresses the printer's ability to attempt to override
processing instructions embedded in documents' print data with processing
instructions specified as attributes outside the print data.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

IPP Compatibility:

The category name returned by

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

PDLOverrideSupported

ATTEMPTED

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

static

PDLOverrideSupported

NOT_ATTEMPTED

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PDLOverrideSupported

​(int value)

Construct a new PDL override supported enumeration value with the given
integer value.

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

PDLOverrideSupported

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

PDLOverrideSupported

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

PDLOverrideSupported

ATTEMPTED

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

static

PDLOverrideSupported

NOT_ATTEMPTED

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

---

#### Field Summary

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PDLOverrideSupported

​(int value)

Construct a new PDL override supported enumeration value with the given
integer value.

---

#### Constructor Summary

Construct a new PDL override supported enumeration value with the given
integer value.

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

PDLOverrideSupported

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

PDLOverrideSupported

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

PDLOverrideSupported

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

PDLOverrideSupported

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

- NOT_ATTEMPTED

```java
public static final
PDLOverrideSupported
NOT_ATTEMPTED
```

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

- ATTEMPTED

```java
public static final
PDLOverrideSupported
ATTEMPTED
```

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PDLOverrideSupported

```java
protected PDLOverrideSupported​(int value)
```

Construct a new PDL override supported enumeration value with the given
integer value.

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

PDLOverrideSupported

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

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category is class

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category name is

"pdl-override-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- NOT_ATTEMPTED

```java
public static final
PDLOverrideSupported
NOT_ATTEMPTED
```

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

- ATTEMPTED

```java
public static final
PDLOverrideSupported
ATTEMPTED
```

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

---

#### Field Detail

NOT_ATTEMPTED

```java
public static final
PDLOverrideSupported
NOT_ATTEMPTED
```

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

---

#### NOT_ATTEMPTED

public static final

PDLOverrideSupported

NOT_ATTEMPTED

The printer makes no attempt to make the external job attribute values
take precedence over embedded instructions in the documents' print data.

ATTEMPTED

```java
public static final
PDLOverrideSupported
ATTEMPTED
```

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

---

#### ATTEMPTED

public static final

PDLOverrideSupported

ATTEMPTED

The printer attempts to make the external job attribute values take
precedence over embedded instructions in the documents' print data,
however there is no guarantee.

Constructor Detail

- PDLOverrideSupported

```java
protected PDLOverrideSupported​(int value)
```

Construct a new PDL override supported enumeration value with the given
integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

PDLOverrideSupported

```java
protected PDLOverrideSupported​(int value)
```

Construct a new PDL override supported enumeration value with the given
integer value.

**Parameters:** value

- Integer value

---

#### PDLOverrideSupported

protected PDLOverrideSupported​(int value)

Construct a new PDL override supported enumeration value with the given
integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PDLOverrideSupported

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

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category is class

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category name is

"pdl-override-supported"

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

PDLOverrideSupported

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

PDLOverrideSupported

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

PDLOverrideSupported

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

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category is class

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category is class

PDLOverrideSupported

itself.

For class

PDLOverrideSupported

and any vendor-defined subclasses,
the category is class

PDLOverrideSupported

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category name is

"pdl-override-supported"

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

PDLOverrideSupported

and any vendor-defined subclasses,
the category name is

"pdl-override-supported"

.

For class

PDLOverrideSupported

and any vendor-defined subclasses,
the category name is

"pdl-override-supported"

.

---

