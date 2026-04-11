# Enum NumericShaper.Range

**Source:** `java.desktop\java\awt\font\NumericShaper.Range.html`

### Class Description

```java
public static enum
NumericShaper.Range

extends
Enum
<
NumericShaper.Range
>
```

A

NumericShaper.Range

represents a Unicode range of a
script having its own decimal digits. For example, the

THAI

range has the Thai digits, THAI DIGIT
ZERO (U+0E50) to THAI DIGIT NINE (U+0E59).

The

Range

enum replaces the traditional bit
mask-based values (e.g.,

NumericShaper.ARABIC

), and
supports more Unicode ranges than the bit mask-based ones. For
example, the following code using the bit mask:

```java
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
```

can be written using this enum as:

```java
NumericShaper.getContextualShaper(EnumSet.of(
NumericShaper.Range.ARABIC,
NumericShaper.Range.TAMIL),
NumericShaper.Range.EUROPEAN);
```

**All Implemented Interfaces:** Serializable

,

Comparable

<

NumericShaper.Range

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
NumericShaper.Range
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NumericShaper.Range c : NumericShaper.Range.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
NumericShaper.Range
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

#### Enum NumericShaper.Range

java.lang.Object

- java.lang.Enum

<

NumericShaper.Range

>
- - java.awt.font.NumericShaper.Range

java.lang.Enum

<

NumericShaper.Range

>

- java.awt.font.NumericShaper.Range

java.awt.font.NumericShaper.Range

**All Implemented Interfaces:** Serializable

,

Comparable

<

NumericShaper.Range

>

**Enclosing class:** NumericShaper

```java
public static enum
NumericShaper.Range

extends
Enum
<
NumericShaper.Range
>
```

A

NumericShaper.Range

represents a Unicode range of a
script having its own decimal digits. For example, the

THAI

range has the Thai digits, THAI DIGIT
ZERO (U+0E50) to THAI DIGIT NINE (U+0E59).

The

Range

enum replaces the traditional bit
mask-based values (e.g.,

NumericShaper.ARABIC

), and
supports more Unicode ranges than the bit mask-based ones. For
example, the following code using the bit mask:

```java
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
```

can be written using this enum as:

```java
NumericShaper.getContextualShaper(EnumSet.of(
NumericShaper.Range.ARABIC,
NumericShaper.Range.TAMIL),
NumericShaper.Range.EUROPEAN);
```

**Since:** 1.7

public static enum

NumericShaper.Range

extends

Enum

<

NumericShaper.Range

>

A

NumericShaper.Range

represents a Unicode range of a
script having its own decimal digits. For example, the

THAI

range has the Thai digits, THAI DIGIT
ZERO (U+0E50) to THAI DIGIT NINE (U+0E59).

The

Range

enum replaces the traditional bit
mask-based values (e.g.,

NumericShaper.ARABIC

), and
supports more Unicode ranges than the bit mask-based ones. For
example, the following code using the bit mask:

```java
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
```

can be written using this enum as:

```java
NumericShaper.getContextualShaper(EnumSet.of(
NumericShaper.Range.ARABIC,
NumericShaper.Range.TAMIL),
NumericShaper.Range.EUROPEAN);
```

The

Range

enum replaces the traditional bit
mask-based values (e.g.,

NumericShaper.ARABIC

), and
supports more Unicode ranges than the bit mask-based ones. For
example, the following code using the bit mask:

```java
NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);
```

can be written using this enum as:

```java
NumericShaper.getContextualShaper(EnumSet.of(
NumericShaper.Range.ARABIC,
NumericShaper.Range.TAMIL),
NumericShaper.Range.EUROPEAN);
```

NumericShaper.getContextualShaper(NumericShaper.ARABIC |
NumericShaper.TAMIL,
NumericShaper.EUROPEAN);

NumericShaper.getContextualShaper(EnumSet.of(
NumericShaper.Range.ARABIC,
NumericShaper.Range.TAMIL),
NumericShaper.Range.EUROPEAN);

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ARABIC

