# Enum Locale.IsoCountryCode

**Source:** `java.base\java\util\Locale.IsoCountryCode.html`

### Class Description

```java
public static enum
Locale.IsoCountryCode

extends
Enum
<
Locale.IsoCountryCode
>
```

Enum for specifying the type defined in ISO 3166. This enum is used to
retrieve the two-letter ISO3166-1 alpha-2, three-letter ISO3166-1
alpha-3, four-letter ISO3166-3 country codes.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Locale.IsoCountryCode

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Locale.IsoCountryCode
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.IsoCountryCode c : Locale.IsoCountryCode.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Locale.IsoCountryCode
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

### Additional Sections

#### Enum Locale.IsoCountryCode

java.lang.Object

- java.lang.Enum

<

Locale.IsoCountryCode

>
- - java.util.Locale.IsoCountryCode

java.lang.Enum

<

Locale.IsoCountryCode

>

- java.util.Locale.IsoCountryCode

java.util.Locale.IsoCountryCode

**All Implemented Interfaces:** Serializable

,

Comparable

<

Locale.IsoCountryCode

>

**Enclosing class:** Locale

```java
public static enum
Locale.IsoCountryCode

extends
Enum
<
Locale.IsoCountryCode
>
```

Enum for specifying the type defined in ISO 3166. This enum is used to
retrieve the two-letter ISO3166-1 alpha-2, three-letter ISO3166-1
alpha-3, four-letter ISO3166-3 country codes.

**Since:** 9
**See Also:** Locale.getISOCountries(Locale.IsoCountryCode)

public static enum

Locale.IsoCountryCode

extends

Enum

<

Locale.IsoCountryCode

>

Enum for specifying the type defined in ISO 3166. This enum is used to
retrieve the two-letter ISO3166-1 alpha-2, three-letter ISO3166-1
alpha-3, four-letter ISO3166-3 country codes.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

PART1_ALPHA2

PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
country codes.

PART1_ALPHA3

PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
country codes.

PART3

PART3 is used to represent the ISO3166-3 four letter country codes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Locale.IsoCountryCode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Locale.IsoCountryCode

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

PART1_ALPHA2

PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
country codes.

PART1_ALPHA3

PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
country codes.

PART3

PART3 is used to represent the ISO3166-3 four letter country codes.

---

#### Enum Constant Summary

PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
country codes.

PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
country codes.

PART3 is used to represent the ISO3166-3 four letter country codes.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Locale.IsoCountryCode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Locale.IsoCountryCode

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

- PART1_ALPHA2

```java
public static final
Locale.IsoCountryCode
PART1_ALPHA2
```

PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
country codes.

- PART1_ALPHA3

```java
public static final
Locale.IsoCountryCode
PART1_ALPHA3
```

PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
country codes.

- PART3

```java
public static final
Locale.IsoCountryCode
PART3
```

PART3 is used to represent the ISO3166-3 four letter country codes.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Locale.IsoCountryCode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.IsoCountryCode c : Locale.IsoCountryCode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Locale.IsoCountryCode
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

Enum Constant Detail

- PART1_ALPHA2

```java
public static final
Locale.IsoCountryCode
PART1_ALPHA2
```

PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
country codes.

- PART1_ALPHA3

```java
public static final
Locale.IsoCountryCode
PART1_ALPHA3
```

PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
country codes.

- PART3

```java
public static final
Locale.IsoCountryCode
PART3
```

PART3 is used to represent the ISO3166-3 four letter country codes.

---

#### Enum Constant Detail

PART1_ALPHA2

```java
public static final
Locale.IsoCountryCode
PART1_ALPHA2
```

PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
country codes.

---

#### PART1_ALPHA2

public static final

Locale.IsoCountryCode

PART1_ALPHA2

PART1_ALPHA2 is used to represent the ISO3166-1 alpha-2 two letter
country codes.

PART1_ALPHA3

```java
public static final
Locale.IsoCountryCode
PART1_ALPHA3
```

PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
country codes.

---

#### PART1_ALPHA3

public static final

Locale.IsoCountryCode

PART1_ALPHA3

PART1_ALPHA3 is used to represent the ISO3166-1 alpha-3 three letter
country codes.

PART3

```java
public static final
Locale.IsoCountryCode
PART3
```

PART3 is used to represent the ISO3166-3 four letter country codes.

---

#### PART3

public static final

Locale.IsoCountryCode

PART3

PART3 is used to represent the ISO3166-3 four letter country codes.

Method Detail

- values

```java
public static
Locale.IsoCountryCode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.IsoCountryCode c : Locale.IsoCountryCode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Locale.IsoCountryCode
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

#### Method Detail

values

```java
public static
Locale.IsoCountryCode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.IsoCountryCode c : Locale.IsoCountryCode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Locale.IsoCountryCode

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.IsoCountryCode c : Locale.IsoCountryCode.values())
System.out.println(c);
```

for (Locale.IsoCountryCode c : Locale.IsoCountryCode.values())
System.out.println(c);

valueOf

```java
public static
Locale.IsoCountryCode
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

Locale.IsoCountryCode

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

