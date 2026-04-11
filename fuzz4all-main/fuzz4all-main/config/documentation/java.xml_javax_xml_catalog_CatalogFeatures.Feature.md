# Enum CatalogFeatures.Feature

**Source:** `java.xml\javax\xml\catalog\CatalogFeatures.Feature.html`

### Class Description

```java
public static enum
CatalogFeatures.Feature

extends
Enum
<
CatalogFeatures.Feature
>
```

A Feature type as defined in the

Catalog Features table

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

CatalogFeatures.Feature

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
CatalogFeatures.Feature
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CatalogFeatures.Feature c : CatalogFeatures.Feature.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
CatalogFeatures.Feature
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public
String
getPropertyName()

Returns the name of the corresponding System Property.

**Returns:**
- the name of the System Property

---

#### public
String
defaultValue()

Returns the default value of the property.

**Returns:**
- the default value of the property

---

### Additional Sections

#### Enum CatalogFeatures.Feature

java.lang.Object

- java.lang.Enum

<

CatalogFeatures.Feature

>
- - javax.xml.catalog.CatalogFeatures.Feature

java.lang.Enum

<

CatalogFeatures.Feature

>

- javax.xml.catalog.CatalogFeatures.Feature

javax.xml.catalog.CatalogFeatures.Feature

**All Implemented Interfaces:** Serializable

,

Comparable

<

CatalogFeatures.Feature

>

**Enclosing class:** CatalogFeatures

```java
public static enum
CatalogFeatures.Feature

extends
Enum
<
CatalogFeatures.Feature
>
```

A Feature type as defined in the

Catalog Features table

.

public static enum

CatalogFeatures.Feature

extends

Enum

<

CatalogFeatures.Feature

>

A Feature type as defined in the

Catalog Features table

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DEFER

The

javax.xml.catalog.defer

property as described in
item

DEFER

of the
Catalog Features table.

FILES

The

javax.xml.catalog.files

property as described in
item

FILES

of the
Catalog Features table.

PREFER

The

javax.xml.catalog.prefer

property as described in
item

PREFER

of the
Catalog Features table.

RESOLVE

The

javax.xml.catalog.resolve

property as described in
item

RESOLVE

of the
Catalog Features table.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

defaultValue

()

Returns the default value of the property.

String

getPropertyName

()

Returns the name of the corresponding System Property.

static

CatalogFeatures.Feature

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CatalogFeatures.Feature

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

DEFER

The

javax.xml.catalog.defer

property as described in
item

DEFER

of the
Catalog Features table.

FILES

The

javax.xml.catalog.files

property as described in
item

FILES

of the
Catalog Features table.

PREFER

The

javax.xml.catalog.prefer

property as described in
item

PREFER

of the
Catalog Features table.

RESOLVE

The

javax.xml.catalog.resolve

property as described in
item

RESOLVE

of the
Catalog Features table.

---

#### Enum Constant Summary

The

javax.xml.catalog.defer

property as described in
item

DEFER

of the
Catalog Features table.

The

javax.xml.catalog.files

property as described in
item

FILES

of the
Catalog Features table.

The

javax.xml.catalog.prefer

property as described in
item

PREFER

of the
Catalog Features table.

The

javax.xml.catalog.resolve

property as described in
item

RESOLVE

of the
Catalog Features table.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

defaultValue

()

Returns the default value of the property.

String

getPropertyName

()

Returns the name of the corresponding System Property.

static

CatalogFeatures.Feature

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CatalogFeatures.Feature

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the default value of the property.

Returns the name of the corresponding System Property.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- FILES

```java
public static final
CatalogFeatures.Feature
FILES
```

The

javax.xml.catalog.files

property as described in
item

FILES

of the
Catalog Features table.

- PREFER

```java
public static final
CatalogFeatures.Feature
PREFER
```

The

javax.xml.catalog.prefer

property as described in
item

PREFER

of the
Catalog Features table.

- DEFER

```java
public static final
CatalogFeatures.Feature
DEFER
```

The

javax.xml.catalog.defer

property as described in
item

DEFER

of the
Catalog Features table.

- RESOLVE

```java
public static final
CatalogFeatures.Feature
RESOLVE
```