The Arabic range with the Arabic-Indic digits.

BALINESE

The Balinese range with the Balinese digits.

BENGALI

The Bengali range with the Bengali digits.

CHAM

The Cham range with the Cham digits.

DEVANAGARI

The Devanagari range with the Devanagari digits.

EASTERN_ARABIC

The Arabic range with the Eastern Arabic-Indic digits.

ETHIOPIC

The Ethiopic range with the Ethiopic digits.

EUROPEAN

The Latin (European) range with the Latin (ASCII) digits.

GUJARATI

The Gujarati range with the Gujarati digits.

GURMUKHI

The Gurmukhi range with the Gurmukhi digits.

JAVANESE

The Javanese range with the Javanese digits.

KANNADA

The Kannada range with the Kannada digits.

KAYAH_LI

The Kayah Li range with the Kayah Li digits.

KHMER

The Khmer range with the Khmer digits.

LAO

The Lao range with the Lao digits.

LEPCHA

The Lepcha range with the Lepcha digits.

LIMBU

The Limbu range with the Limbu digits.

MALAYALAM

The Malayalam range with the Malayalam digits.

MEETEI_MAYEK

The Meetei Mayek range with the Meetei Mayek digits.

MONGOLIAN

The Mongolian range with the Mongolian digits.

MYANMAR

The Myanmar range with the Myanmar digits.

MYANMAR_SHAN

The Myanmar range with the Myanmar Shan digits.

MYANMAR_TAI_LAING

The Myanmar Extended-B range with the Myanmar Tai Laing digits.

NEW_TAI_LUE

The New Tai Lue range with the New Tai Lue digits.

NKO

The N'Ko range with the N'Ko digits.

OL_CHIKI

The Ol Chiki range with the Ol Chiki digits.

ORIYA

The Oriya range with the Oriya digits.

SAURASHTRA

The Saurashtra range with the Saurashtra digits.

SINHALA

The Sinhala range with the Sinhala digits.

SUNDANESE

The Sundanese range with the Sundanese digits.

TAI_THAM_HORA

The Tai Tham Hora range with the Tai Tham Hora digits.

TAI_THAM_THAM

The Tai Tham Tham range with the Tai Tham Tham digits.

TAMIL

The Tamil range with the Tamil digits.

TELUGU

The Telugu range with the Telugu digits.

THAI

The Thai range with the Thai digits.

TIBETAN

The Tibetan range with the Tibetan digits.

VAI

The Vai range with the Vai digits.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

NumericShaper.Range

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

NumericShaper.Range

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

ARABIC

The Arabic range with the Arabic-Indic digits.

BALINESE

The Balinese range with the Balinese digits.

BENGALI

The Bengali range with the Bengali digits.

CHAM

The Cham range with the Cham digits.

DEVANAGARI

The Devanagari range with the Devanagari digits.

EASTERN_ARABIC

The Arabic range with the Eastern Arabic-Indic digits.

ETHIOPIC

The Ethiopic range with the Ethiopic digits.

EUROPEAN

The Latin (European) range with the Latin (ASCII) digits.

GUJARATI

The Gujarati range with the Gujarati digits.

GURMUKHI

The Gurmukhi range with the Gurmukhi digits.

JAVANESE

The Javanese range with the Javanese digits.

KANNADA

The Kannada range with the Kannada digits.

KAYAH_LI

The Kayah Li range with the Kayah Li digits.

KHMER

The Khmer range with the Khmer digits.

LAO

The Lao range with the Lao digits.

LEPCHA

The Lepcha range with the Lepcha digits.

LIMBU

The Limbu range with the Limbu digits.

MALAYALAM

The Malayalam range with the Malayalam digits.

MEETEI_MAYEK

The Meetei Mayek range with the Meetei Mayek digits.

MONGOLIAN

The Mongolian range with the Mongolian digits.

MYANMAR

The Myanmar range with the Myanmar digits.

MYANMAR_SHAN

The Myanmar range with the Myanmar Shan digits.

