# Enum CardTerminals.State

**Source:** `java.smartcardio\javax\smartcardio\CardTerminals.State.html`

### Class Description

```java
public static enum
CardTerminals.State

extends
Enum
<
CardTerminals.State
>
```

Enumeration of attributes of a CardTerminal.
It is used as a parameter to the

CardTerminals.list()

method.

**All Implemented Interfaces:** Serializable

,

Comparable

<

CardTerminals.State

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
CardTerminals.State
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CardTerminals.State c : CardTerminals.State.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
CardTerminals.State
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

#### Enum CardTerminals.State

java.lang.Object

- java.lang.Enum

<

CardTerminals.State

>
- - javax.smartcardio.CardTerminals.State

java.lang.Enum

<

CardTerminals.State

>

- javax.smartcardio.CardTerminals.State

javax.smartcardio.CardTerminals.State

**All Implemented Interfaces:** Serializable

,

Comparable

<

CardTerminals.State

>

**Enclosing class:** CardTerminals

```java
public static enum
CardTerminals.State

extends
Enum
<
CardTerminals.State
>
```

Enumeration of attributes of a CardTerminal.
It is used as a parameter to the

CardTerminals.list()

method.

**Since:** 1.6

public static enum

CardTerminals.State

extends

Enum

<

CardTerminals.State

>

Enumeration of attributes of a CardTerminal.
It is used as a parameter to the

CardTerminals.list()

method.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ALL

All CardTerminals.

CARD_ABSENT

CardTerminals in which a card is not present.

CARD_INSERTION

CardTerminals for which a card insertion was detected during the
latest call to

waitForChange()

call.

CARD_PRESENT

CardTerminals in which a card is present.

CARD_REMOVAL

CardTerminals for which a card removal was detected during the
latest call to

waitForChange()

call.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CardTerminals.State

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CardTerminals.State

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

ALL

All CardTerminals.

CARD_ABSENT

CardTerminals in which a card is not present.

CARD_INSERTION

CardTerminals for which a card insertion was detected during the
latest call to

waitForChange()

call.

CARD_PRESENT

CardTerminals in which a card is present.

CARD_REMOVAL

CardTerminals for which a card removal was detected during the
latest call to

waitForChange()

call.

---

#### Enum Constant Summary

All CardTerminals.

CardTerminals in which a card is not present.

CardTerminals for which a card insertion was detected during the
latest call to

waitForChange()

call.

CardTerminals in which a card is present.

CardTerminals for which a card removal was detected during the
latest call to

waitForChange()

call.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CardTerminals.State

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

CardTerminals.State

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

- ALL

```java
public static final
CardTerminals.State
ALL
```

All CardTerminals.

- CARD_PRESENT

```java
public static final
CardTerminals.State
CARD_PRESENT
```

CardTerminals in which a card is present.

- CARD_ABSENT

```java
public static final
CardTerminals.State
CARD_ABSENT
```

CardTerminals in which a card is not present.

- CARD_INSERTION

```java
public static final
CardTerminals.State
CARD_INSERTION
```

CardTerminals for which a card insertion was detected during the
latest call to

waitForChange()

call.

- CARD_REMOVAL

```java
public static final
CardTerminals.State
CARD_REMOVAL
```

CardTerminals for which a card removal was detected during the
latest call to

waitForChange()

call.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
CardTerminals.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CardTerminals.State c : CardTerminals.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CardTerminals.State
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

- ALL

```java
public static final
CardTerminals.State
ALL
```

All CardTerminals.

- CARD_PRESENT

```java
public static final
CardTerminals.State
CARD_PRESENT
```

CardTerminals in which a card is present.

- CARD_ABSENT

```java
public static final
CardTerminals.State
CARD_ABSENT
```

CardTerminals in which a card is not present.

- CARD_INSERTION

```java
public static final
CardTerminals.State
CARD_INSERTION
```

CardTerminals for which a card insertion was detected during the
latest call to

waitForChange()

call.

- CARD_REMOVAL

```java
public static final
CardTerminals.State
CARD_REMOVAL
```

CardTerminals for which a card removal was detected during the
latest call to

waitForChange()

call.

---

#### Enum Constant Detail

ALL

```java
public static final
CardTerminals.State
ALL
```

All CardTerminals.

---

#### ALL

public static final

CardTerminals.State

ALL

All CardTerminals.

CARD_PRESENT

```java
public static final
CardTerminals.State
CARD_PRESENT
```

CardTerminals in which a card is present.

---

#### CARD_PRESENT

public static final

CardTerminals.State

CARD_PRESENT

CardTerminals in which a card is present.

CARD_ABSENT

```java
public static final
CardTerminals.State
CARD_ABSENT
```

CardTerminals in which a card is not present.

---

#### CARD_ABSENT

public static final

CardTerminals.State

CARD_ABSENT

CardTerminals in which a card is not present.

CARD_INSERTION

```java
public static final
CardTerminals.State
CARD_INSERTION
```

CardTerminals for which a card insertion was detected during the
latest call to

waitForChange()

call.

---

#### CARD_INSERTION

public static final

CardTerminals.State

CARD_INSERTION

CardTerminals for which a card insertion was detected during the
latest call to

waitForChange()

call.

CARD_REMOVAL

```java
public static final
CardTerminals.State
CARD_REMOVAL
```

CardTerminals for which a card removal was detected during the
latest call to

waitForChange()

call.

---

#### CARD_REMOVAL

public static final

CardTerminals.State

CARD_REMOVAL

CardTerminals for which a card removal was detected during the
latest call to

waitForChange()

call.

Method Detail

- values

```java
public static
CardTerminals.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CardTerminals.State c : CardTerminals.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
CardTerminals.State
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
CardTerminals.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CardTerminals.State c : CardTerminals.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

CardTerminals.State

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (CardTerminals.State c : CardTerminals.State.values())
System.out.println(c);
```

for (CardTerminals.State c : CardTerminals.State.values())
System.out.println(c);

valueOf

```java
public static
CardTerminals.State
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

CardTerminals.State

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