The

javax.xml.catalog.resolve

property as described in
item

RESOLVE

of the
Catalog Features table.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
CatalogFeatures.Feature
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CatalogFeatures.Feature c : CatalogFeatures.Feature.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CatalogFeatures.Feature
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- getPropertyName

```java
public
String
getPropertyName()
```

Returns the name of the corresponding System Property.

**Returns:** the name of the System Property

- defaultValue

```java
public
String
defaultValue()
```

Returns the default value of the property.

**Returns:** the default value of the property

Enum Constant Detail

- FILES

```java
public static final
CatalogFeatures.Feature
FILES
```

The

javax.xml.catalog.files

property as described in
item

FILES

of the
Catalog Features table.

- PREFER

```java
public static final
CatalogFeatures.Feature
PREFER
```

The

javax.xml.catalog.prefer

property as described in
item

PREFER

of the
Catalog Features table.

- DEFER

```java
public static final
CatalogFeatures.Feature
DEFER
```

The

javax.xml.catalog.defer

property as described in
item

DEFER

of the
Catalog Features table.

- RESOLVE

```java
public static final
CatalogFeatures.Feature
RESOLVE
```

The

javax.xml.catalog.resolve

property as described in
item

RESOLVE

of the
Catalog Features table.

---

#### Enum Constant Detail

FILES

```java
public static final
CatalogFeatures.Feature
FILES
```

The

javax.xml.catalog.files

property as described in
item

FILES

of the
Catalog Features table.

---

#### FILES

public static final

CatalogFeatures.Feature

FILES

The

javax.xml.catalog.files

property as described in
item

FILES

of the
Catalog Features table.

PREFER

```java
public static final
CatalogFeatures.Feature
PREFER
```

The

javax.xml.catalog.prefer

property as described in
item

PREFER

of the
Catalog Features table.

---

#### PREFER

public static final

CatalogFeatures.Feature

PREFER

The

javax.xml.catalog.prefer

property as described in
item

PREFER

of the
Catalog Features table.

DEFER

```java
public static final
CatalogFeatures.Feature
DEFER
```

The

javax.xml.catalog.defer

property as described in
item

DEFER

of the
Catalog Features table.

---

#### DEFER

public static final

CatalogFeatures.Feature

DEFER

The

javax.xml.catalog.defer

property as described in
item

DEFER

of the
Catalog Features table.

RESOLVE

```java
public static final
CatalogFeatures.Feature
RESOLVE
```

The

javax.xml.catalog.resolve

property as described in
item

RESOLVE

of the
Catalog Features table.

---

#### RESOLVE

public static final

CatalogFeatures.Feature

RESOLVE

The

javax.xml.catalog.resolve

property as described in
item

RESOLVE

of the
Catalog Features table.

Method Detail

- values

```java
public static
CatalogFeatures.Feature
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CatalogFeatures.Feature c : CatalogFeatures.Feature.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CatalogFeatures.Feature
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- getPropertyName

```java
public
String
getPropertyName()
```

Returns the name of the corresponding System Property.

**Returns:** the name of the System Property

- defaultValue

```java
public
String
defaultValue()
```

Returns the default value of the property.

**Returns:** the default value of the property

---

#### Method Detail

values

```java
public static
CatalogFeatures.Feature
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CatalogFeatures.Feature c : CatalogFeatures.Feature.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

CatalogFeatures.Feature

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CatalogFeatures.Feature c : CatalogFeatures.Feature.values())
System.out.println(c);
```

for (CatalogFeatures.Feature c : CatalogFeatures.Feature.values())
System.out.println(c);

valueOf

```java
public static
CatalogFeatures.Feature
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

CatalogFeatures.Feature

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

getPropertyName

```java
public
String
getPropertyName()
```

Returns the name of the corresponding System Property.

**Returns:** the name of the System Property

---

#### getPropertyName

public

String

getPropertyName()

Returns the name of the corresponding System Property.

defaultValue

```java
public
String
defaultValue()
```

Returns the default value of the property.

**Returns:** the default value of the property

---

#### defaultValue

public

String

defaultValue()

Returns the default value of the property.

---