MYANMAR_TAI_LAING

The Myanmar Extended-B range with the Myanmar Tai Laing digits.

NEW_TAI_LUE

The New Tai Lue range with the New Tai Lue digits.

NKO

The N'Ko range with the N'Ko digits.

OL_CHIKI

The Ol Chiki range with the Ol Chiki digits.

ORIYA

The Oriya range with the Oriya digits.

SAURASHTRA

The Saurashtra range with the Saurashtra digits.

SINHALA

The Sinhala range with the Sinhala digits.

SUNDANESE

The Sundanese range with the Sundanese digits.

TAI_THAM_HORA

The Tai Tham Hora range with the Tai Tham Hora digits.

TAI_THAM_THAM

The Tai Tham Tham range with the Tai Tham Tham digits.

TAMIL

The Tamil range with the Tamil digits.

TELUGU

The Telugu range with the Telugu digits.

THAI

The Thai range with the Thai digits.

TIBETAN

The Tibetan range with the Tibetan digits.

VAI

The Vai range with the Vai digits.

---

#### Enum Constant Summary

The Arabic range with the Arabic-Indic digits.

The Balinese range with the Balinese digits.

The Bengali range with the Bengali digits.

The Cham range with the Cham digits.

The Devanagari range with the Devanagari digits.

The Arabic range with the Eastern Arabic-Indic digits.

The Ethiopic range with the Ethiopic digits.

The Latin (European) range with the Latin (ASCII) digits.

The Gujarati range with the Gujarati digits.

The Gurmukhi range with the Gurmukhi digits.

The Javanese range with the Javanese digits.

The Kannada range with the Kannada digits.

The Kayah Li range with the Kayah Li digits.

The Khmer range with the Khmer digits.

The Lao range with the Lao digits.

The Lepcha range with the Lepcha digits.

The Limbu range with the Limbu digits.

The Malayalam range with the Malayalam digits.

The Meetei Mayek range with the Meetei Mayek digits.

The Mongolian range with the Mongolian digits.

The Myanmar range with the Myanmar digits.

The Myanmar range with the Myanmar Shan digits.

The Myanmar Extended-B range with the Myanmar Tai Laing digits.

The New Tai Lue range with the New Tai Lue digits.

The N'Ko range with the N'Ko digits.

The Ol Chiki range with the Ol Chiki digits.

The Oriya range with the Oriya digits.

The Saurashtra range with the Saurashtra digits.

The Sinhala range with the Sinhala digits.

The Sundanese range with the Sundanese digits.

The Tai Tham Hora range with the Tai Tham Hora digits.

The Tai Tham Tham range with the Tai Tham Tham digits.

The Tamil range with the Tamil digits.

The Telugu range with the Telugu digits.

The Thai range with the Thai digits.

The Tibetan range with the Tibetan digits.

The Vai range with the Vai digits.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

NumericShaper.Range

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

NumericShaper.Range

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

- EUROPEAN

```java
public static final
NumericShaper.Range
EUROPEAN
```

The Latin (European) range with the Latin (ASCII) digits.

- ARABIC

```java
public static final
NumericShaper.Range
ARABIC
```

The Arabic range with the Arabic-Indic digits.

- EASTERN_ARABIC

```java
public static final
NumericShaper.Range
EASTERN_ARABIC
```

The Arabic range with the Eastern Arabic-Indic digits.

- DEVANAGARI

```java
public static final
NumericShaper.Range
DEVANAGARI
```

The Devanagari range with the Devanagari digits.

- BENGALI

```java
public static final
NumericShaper.Range
BENGALI
```

The Bengali range with the Bengali digits.

- GURMUKHI

```java
public static final
NumericShaper.Range
GURMUKHI
```

The Gurmukhi range with the Gurmukhi digits.

- GUJARATI

```java
public static final
NumericShaper.Range
GUJARATI
```

The Gujarati range with the Gujarati digits.

- ORIYA

```java
public static final
NumericShaper.Range
ORIYA
```

The Oriya range with the Oriya digits.

- TAMIL

