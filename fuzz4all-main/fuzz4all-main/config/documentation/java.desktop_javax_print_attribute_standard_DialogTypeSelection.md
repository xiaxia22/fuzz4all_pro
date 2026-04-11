# Class DialogTypeSelection

**Source:** `java.desktop\javax\print\attribute\standard\DialogTypeSelection.html`

### Class Description

```java
public final class
DialogTypeSelection

extends
EnumSyntax

implements
PrintRequestAttribute
```

Class

DialogTypeSelection

is a printing attribute class, an
enumeration, that indicates the user dialog type to be used for specifying
printing options. If

NATIVE

is specified, then where available, a
native platform dialog is displayed. If

COMMON

is specified, a
cross-platform print dialog is displayed.

This option to specify a native dialog for use with an IPP attribute set
provides a standard way to reflect back of the setting and option changes
made by a user to the calling application, and integrates the native dialog
into the Java printing APIs. But note that some options and settings in a
native dialog may not necessarily map to IPP attributes as they may be
non-standard platform, or even printer specific options.

IPP Compatibility:

This is not an IPP attribute.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintRequestAttribute

---

### Field Details

#### public static final
DialogTypeSelection
NATIVE

The native platform print dialog should be used.

---

#### public static final
DialogTypeSelection
COMMON

The cross-platform print dialog should be used.

---

### Constructor Details

#### protected DialogTypeSelection​(int value)

Constructs a new dialog type selection enumeration value with the given
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

DialogTypeSelection

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

DialogTypeSelection

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

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogTypeSelection

the category is class

DialogTypeSelection

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

Gets the name of the category of which this attribute value is an
instance.

For class

DialogTypeSelection

the category name is

"dialog-type-selection"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class DialogTypeSelection

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.DialogTypeSelection

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.DialogTypeSelection

javax.print.attribute.standard.DialogTypeSelection

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintRequestAttribute

```java
public final class
DialogTypeSelection

extends
EnumSyntax

implements
PrintRequestAttribute
```

Class

DialogTypeSelection

is a printing attribute class, an
enumeration, that indicates the user dialog type to be used for specifying
printing options. If

NATIVE

is specified, then where available, a
native platform dialog is displayed. If

COMMON

is specified, a
cross-platform print dialog is displayed.

This option to specify a native dialog for use with an IPP attribute set
provides a standard way to reflect back of the setting and option changes
made by a user to the calling application, and integrates the native dialog
into the Java printing APIs. But note that some options and settings in a
native dialog may not necessarily map to IPP attributes as they may be
non-standard platform, or even printer specific options.

IPP Compatibility:

This is not an IPP attribute.

**Since:** 1.7
**See Also:** Serialized Form

public final class

DialogTypeSelection

extends

EnumSyntax

implements

PrintRequestAttribute

Class

DialogTypeSelection

is a printing attribute class, an
enumeration, that indicates the user dialog type to be used for specifying
printing options. If

NATIVE

is specified, then where available, a
native platform dialog is displayed. If

COMMON

is specified, a
cross-platform print dialog is displayed.

This option to specify a native dialog for use with an IPP attribute set
provides a standard way to reflect back of the setting and option changes
made by a user to the calling application, and integrates the native dialog
into the Java printing APIs. But note that some options and settings in a
native dialog may not necessarily map to IPP attributes as they may be
non-standard platform, or even printer specific options.

IPP Compatibility:

This is not an IPP attribute.

This option to specify a native dialog for use with an IPP attribute set
provides a standard way to reflect back of the setting and option changes
made by a user to the calling application, and integrates the native dialog
into the Java printing APIs. But note that some options and settings in a
native dialog may not necessarily map to IPP attributes as they may be
non-standard platform, or even printer specific options.

IPP Compatibility:

This is not an IPP attribute.

IPP Compatibility:

This is not an IPP attribute.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

DialogTypeSelection

COMMON

The cross-platform print dialog should be used.

static

DialogTypeSelection

NATIVE

The native platform print dialog should be used.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DialogTypeSelection

​(int value)

Constructs a new dialog type selection enumeration value with the given
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

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

DialogTypeSelection

.

String

getName

()

Gets the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

DialogTypeSelection

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

DialogTypeSelection

COMMON

The cross-platform print dialog should be used.

static

DialogTypeSelection

NATIVE

The native platform print dialog should be used.

---

#### Field Summary

The cross-platform print dialog should be used.

The native platform print dialog should be used.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DialogTypeSelection

​(int value)

Constructs a new dialog type selection enumeration value with the given
integer value.

---

#### Constructor Summary

Constructs a new dialog type selection enumeration value with the given
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

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

DialogTypeSelection

.

String

getName

()

Gets the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

DialogTypeSelection

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

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

Returns the enumeration value table for class

DialogTypeSelection

.

Gets the name of the category of which this attribute value is an
instance.

Returns the string table for class

DialogTypeSelection

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

- NATIVE

```java
public static final
DialogTypeSelection
NATIVE
```

The native platform print dialog should be used.

- COMMON

```java
public static final
DialogTypeSelection
COMMON
```

The cross-platform print dialog should be used.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DialogTypeSelection

```java
protected DialogTypeSelection​(int value)
```

Constructs a new dialog type selection enumeration value with the given
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

DialogTypeSelection

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

DialogTypeSelection

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

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogTypeSelection

the category is class

DialogTypeSelection

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

Gets the name of the category of which this attribute value is an
instance.

For class

DialogTypeSelection

the category name is

"dialog-type-selection"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- NATIVE

```java
public static final
DialogTypeSelection
NATIVE
```

The native platform print dialog should be used.

- COMMON

```java
public static final
DialogTypeSelection
COMMON
```

The cross-platform print dialog should be used.

---

#### Field Detail

NATIVE

```java
public static final
DialogTypeSelection
NATIVE
```

The native platform print dialog should be used.

---

#### NATIVE

public static final

DialogTypeSelection

NATIVE

The native platform print dialog should be used.

COMMON

```java
public static final
DialogTypeSelection
COMMON
```

The cross-platform print dialog should be used.

---

#### COMMON

public static final

DialogTypeSelection

COMMON

The cross-platform print dialog should be used.

Constructor Detail

- DialogTypeSelection

```java
protected DialogTypeSelection​(int value)
```

Constructs a new dialog type selection enumeration value with the given
integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

DialogTypeSelection

```java
protected DialogTypeSelection​(int value)
```

Constructs a new dialog type selection enumeration value with the given
integer value.

**Parameters:** value

- Integer value

---

#### DialogTypeSelection

protected DialogTypeSelection​(int value)

Constructs a new dialog type selection enumeration value with the given
integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

DialogTypeSelection

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

DialogTypeSelection

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

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogTypeSelection

the category is class

DialogTypeSelection

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

Gets the name of the category of which this attribute value is an
instance.

For class

DialogTypeSelection

the category name is

"dialog-type-selection"

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

DialogTypeSelection

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

DialogTypeSelection

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

DialogTypeSelection

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

DialogTypeSelection

.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogTypeSelection

the category is class

DialogTypeSelection

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

Gets the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogTypeSelection

the category is class

DialogTypeSelection

itself.

For class

DialogTypeSelection

the category is class

DialogTypeSelection

itself.

getName

```java
public final
String
getName()
```

Gets the name of the category of which this attribute value is an
instance.

For class

DialogTypeSelection

the category name is

"dialog-type-selection"

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

Gets the name of the category of which this attribute value is an
instance.

For class

DialogTypeSelection

the category name is

"dialog-type-selection"

.

For class

DialogTypeSelection

the category name is

"dialog-type-selection"

.

---

