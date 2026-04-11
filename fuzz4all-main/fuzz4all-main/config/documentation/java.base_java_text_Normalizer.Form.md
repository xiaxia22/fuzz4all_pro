# Enum Normalizer.Form

**Source:** `java.base\java\text\Normalizer.Form.html`

### Class Description

```java
public static enum
Normalizer.Form

extends
Enum
<
Normalizer.Form
>
```

This enum provides constants of the four Unicode normalization forms
that are described in

Unicode Standard Annex #15 — Unicode Normalization Forms

and two methods to access them.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Normalizer.Form

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Normalizer.Form
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Normalizer.Form c : Normalizer.Form.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Normalizer.Form
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

#### Enum Normalizer.Form

java.lang.Object

- java.lang.Enum

<

Normalizer.Form

>
- - java.text.Normalizer.Form

java.lang.Enum

<

Normalizer.Form

>

- java.text.Normalizer.Form

java.text.Normalizer.Form

**All Implemented Interfaces:** Serializable

,

Comparable

<

Normalizer.Form

>

**Enclosing class:** Normalizer

```java
public static enum
Normalizer.Form

extends
Enum
<
Normalizer.Form
>
```

This enum provides constants of the four Unicode normalization forms
that are described in

Unicode Standard Annex #15 — Unicode Normalization Forms

and two methods to access them.

**Since:** 1.6

public static enum

Normalizer.Form

extends

Enum

<

Normalizer.Form

>

This enum provides constants of the four Unicode normalization forms
that are described in

Unicode Standard Annex #15 — Unicode Normalization Forms

and two methods to access them.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

NFC

Canonical decomposition, followed by canonical composition.

NFD

Canonical decomposition.

NFKC

Compatibility decomposition, followed by canonical composition.

NFKD

Compatibility decomposition.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Normalizer.Form

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Normalizer.Form

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

NFC

Canonical decomposition, followed by canonical composition.

NFD

Canonical decomposition.

NFKC

Compatibility decomposition, followed by canonical composition.

NFKD

Compatibility decomposition.

---

#### Enum Constant Summary

Canonical decomposition, followed by canonical composition.

Canonical decomposition.

Compatibility decomposition, followed by canonical composition.

Compatibility decomposition.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Normalizer.Form

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Normalizer.Form

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

- NFD

```java
public static final
Normalizer.Form
NFD
```

Canonical decomposition.

- NFC

```java
public static final
Normalizer.Form
NFC
```

Canonical decomposition, followed by canonical composition.

- NFKD

```java
public static final
Normalizer.Form
NFKD
```

Compatibility decomposition.

- NFKC

```java
public static final
Normalizer.Form
NFKC
```

Compatibility decomposition, followed by canonical composition.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Normalizer.Form
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Normalizer.Form c : Normalizer.Form.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Normalizer.Form
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

- NFD

```java
public static final
Normalizer.Form
NFD
```

Canonical decomposition.

- NFC

```java
public static final
Normalizer.Form
NFC
```

Canonical decomposition, followed by canonical composition.

- NFKD

```java
public static final
Normalizer.Form
NFKD
```

Compatibility decomposition.

- NFKC

```java
public static final
Normalizer.Form
NFKC
```

Compatibility decomposition, followed by canonical composition.

---

#### Enum Constant Detail

NFD

```java
public static final
Normalizer.Form
NFD
```

Canonical decomposition.

---

#### NFD

public static final

Normalizer.Form

NFD

Canonical decomposition.

NFC

```java
public static final
Normalizer.Form
NFC
```

Canonical decomposition, followed by canonical composition.

---

#### NFC

public static final

Normalizer.Form

NFC

Canonical decomposition, followed by canonical composition.

NFKD

```java
public static final
Normalizer.Form
NFKD
```

Compatibility decomposition.

---

#### NFKD

public static final

Normalizer.Form

NFKD

Compatibility decomposition.

NFKC

```java
public static final
Normalizer.Form
NFKC
```

Compatibility decomposition, followed by canonical composition.

---

#### NFKC

public static final

Normalizer.Form

NFKC

Compatibility decomposition, followed by canonical composition.

Method Detail

- values

```java
public static
Normalizer.Form
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Normalizer.Form c : Normalizer.Form.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Normalizer.Form
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
Normalizer.Form
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Normalizer.Form c : Normalizer.Form.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Normalizer.Form

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Normalizer.Form c : Normalizer.Form.values())
System.out.println(c);
```

for (Normalizer.Form c : Normalizer.Form.values())
System.out.println(c);

valueOf

```java
public static
Normalizer.Form
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

Normalizer.Form

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