```java
public static final
NumericShaper.Range
TAMIL
```

The Tamil range with the Tamil digits.

- TELUGU

```java
public static final
NumericShaper.Range
TELUGU
```

The Telugu range with the Telugu digits.

- KANNADA

```java
public static final
NumericShaper.Range
KANNADA
```

The Kannada range with the Kannada digits.

- MALAYALAM

```java
public static final
NumericShaper.Range
MALAYALAM
```

The Malayalam range with the Malayalam digits.

- THAI

```java
public static final
NumericShaper.Range
THAI
```

The Thai range with the Thai digits.

- LAO

```java
public static final
NumericShaper.Range
LAO
```

The Lao range with the Lao digits.

- TIBETAN

```java
public static final
NumericShaper.Range
TIBETAN
```

The Tibetan range with the Tibetan digits.

- MYANMAR

```java
public static final
NumericShaper.Range
MYANMAR
```

The Myanmar range with the Myanmar digits.

- ETHIOPIC

```java
public static final
NumericShaper.Range
ETHIOPIC
```

The Ethiopic range with the Ethiopic digits. Ethiopic
does not have a decimal digit 0 so Latin (European) 0 is
used.

- KHMER

```java
public static final
NumericShaper.Range
KHMER
```

The Khmer range with the Khmer digits.

- MONGOLIAN

```java
public static final
NumericShaper.Range
MONGOLIAN
```

The Mongolian range with the Mongolian digits.

- NKO

```java
public static final
NumericShaper.Range
NKO
```

The N'Ko range with the N'Ko digits.

- MYANMAR_SHAN

```java
public static final
NumericShaper.Range
MYANMAR_SHAN
```

The Myanmar range with the Myanmar Shan digits.

- LIMBU

```java
public static final
NumericShaper.Range
LIMBU
```

The Limbu range with the Limbu digits.

- NEW_TAI_LUE

```java
public static final
NumericShaper.Range
NEW_TAI_LUE
```

The New Tai Lue range with the New Tai Lue digits.

- BALINESE

```java
public static final
NumericShaper.Range
BALINESE
```

The Balinese range with the Balinese digits.

- SUNDANESE

```java
public static final
NumericShaper.Range
SUNDANESE
```

The Sundanese range with the Sundanese digits.

- LEPCHA

```java
public static final
NumericShaper.Range
LEPCHA
```

The Lepcha range with the Lepcha digits.

- OL_CHIKI

```java
public static final
NumericShaper.Range
OL_CHIKI
```

The Ol Chiki range with the Ol Chiki digits.

- VAI

```java
public static final
NumericShaper.Range
VAI
```

The Vai range with the Vai digits.

- SAURASHTRA

```java
public static final
NumericShaper.Range
SAURASHTRA
```

The Saurashtra range with the Saurashtra digits.

- KAYAH_LI

```java
public static final
NumericShaper.Range
KAYAH_LI
```

The Kayah Li range with the Kayah Li digits.

- CHAM

```java
public static final
NumericShaper.Range
CHAM
```

The Cham range with the Cham digits.

- TAI_THAM_HORA

```java
public static final
NumericShaper.Range
TAI_THAM_HORA
```

The Tai Tham Hora range with the Tai Tham Hora digits.

- TAI_THAM_THAM

```java
public static final
NumericShaper.Range
TAI_THAM_THAM
```

The Tai Tham Tham range with the Tai Tham Tham digits.

- JAVANESE

```java
public static final
NumericShaper.Range
JAVANESE
```

The Javanese range with the Javanese digits.

- MEETEI_MAYEK

```java
public static final
NumericShaper.Range
MEETEI_MAYEK
```

The Meetei Mayek range with the Meetei Mayek digits.

- SINHALA

```java
public static final
NumericShaper.Range
SINHALA
```

The Sinhala range with the Sinhala digits.

**Since:** 9

- MYANMAR_TAI_LAING

```java
public static final
NumericShaper.Range
MYANMAR_TAI_LAING
```

