# Class Fidelity

**Source:** `java.desktop\javax\print\attribute\standard\Fidelity.html`

### Class Description

```java
public final class
Fidelity

extends
EnumSyntax

implements
PrintJobAttribute
,
PrintRequestAttribute
```

Class

Fidelity

is a printing attribute class, an enumeration, that
indicates whether total fidelity to client supplied print request attributes
is required. If

FIDELITY_TRUE

is specified and a service cannot print
the job exactly as specified it must reject the job. If

FIDELITY_FALSE

is specified a reasonable attempt to print the job is
acceptable. If not supplied the default is

FIDELITY_FALSE

.

IPP Compatibility:

The IPP boolean value is "true" for

FIDELITY_TRUE

and "false" for

FIDELITY_FALSE

. The category
name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value. See

RFC 2911

Section 15.1 for a
fuller description of the IPP fidelity attribute.

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
Fidelity
FIDELITY_TRUE

The job must be printed exactly as specified. or else rejected.

---

#### public static final
Fidelity
FIDELITY_FALSE

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

---

### Constructor Details

#### protected Fidelity​(int value)

Construct a new fidelity enumeration value with the given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

Fidelity

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

Fidelity

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

Fidelity

the category is class

Fidelity

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

Fidelity

the category name is

"ipp-attribute-fidelity"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Fidelity

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Fidelity

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Fidelity

javax.print.attribute.standard.Fidelity

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
Fidelity

extends
EnumSyntax

implements
PrintJobAttribute
,
PrintRequestAttribute
```

Class

Fidelity

is a printing attribute class, an enumeration, that
indicates whether total fidelity to client supplied print request attributes
is required. If

FIDELITY_TRUE

is specified and a service cannot print
the job exactly as specified it must reject the job. If

FIDELITY_FALSE

is specified a reasonable attempt to print the job is
acceptable. If not supplied the default is

FIDELITY_FALSE

.

IPP Compatibility:

The IPP boolean value is "true" for

FIDELITY_TRUE

and "false" for

FIDELITY_FALSE

. The category
name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value. See

RFC 2911

Section 15.1 for a
fuller description of the IPP fidelity attribute.

**See Also:** Serialized Form

public final class

Fidelity

extends

EnumSyntax

implements

PrintJobAttribute

,

PrintRequestAttribute

Class

Fidelity

is a printing attribute class, an enumeration, that
indicates whether total fidelity to client supplied print request attributes
is required. If

FIDELITY_TRUE

is specified and a service cannot print
the job exactly as specified it must reject the job. If

FIDELITY_FALSE

is specified a reasonable attempt to print the job is
acceptable. If not supplied the default is

FIDELITY_FALSE

.

IPP Compatibility:

The IPP boolean value is "true" for

FIDELITY_TRUE

and "false" for

FIDELITY_FALSE

. The category
name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value. See

RFC 2911

Section 15.1 for a
fuller description of the IPP fidelity attribute.

IPP Compatibility:

The IPP boolean value is "true" for

FIDELITY_TRUE

and "false" for

FIDELITY_FALSE

. The category
name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value. See

RFC 2911

Section 15.1 for a
fuller description of the IPP fidelity attribute.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Fidelity

FIDELITY_FALSE

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

static

Fidelity

FIDELITY_TRUE

The job must be printed exactly as specified. or else rejected.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Fidelity

​(int value)

Construct a new fidelity enumeration value with the given integer value.

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

Fidelity

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

Fidelity

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

Fidelity

FIDELITY_FALSE

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

static

Fidelity

FIDELITY_TRUE

The job must be printed exactly as specified. or else rejected.

---

#### Field Summary

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

The job must be printed exactly as specified. or else rejected.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Fidelity

​(int value)

Construct a new fidelity enumeration value with the given integer value.

---

#### Constructor Summary

Construct a new fidelity enumeration value with the given integer value.

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

Fidelity

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

Fidelity

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

Fidelity

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

Fidelity

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

- FIDELITY_TRUE

```java
public static final
Fidelity
FIDELITY_TRUE
```

The job must be printed exactly as specified. or else rejected.

- FIDELITY_FALSE

```java
public static final
Fidelity
FIDELITY_FALSE
```

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Fidelity

```java
protected Fidelity​(int value)
```

Construct a new fidelity enumeration value with the given integer value.

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

Fidelity

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

Fidelity

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

Fidelity

the category is class

Fidelity

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

Fidelity

the category name is

"ipp-attribute-fidelity"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- FIDELITY_TRUE

```java
public static final
Fidelity
FIDELITY_TRUE
```

The job must be printed exactly as specified. or else rejected.

- FIDELITY_FALSE

```java
public static final
Fidelity
FIDELITY_FALSE
```

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

---

#### Field Detail

FIDELITY_TRUE

```java
public static final
Fidelity
FIDELITY_TRUE
```

The job must be printed exactly as specified. or else rejected.

---

#### FIDELITY_TRUE

public static final

Fidelity

FIDELITY_TRUE

The job must be printed exactly as specified. or else rejected.

FIDELITY_FALSE

```java
public static final
Fidelity
FIDELITY_FALSE
```

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

---

#### FIDELITY_FALSE

public static final

Fidelity

FIDELITY_FALSE

The printer should make reasonable attempts to print the job, even if it
cannot print it exactly as specified.

Constructor Detail

- Fidelity

```java
protected Fidelity​(int value)
```

Construct a new fidelity enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

Fidelity

```java
protected Fidelity​(int value)
```

Construct a new fidelity enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Fidelity

protected Fidelity​(int value)

Construct a new fidelity enumeration value with the given integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Fidelity

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

Fidelity

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

Fidelity

the category is class

Fidelity

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

Fidelity

the category name is

"ipp-attribute-fidelity"

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

Fidelity

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

Fidelity

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Fidelity

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

Fidelity

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

Fidelity

the category is class

Fidelity

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

Fidelity

the category is class

Fidelity

itself.

For class

Fidelity

the category is class

Fidelity

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

Fidelity

the category name is

"ipp-attribute-fidelity"

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

Fidelity

the category name is

"ipp-attribute-fidelity"

.

For class

Fidelity

the category name is

"ipp-attribute-fidelity"

.

---

