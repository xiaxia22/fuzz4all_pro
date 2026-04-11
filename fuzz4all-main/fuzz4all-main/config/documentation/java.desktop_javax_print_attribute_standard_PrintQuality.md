# Class PrintQuality

**Source:** `java.desktop\javax\print\attribute\standard\PrintQuality.html`

### Class Description

```java
public class
PrintQuality

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

PrintQuality

is a printing attribute class, an enumeration,
that specifies the print quality that the printer uses for the job.

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

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

#### public static final
PrintQuality
DRAFT

Lowest quality available on the printer.

---

#### public static final
PrintQuality
NORMAL

Normal or intermediate quality on the printer.

---

#### public static final
PrintQuality
HIGH

Highest quality available on the printer.

---

### Constructor Details

#### protected PrintQuality​(int value)

Construct a new print quality enumeration value with the given integer
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

PrintQuality

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

PrintQuality

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the value table

---

#### protected int getOffset()

Returns the lowest integer value used by class

PrintQuality

.

**Overrides:**
- getOffset

in class

EnumSyntax

**Returns:**
- the offset of the lowest enumeration value

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PrintQuality

and any vendor-defined subclasses, the
category is class

PrintQuality

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

PrintQuality

and any vendor-defined subclasses, the
category name is

"print-quality"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrintQuality

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.PrintQuality

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.PrintQuality

javax.print.attribute.standard.PrintQuality

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
PrintQuality

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

PrintQuality

is a printing attribute class, an enumeration,
that specifies the print quality that the printer uses for the job.

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

PrintQuality

extends

EnumSyntax

implements

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

Class

PrintQuality

is a printing attribute class, an enumeration,
that specifies the print quality that the printer uses for the job.

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

PrintQuality

DRAFT

Lowest quality available on the printer.

static

PrintQuality

HIGH

Highest quality available on the printer.

static

PrintQuality

NORMAL

Normal or intermediate quality on the printer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrintQuality

​(int value)

Construct a new print quality enumeration value with the given integer
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

PrintQuality

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected int

getOffset

()

Returns the lowest integer value used by class

PrintQuality

.

protected

String

[]

getStringTable

()

Returns the string table for class

PrintQuality

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

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

PrintQuality

DRAFT

Lowest quality available on the printer.

static

PrintQuality

HIGH

Highest quality available on the printer.

static

PrintQuality

NORMAL

Normal or intermediate quality on the printer.

---

#### Field Summary

Lowest quality available on the printer.

Highest quality available on the printer.

Normal or intermediate quality on the printer.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrintQuality

​(int value)

Construct a new print quality enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new print quality enumeration value with the given integer
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

PrintQuality

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected int

getOffset

()

Returns the lowest integer value used by class

PrintQuality

.

protected

String

[]

getStringTable

()

Returns the string table for class

PrintQuality

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

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

PrintQuality

.

Get the name of the category of which this attribute value is an
instance.

Returns the lowest integer value used by class

PrintQuality

.

Returns the string table for class

PrintQuality

.

Methods declared in class javax.print.attribute.

EnumSyntax

clone

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

- DRAFT

```java
public static final
PrintQuality
DRAFT
```

Lowest quality available on the printer.

- NORMAL

```java
public static final
PrintQuality
NORMAL
```

Normal or intermediate quality on the printer.

- HIGH

```java
public static final
PrintQuality
HIGH
```

Highest quality available on the printer.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrintQuality

```java
protected PrintQuality​(int value)
```

Construct a new print quality enumeration value with the given integer
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

PrintQuality

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

PrintQuality

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getOffset

```java
protected int getOffset()
```

Returns the lowest integer value used by class

PrintQuality

.

**Overrides:** getOffset

in class

EnumSyntax
**Returns:** the offset of the lowest enumeration value

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

PrintQuality

and any vendor-defined subclasses, the
category is class

PrintQuality

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

PrintQuality

and any vendor-defined subclasses, the
category name is

"print-quality"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- DRAFT

```java
public static final
PrintQuality
DRAFT
```

Lowest quality available on the printer.

- NORMAL

```java
public static final
PrintQuality
NORMAL
```

Normal or intermediate quality on the printer.

- HIGH

```java
public static final
PrintQuality
HIGH
```

Highest quality available on the printer.

---

#### Field Detail

DRAFT

```java
public static final
PrintQuality
DRAFT
```

Lowest quality available on the printer.

---

#### DRAFT

public static final

PrintQuality

DRAFT

Lowest quality available on the printer.

NORMAL

```java
public static final
PrintQuality
NORMAL
```

Normal or intermediate quality on the printer.

---

#### NORMAL

public static final

PrintQuality

NORMAL

Normal or intermediate quality on the printer.

HIGH

```java
public static final
PrintQuality
HIGH
```

Highest quality available on the printer.

---

#### HIGH

public static final

PrintQuality

HIGH

Highest quality available on the printer.

Constructor Detail

- PrintQuality

```java
protected PrintQuality​(int value)
```

Construct a new print quality enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

PrintQuality

```java
protected PrintQuality​(int value)
```

Construct a new print quality enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### PrintQuality

protected PrintQuality​(int value)

Construct a new print quality enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PrintQuality

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

PrintQuality

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getOffset

```java
protected int getOffset()
```

Returns the lowest integer value used by class

PrintQuality

.

**Overrides:** getOffset

in class

EnumSyntax
**Returns:** the offset of the lowest enumeration value

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

PrintQuality

and any vendor-defined subclasses, the
category is class

PrintQuality

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

PrintQuality

and any vendor-defined subclasses, the
category name is

"print-quality"

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

PrintQuality

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

PrintQuality

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

PrintQuality

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

PrintQuality

.

getOffset

```java
protected int getOffset()
```

Returns the lowest integer value used by class

PrintQuality

.

**Overrides:** getOffset

in class

EnumSyntax
**Returns:** the offset of the lowest enumeration value

---

#### getOffset

protected int getOffset()

Returns the lowest integer value used by class

PrintQuality

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

PrintQuality

and any vendor-defined subclasses, the
category is class

PrintQuality

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

PrintQuality

and any vendor-defined subclasses, the
category is class

PrintQuality

itself.

For class

PrintQuality

and any vendor-defined subclasses, the
category is class

PrintQuality

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

PrintQuality

and any vendor-defined subclasses, the
category name is

"print-quality"

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

PrintQuality

and any vendor-defined subclasses, the
category name is

"print-quality"

.

For class

PrintQuality

and any vendor-defined subclasses, the
category name is

"print-quality"

.

---