The Myanmar Extended-B range with the Myanmar Tai Laing digits.

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
NumericShaper.Range
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NumericShaper.Range c : NumericShaper.Range.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
NumericShaper.Range
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

- EUROPEAN

```java
public static final
NumericShaper.Range
EUROPEAN
```

The Latin (European) range with the Latin (ASCII) digits.

- ARABIC

```java
public static final
NumericShaper.Range
ARABIC
```

The Arabic range with the Arabic-Indic digits.

- EASTERN_ARABIC

```java
public static final
NumericShaper.Range
EASTERN_ARABIC
```

The Arabic range with the Eastern Arabic-Indic digits.

- DEVANAGARI

```java
public static final
NumericShaper.Range
DEVANAGARI
```

The Devanagari range with the Devanagari digits.

- BENGALI

```java
public static final
NumericShaper.Range
BENGALI
```

The Bengali range with the Bengali digits.

- GURMUKHI

```java
public static final
NumericShaper.Range
GURMUKHI
```

The Gurmukhi range with the Gurmukhi digits.

- GUJARATI

```java
public static final
NumericShaper.Range
GUJARATI
```

The Gujarati range with the Gujarati digits.

- ORIYA

```java
public static final
NumericShaper.Range
ORIYA
```

The Oriya range with the Oriya digits.

- TAMIL

```java
public static final
NumericShaper.Range
TAMIL
```

The Tamil range with the Tamil digits.

- TELUGU

```java
public static final
NumericShaper.Range
TELUGU
```

The Telugu range with the Telugu digits.

- KANNADA

```java
public static final
NumericShaper.Range
KANNADA
```

The Kannada range with the Kannada digits.

- MALAYALAM

```java
public static final
NumericShaper.Range
MALAYALAM
```

The Malayalam range with the Malayalam digits.

- THAI

```java
public static final
NumericShaper.Range
THAI
```

The Thai range with the Thai digits.

- LAO

```java
public static final
NumericShaper.Range
LAO
```

The Lao range with the Lao digits.

- TIBETAN

```java
public static final
NumericShaper.Range
TIBETAN
```

The Tibetan range with the Tibetan digits.

- MYANMAR

```java
public static final
NumericShaper.Range
MYANMAR
```

The Myanmar range with the Myanmar digits.

- ETHIOPIC

```java
public static final
NumericShaper.Range
ETHIOPIC
```

The Ethiopic range with the Ethiopic digits. Ethiopic
does not have a decimal digit 0 so Latin (European) 0 is
used.

- KHMER

```java
public static final
NumericShaper.Range
KHMER
```

The Khmer range with the Khmer digits.

- MONGOLIAN

```java
public static final
NumericShaper.Range
MONGOLIAN
```

The Mongolian range with the Mongolian digits.

- NKO

```java
public static final
NumericShaper.Range
NKO
```

The N'Ko range with the N'Ko digits.

- MYANMAR_SHAN

```java
public static final
NumericShaper.Range
MYANMAR_SHAN
```

The Myanmar range with the Myanmar Shan digits.

- LIMBU

```java
public static final
NumericShaper.Range
LIMBU
```

The Limbu range with the Limbu digits.

- NEW_TAI_LUE

```java
public static final
NumericShaper.Range
NEW_TAI_LUE
```

The New Tai Lue range with the New Tai Lue digits.

- BALINESE

```java
public static final
NumericShaper.Range
BALINESE
```

The Balinese range with the Balinese digits.

- SUNDANESE

```java
public static final
NumericShaper.Range
SUNDANESE
```

The Sundanese range with the Sundanese digits.

- LEPCHA

```java
public static final
NumericShaper.Range
LEPCHA
```

The Lepcha range with the Lepcha digits.

- OL_CHIKI

```java
public static final
NumericShaper.Range
OL_CHIKI
```

The Ol Chiki range with the Ol Chiki digits.

- VAI

```java
public static final
NumericShaper.Range
VAI
```

The Vai range with the Vai digits.

- SAURASHTRA

```java
public static final
NumericShaper.Range
SAURASHTRA
```

The Saurashtra range with the Saurashtra digits.

- KAYAH_LI

```java
public static final
NumericShaper.Range
KAYAH_LI
```

The Kayah Li range with the Kayah Li digits.

- CHAM

```java
public static final
NumericShaper.Range
CHAM
```

The Cham range with the Cham digits.

- TAI_THAM_HORA

```java
public static final
NumericShaper.Range
TAI_THAM_HORA
```

The Tai Tham Hora range with the Tai Tham Hora digits.

- TAI_THAM_THAM

```java
public static final
NumericShaper.Range
TAI_THAM_THAM
```

The Tai Tham Tham range with the Tai Tham Tham digits.

- JAVANESE

```java
public static final
NumericShaper.Range
JAVANESE
```

The Javanese range with the Javanese digits.

- MEETEI_MAYEK

```java
public static final
NumericShaper.Range
MEETEI_MAYEK
```

The Meetei Mayek range with the Meetei Mayek digits.

- SINHALA

```java
public static final
NumericShaper.Range
SINHALA
```

The Sinhala range with the Sinhala digits.

**Since:** 9

- MYANMAR_TAI_LAING

```java
public static final
NumericShaper.Range
MYANMAR_TAI_LAING
```

The Myanmar Extended-B range with the Myanmar Tai Laing digits.

**Since:** 9

---

#### Enum Constant Detail

EUROPEAN

```java
public static final
NumericShaper.Range
EUROPEAN
```

The Latin (European) range with the Latin (ASCII) digits.

---

#### EUROPEAN

public static final

NumericShaper.Range

EUROPEAN

The Latin (European) range with the Latin (ASCII) digits.

ARABIC

```java
public static final
NumericShaper.Range
ARABIC
```

The Arabic range with the Arabic-Indic digits.

---

#### ARABIC

public static final

NumericShaper.Range

ARABIC

The Arabic range with the Arabic-Indic digits.

EASTERN_ARABIC

```java
public static final
NumericShaper.Range
EASTERN_ARABIC
```

The Arabic range with the Eastern Arabic-Indic digits.

---

#### EASTERN_ARABIC

public static final

NumericShaper.Range

EASTERN_ARABIC

The Arabic range with the Eastern Arabic-Indic digits.

DEVANAGARI

```java
public static final
NumericShaper.Range
DEVANAGARI
```

The Devanagari range with the Devanagari digits.

---

#### DEVANAGARI

public static final

NumericShaper.Range

DEVANAGARI

The Devanagari range with the Devanagari digits.

BENGALI

```java
public static final
NumericShaper.Range
BENGALI
```

The Bengali range with the Bengali digits.

---

#### BENGALI

public static final

NumericShaper.Range

BENGALI

The Bengali range with the Bengali digits.

GURMUKHI

```java
public static final
NumericShaper.Range
GURMUKHI
```

The Gurmukhi range with the Gurmukhi digits.

---

#### GURMUKHI

public static final

NumericShaper.Range

GURMUKHI

The Gurmukhi range with the Gurmukhi digits.

GUJARATI

```java
public static final
NumericShaper.Range
GUJARATI
```

The Gujarati range with the Gujarati digits.

---

#### GUJARATI

public static final

NumericShaper.Range

GUJARATI

The Gujarati range with the Gujarati digits.

ORIYA

```java
public static final
NumericShaper.Range
ORIYA
```

The Oriya range with the Oriya digits.

---

#### ORIYA

public static final

NumericShaper.Range

ORIYA

The Oriya range with the Oriya digits.

TAMIL

```java
public static final
NumericShaper.Range
TAMIL
```

The Tamil range with the Tamil digits.

---

#### TAMIL

public static final

NumericShaper.Range

TAMIL

The Tamil range with the Tamil digits.

TELUGU

```java
public static final
NumericShaper.Range
TELUGU
```

The Telugu range with the Telugu digits.

---

#### TELUGU

public static final

NumericShaper.Range

TELUGU

The Telugu range with the Telugu digits.

KANNADA

```java
public static final
NumericShaper.Range
KANNADA
```

The Kannada range with the Kannada digits.

---

#### KANNADA

public static final

NumericShaper.Range

KANNADA

The Kannada range with the Kannada digits.

MALAYALAM

```java
public static final
NumericShaper.Range
MALAYALAM
```

The Malayalam range with the Malayalam digits.

---

#### MALAYALAM

public static final

NumericShaper.Range

MALAYALAM

The Malayalam range with the Malayalam digits.

THAI

```java
public static final
NumericShaper.Range
THAI
```

The Thai range with the Thai digits.

---

#### THAI

public static final

NumericShaper.Range

THAI

The Thai range with the Thai digits.

LAO

```java
public static final
NumericShaper.Range
LAO
```

The Lao range with the Lao digits.

---

#### LAO

public static final

NumericShaper.Range

LAO

The Lao range with the Lao digits.

TIBETAN

```java
public static final
NumericShaper.Range
TIBETAN
```

The Tibetan range with the Tibetan digits.

---

#### TIBETAN

public static final

NumericShaper.Range

TIBETAN

The Tibetan range with the Tibetan digits.

MYANMAR

```java
public static final
NumericShaper.Range
MYANMAR
```

The Myanmar range with the Myanmar digits.

---

#### MYANMAR

public static final

NumericShaper.Range

MYANMAR

The Myanmar range with the Myanmar digits.

ETHIOPIC

```java
public static final
NumericShaper.Range
ETHIOPIC
```

The Ethiopic range with the Ethiopic digits. Ethiopic
does not have a decimal digit 0 so Latin (European) 0 is
used.

---

#### ETHIOPIC

public static final

NumericShaper.Range

ETHIOPIC

The Ethiopic range with the Ethiopic digits. Ethiopic
does not have a decimal digit 0 so Latin (European) 0 is
used.

KHMER

```java
public static final
NumericShaper.Range
KHMER
```

The Khmer range with the Khmer digits.

---

#### KHMER

public static final

NumericShaper.Range

KHMER

The Khmer range with the Khmer digits.

MONGOLIAN

```java
public static final
NumericShaper.Range
MONGOLIAN
```

The Mongolian range with the Mongolian digits.

---

#### MONGOLIAN

public static final

NumericShaper.Range

MONGOLIAN

The Mongolian range with the Mongolian digits.

NKO

```java
public static final
NumericShaper.Range
NKO
```

The N'Ko range with the N'Ko digits.

---

#### NKO

public static final

NumericShaper.Range

NKO

The N'Ko range with the N'Ko digits.

MYANMAR_SHAN

```java
public static final
NumericShaper.Range
MYANMAR_SHAN
```

The Myanmar range with the Myanmar Shan digits.

---

#### MYANMAR_SHAN

public static final

NumericShaper.Range

MYANMAR_SHAN

The Myanmar range with the Myanmar Shan digits.

LIMBU

```java
public static final
NumericShaper.Range
LIMBU
```

The Limbu range with the Limbu digits.

---

#### LIMBU

public static final

NumericShaper.Range

LIMBU

The Limbu range with the Limbu digits.

NEW_TAI_LUE

```java
public static final
NumericShaper.Range
NEW_TAI_LUE
```

The New Tai Lue range with the New Tai Lue digits.

---

#### NEW_TAI_LUE

public static final

NumericShaper.Range

NEW_TAI_LUE

The New Tai Lue range with the New Tai Lue digits.

BALINESE

```java
public static final
NumericShaper.Range
BALINESE
```

The Balinese range with the Balinese digits.

---

#### BALINESE

public static final

NumericShaper.Range

BALINESE

The Balinese range with the Balinese digits.

SUNDANESE

```java
public static final
NumericShaper.Range
SUNDANESE
```

The Sundanese range with the Sundanese digits.

---

#### SUNDANESE

public static final

NumericShaper.Range

SUNDANESE

The Sundanese range with the Sundanese digits.

LEPCHA

```java
public static final
NumericShaper.Range
LEPCHA
```

The Lepcha range with the Lepcha digits.

---

#### LEPCHA

public static final

NumericShaper.Range

LEPCHA

The Lepcha range with the Lepcha digits.

OL_CHIKI

```java
public static final
NumericShaper.Range
OL_CHIKI
```

The Ol Chiki range with the Ol Chiki digits.

---

#### OL_CHIKI

public static final

NumericShaper.Range

OL_CHIKI

The Ol Chiki range with the Ol Chiki digits.

VAI

```java
public static final
NumericShaper.Range
VAI
```

The Vai range with the Vai digits.

---

#### VAI

public static final

NumericShaper.Range

VAI

The Vai range with the Vai digits.

SAURASHTRA

```java
public static final
NumericShaper.Range
SAURASHTRA
```

The Saurashtra range with the Saurashtra digits.

---

#### SAURASHTRA

public static final

NumericShaper.Range

SAURASHTRA

The Saurashtra range with the Saurashtra digits.

KAYAH_LI

```java
public static final
NumericShaper.Range
KAYAH_LI
```

The Kayah Li range with the Kayah Li digits.

---

#### KAYAH_LI

public static final

NumericShaper.Range

KAYAH_LI

The Kayah Li range with the Kayah Li digits.

CHAM

```java
public static final
NumericShaper.Range
CHAM
```

The Cham range with the Cham digits.

---

#### CHAM

public static final

NumericShaper.Range

CHAM

The Cham range with the Cham digits.

TAI_THAM_HORA

```java
public static final
NumericShaper.Range
TAI_THAM_HORA
```

The Tai Tham Hora range with the Tai Tham Hora digits.

---

#### TAI_THAM_HORA

public static final

NumericShaper.Range

TAI_THAM_HORA

The Tai Tham Hora range with the Tai Tham Hora digits.

TAI_THAM_THAM

```java
public static final
NumericShaper.Range
TAI_THAM_THAM
```

The Tai Tham Tham range with the Tai Tham Tham digits.

---

#### TAI_THAM_THAM

public static final

NumericShaper.Range

TAI_THAM_THAM

The Tai Tham Tham range with the Tai Tham Tham digits.

JAVANESE

```java
public static final
NumericShaper.Range
JAVANESE
```

The Javanese range with the Javanese digits.

---

#### JAVANESE

public static final

NumericShaper.Range

JAVANESE

The Javanese range with the Javanese digits.

MEETEI_MAYEK

```java
public static final
NumericShaper.Range
MEETEI_MAYEK
```

The Meetei Mayek range with the Meetei Mayek digits.

---

#### MEETEI_MAYEK

public static final

NumericShaper.Range

MEETEI_MAYEK

The Meetei Mayek range with the Meetei Mayek digits.

SINHALA

```java
public static final
NumericShaper.Range
SINHALA
```

The Sinhala range with the Sinhala digits.

**Since:** 9

---

#### SINHALA

public static final

NumericShaper.Range

SINHALA

The Sinhala range with the Sinhala digits.

MYANMAR_TAI_LAING

```java
public static final
NumericShaper.Range
MYANMAR_TAI_LAING
```

The Myanmar Extended-B range with the Myanmar Tai Laing digits.

**Since:** 9

---

#### MYANMAR_TAI_LAING

public static final

NumericShaper.Range

MYANMAR_TAI_LAING

The Myanmar Extended-B range with the Myanmar Tai Laing digits.

Method Detail

- values

```java
public static
NumericShaper.Range
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NumericShaper.Range c : NumericShaper.Range.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
NumericShaper.Range
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
NumericShaper.Range
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NumericShaper.Range c : NumericShaper.Range.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

NumericShaper.Range

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NumericShaper.Range c : NumericShaper.Range.values())
System.out.println(c);
```

for (NumericShaper.Range c : NumericShaper.Range.values())
System.out.println(c);

valueOf

```java
public static
NumericShaper.Range
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

NumericShaper.Range

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

