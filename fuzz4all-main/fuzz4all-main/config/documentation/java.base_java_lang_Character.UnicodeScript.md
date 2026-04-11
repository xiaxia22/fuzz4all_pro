# Enum Character.UnicodeScript

**Source:** `java.base\java\lang\Character.UnicodeScript.html`

### Class Description

```java
public static enum
Character.UnicodeScript

extends
Enum
<
Character.UnicodeScript
>
```

A family of character subsets representing the character scripts
defined in the

Unicode Standard Annex #24: Script Names

. Every Unicode
character is assigned to a single Unicode script, either a specific
script, such as

Latin

, or
one of the following three special values,

Inherited

,

Common

or

Unknown

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Character.UnicodeScript

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Character.UnicodeScript
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Character.UnicodeScript c : Character.UnicodeScript.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Character.UnicodeScript
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

#### public static
Character.UnicodeScript
of​(int codePoint)

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

**Parameters:**
- codePoint

- the character (Unicode code point) in question.

**Returns:**
- The

UnicodeScript

constant representing the
Unicode script of which this character is assigned to.

**Throws:**
- IllegalArgumentException

- if the specified

codePoint

is an invalid Unicode code point.

**See Also:**
- Character.isValidCodePoint(int)

---

#### public static final
Character.UnicodeScript
forName​(
String
scriptName)

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias. Script names and their aliases are
determined by The Unicode Standard. The files

Scripts<version>.txt

and

PropertyValueAliases<version>.txt

define script names
and the script name aliases for a particular version of the
standard. The

Character

class specifies the version of
the standard that it supports.

Character case is ignored for all of the valid script names.
The en_US locale's case mapping rules are used to provide
case-insensitive string comparisons for script name validation.

**Parameters:**
- scriptName

- A

UnicodeScript

name.

**Returns:**
- The

UnicodeScript

constant identified
by

scriptName

**Throws:**
- IllegalArgumentException

- if

scriptName

is an
invalid name
- NullPointerException

- if

scriptName

is null

---

### Additional Sections

#### Enum Character.UnicodeScript

java.lang.Object

- java.lang.Enum

<

Character.UnicodeScript

>
- - java.lang.Character.UnicodeScript

java.lang.Enum

<

Character.UnicodeScript

>

- java.lang.Character.UnicodeScript

java.lang.Character.UnicodeScript

**All Implemented Interfaces:** Serializable

,

Comparable

<

Character.UnicodeScript

>

**Enclosing class:** Character

```java
public static enum
Character.UnicodeScript

extends
Enum
<
Character.UnicodeScript
>
```

A family of character subsets representing the character scripts
defined in the

Unicode Standard Annex #24: Script Names

. Every Unicode
character is assigned to a single Unicode script, either a specific
script, such as

Latin

, or
one of the following three special values,

Inherited

,

Common

or

Unknown

.

**Since:** 1.7

public static enum

Character.UnicodeScript

extends

Enum

<

Character.UnicodeScript

>

A family of character subsets representing the character scripts
defined in the

Unicode Standard Annex #24: Script Names

. Every Unicode
character is assigned to a single Unicode script, either a specific
script, such as

Latin

, or
one of the following three special values,

Inherited

,

Common

or

Unknown

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ADLAM

Unicode script "Adlam".

AHOM

Unicode script "Ahom".

ANATOLIAN_HIEROGLYPHS

Unicode script "Anatolian Hieroglyphs".

ARABIC

Unicode script "Arabic".

ARMENIAN

Unicode script "Armenian".

AVESTAN

Unicode script "Avestan".

BALINESE

Unicode script "Balinese".

BAMUM

Unicode script "Bamum".

BASSA_VAH

Unicode script "Bassa Vah".

BATAK

Unicode script "Batak".

BENGALI

Unicode script "Bengali".

BHAIKSUKI

Unicode script "Bhaiksuki".

BOPOMOFO

Unicode script "Bopomofo".

BRAHMI

Unicode script "Brahmi".

BRAILLE

Unicode script "Braille".

BUGINESE

Unicode script "Buginese".

BUHID

Unicode script "Buhid".

CANADIAN_ABORIGINAL

Unicode script "Canadian_Aboriginal".

CARIAN

Unicode script "Carian".

CAUCASIAN_ALBANIAN

Unicode script "Caucasian Albanian".

CHAKMA

Unicode script "Chakma".

CHAM

Unicode script "Cham".

CHEROKEE

Unicode script "Cherokee".

COMMON

Unicode script "Common".

COPTIC

Unicode script "Coptic".

CUNEIFORM

Unicode script "Cuneiform".

CYPRIOT

Unicode script "Cypriot".

CYRILLIC

Unicode script "Cyrillic".

DESERET

Unicode script "Deseret".

DEVANAGARI

Unicode script "Devanagari".

DUPLOYAN

Unicode script "Duployan".

EGYPTIAN_HIEROGLYPHS

Unicode script "Egyptian_Hieroglyphs".

ELBASAN

Unicode script "Elbasan".

ETHIOPIC

Unicode script "Ethiopic".

GEORGIAN

Unicode script "Georgian".

GLAGOLITIC

Unicode script "Glagolitic".

GOTHIC

Unicode script "Gothic".

GRANTHA

Unicode script "Grantha".

GREEK

Unicode script "Greek".

GUJARATI

Unicode script "Gujarati".

GURMUKHI

Unicode script "Gurmukhi".

HAN

Unicode script "Han".

HANGUL

Unicode script "Hangul".

HANUNOO

Unicode script "Hanunoo".

HATRAN

Unicode script "Hatran".

HEBREW

Unicode script "Hebrew".

HIRAGANA

Unicode script "Hiragana".

IMPERIAL_ARAMAIC

Unicode script "Imperial_Aramaic".

INHERITED

Unicode script "Inherited".

INSCRIPTIONAL_PAHLAVI

Unicode script "Inscriptional_Pahlavi".

INSCRIPTIONAL_PARTHIAN

Unicode script "Inscriptional_Parthian".

JAVANESE

Unicode script "Javanese".

KAITHI

Unicode script "Kaithi".

KANNADA

Unicode script "Kannada".

KATAKANA

Unicode script "Katakana".

KAYAH_LI

Unicode script "Kayah_Li".

KHAROSHTHI

Unicode script "Kharoshthi".

KHMER

Unicode script "Khmer".

KHOJKI

Unicode script "Khojki".

KHUDAWADI

Unicode script "Khudawadi".

LAO

Unicode script "Lao".

LATIN

Unicode script "Latin".

LEPCHA

Unicode script "Lepcha".

LIMBU

Unicode script "Limbu".

LINEAR_A

Unicode script "Linear A".

LINEAR_B

Unicode script "Linear_B".

LISU

Unicode script "Lisu".

LYCIAN

Unicode script "Lycian".

LYDIAN

Unicode script "Lydian".

MAHAJANI

Unicode script "Mahajani".

MALAYALAM

Unicode script "Malayalam".

MANDAIC

Unicode script "Mandaic".

MANICHAEAN

Unicode script "Manichaean".

MARCHEN

Unicode script "Marchen".

MASARAM_GONDI

Unicode script "Masaram Gondi".

MEETEI_MAYEK

Unicode script "Meetei_Mayek".

MENDE_KIKAKUI

Unicode script "Mende Kikakui".

MEROITIC_CURSIVE

Unicode script "Meroitic Cursive".

MEROITIC_HIEROGLYPHS

Unicode script "Meroitic Hieroglyphs".

MIAO

Unicode script "Miao".

MODI

Unicode script "Modi".

MONGOLIAN

Unicode script "Mongolian".

MRO

Unicode script "Mro".

MULTANI

Unicode script "Multani".

MYANMAR

Unicode script "Myanmar".

NABATAEAN

Unicode script "Nabataean".

NEW_TAI_LUE

Unicode script "New_Tai_Lue".

NEWA

Unicode script "Newa".

NKO

Unicode script "Nko".

NUSHU

Unicode script "Nushu".

OGHAM

Unicode script "Ogham".

OL_CHIKI

Unicode script "Ol_Chiki".

OLD_HUNGARIAN

Unicode script "Old Hungarian".

OLD_ITALIC

Unicode script "Old_Italic".

OLD_NORTH_ARABIAN

Unicode script "Old North Arabian".

OLD_PERMIC

Unicode script "Old Permic".

OLD_PERSIAN

Unicode script "Old_Persian".

OLD_SOUTH_ARABIAN

Unicode script "Old_South_Arabian".

OLD_TURKIC

Unicode script "Old_Turkic".

ORIYA

Unicode script "Oriya".

OSAGE

Unicode script "Osage".

OSMANYA

Unicode script "Osmanya".

PAHAWH_HMONG

Unicode script "Pahawh Hmong".

PALMYRENE

Unicode script "Palmyrene".

PAU_CIN_HAU

Unicode script "Pau Cin Hau".

PHAGS_PA

Unicode script "Phags_Pa".

PHOENICIAN

Unicode script "Phoenician".

PSALTER_PAHLAVI

Unicode script "Psalter Pahlavi".

REJANG

Unicode script "Rejang".

RUNIC

Unicode script "Runic".

SAMARITAN

Unicode script "Samaritan".

SAURASHTRA

Unicode script "Saurashtra".

SHARADA

Unicode script "Sharada".

SHAVIAN

Unicode script "Shavian".

SIDDHAM

Unicode script "Siddham".

SIGNWRITING

Unicode script "SignWriting".

SINHALA

Unicode script "Sinhala".

SORA_SOMPENG

Unicode script "Sora Sompeng".

SOYOMBO

Unicode script "Soyombo".

SUNDANESE

Unicode script "Sundanese".

SYLOTI_NAGRI

Unicode script "Syloti_Nagri".

SYRIAC

Unicode script "Syriac".

TAGALOG

Unicode script "Tagalog".

TAGBANWA

Unicode script "Tagbanwa".

TAI_LE

Unicode script "Tai_Le".

TAI_THAM

Unicode script "Tai_Tham".

TAI_VIET

Unicode script "Tai_Viet".

TAKRI

Unicode script "Takri".

TAMIL

Unicode script "Tamil".

TANGUT

Unicode script "Tangut".

TELUGU

Unicode script "Telugu".

THAANA

Unicode script "Thaana".

THAI

Unicode script "Thai".

TIBETAN

Unicode script "Tibetan".

TIFINAGH

Unicode script "Tifinagh".

TIRHUTA

Unicode script "Tirhuta".

UGARITIC

Unicode script "Ugaritic".

UNKNOWN

Unicode script "Unknown".

VAI

Unicode script "Vai".

WARANG_CITI

Unicode script "Warang Citi".

YI

Unicode script "Yi".

ZANABAZAR_SQUARE

Unicode script "Zanabazar Square".

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Character.UnicodeScript

forName

​(

String

scriptName)

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias.

static

Character.UnicodeScript

of

​(int codePoint)

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

static

Character.UnicodeScript

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Character.UnicodeScript

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

ADLAM

Unicode script "Adlam".

AHOM

Unicode script "Ahom".

ANATOLIAN_HIEROGLYPHS

Unicode script "Anatolian Hieroglyphs".

ARABIC

Unicode script "Arabic".

ARMENIAN

Unicode script "Armenian".

AVESTAN

Unicode script "Avestan".

BALINESE

Unicode script "Balinese".

BAMUM

Unicode script "Bamum".

BASSA_VAH

Unicode script "Bassa Vah".

BATAK

Unicode script "Batak".

BENGALI

Unicode script "Bengali".

BHAIKSUKI

Unicode script "Bhaiksuki".

BOPOMOFO

Unicode script "Bopomofo".

BRAHMI

Unicode script "Brahmi".

BRAILLE

Unicode script "Braille".

BUGINESE

Unicode script "Buginese".

BUHID

Unicode script "Buhid".

CANADIAN_ABORIGINAL

Unicode script "Canadian_Aboriginal".

CARIAN

Unicode script "Carian".

CAUCASIAN_ALBANIAN

Unicode script "Caucasian Albanian".

CHAKMA

Unicode script "Chakma".

CHAM

Unicode script "Cham".

CHEROKEE

Unicode script "Cherokee".

COMMON

Unicode script "Common".

COPTIC

Unicode script "Coptic".

CUNEIFORM

Unicode script "Cuneiform".

CYPRIOT

Unicode script "Cypriot".

CYRILLIC

Unicode script "Cyrillic".

DESERET

Unicode script "Deseret".

DEVANAGARI

Unicode script "Devanagari".

DUPLOYAN

Unicode script "Duployan".

EGYPTIAN_HIEROGLYPHS

Unicode script "Egyptian_Hieroglyphs".

ELBASAN

Unicode script "Elbasan".

ETHIOPIC

Unicode script "Ethiopic".

GEORGIAN

Unicode script "Georgian".

GLAGOLITIC

Unicode script "Glagolitic".

GOTHIC

Unicode script "Gothic".

GRANTHA

Unicode script "Grantha".

GREEK

Unicode script "Greek".

GUJARATI

Unicode script "Gujarati".

GURMUKHI

Unicode script "Gurmukhi".

HAN

Unicode script "Han".

HANGUL

Unicode script "Hangul".

HANUNOO

Unicode script "Hanunoo".

HATRAN

Unicode script "Hatran".

HEBREW

Unicode script "Hebrew".

HIRAGANA

Unicode script "Hiragana".

IMPERIAL_ARAMAIC

Unicode script "Imperial_Aramaic".

INHERITED

Unicode script "Inherited".

INSCRIPTIONAL_PAHLAVI

Unicode script "Inscriptional_Pahlavi".

INSCRIPTIONAL_PARTHIAN

Unicode script "Inscriptional_Parthian".

JAVANESE

Unicode script "Javanese".

KAITHI

Unicode script "Kaithi".

KANNADA

Unicode script "Kannada".

KATAKANA

Unicode script "Katakana".

KAYAH_LI

Unicode script "Kayah_Li".

KHAROSHTHI

Unicode script "Kharoshthi".

KHMER

Unicode script "Khmer".

KHOJKI

Unicode script "Khojki".

KHUDAWADI

Unicode script "Khudawadi".

LAO

Unicode script "Lao".

LATIN

Unicode script "Latin".

LEPCHA

Unicode script "Lepcha".

LIMBU

Unicode script "Limbu".

LINEAR_A

Unicode script "Linear A".

LINEAR_B

Unicode script "Linear_B".

LISU

Unicode script "Lisu".

LYCIAN

Unicode script "Lycian".

LYDIAN

Unicode script "Lydian".

MAHAJANI

Unicode script "Mahajani".

MALAYALAM

Unicode script "Malayalam".

MANDAIC

Unicode script "Mandaic".

MANICHAEAN

Unicode script "Manichaean".

MARCHEN

Unicode script "Marchen".

MASARAM_GONDI

Unicode script "Masaram Gondi".

MEETEI_MAYEK

Unicode script "Meetei_Mayek".

MENDE_KIKAKUI

Unicode script "Mende Kikakui".

MEROITIC_CURSIVE

Unicode script "Meroitic Cursive".

MEROITIC_HIEROGLYPHS

Unicode script "Meroitic Hieroglyphs".

MIAO

Unicode script "Miao".

MODI

Unicode script "Modi".

MONGOLIAN

Unicode script "Mongolian".

MRO

Unicode script "Mro".

MULTANI

Unicode script "Multani".

MYANMAR

Unicode script "Myanmar".

NABATAEAN

Unicode script "Nabataean".

NEW_TAI_LUE

Unicode script "New_Tai_Lue".

NEWA

Unicode script "Newa".

NKO

Unicode script "Nko".

NUSHU

Unicode script "Nushu".

OGHAM

Unicode script "Ogham".

OL_CHIKI

Unicode script "Ol_Chiki".

OLD_HUNGARIAN

Unicode script "Old Hungarian".

OLD_ITALIC

Unicode script "Old_Italic".

OLD_NORTH_ARABIAN

Unicode script "Old North Arabian".

OLD_PERMIC

Unicode script "Old Permic".

OLD_PERSIAN

Unicode script "Old_Persian".

OLD_SOUTH_ARABIAN

Unicode script "Old_South_Arabian".

OLD_TURKIC

Unicode script "Old_Turkic".

ORIYA

Unicode script "Oriya".

OSAGE

Unicode script "Osage".

OSMANYA

Unicode script "Osmanya".

PAHAWH_HMONG

Unicode script "Pahawh Hmong".

PALMYRENE

Unicode script "Palmyrene".

PAU_CIN_HAU

Unicode script "Pau Cin Hau".

PHAGS_PA

Unicode script "Phags_Pa".

PHOENICIAN

Unicode script "Phoenician".

PSALTER_PAHLAVI

Unicode script "Psalter Pahlavi".

REJANG

Unicode script "Rejang".

RUNIC

Unicode script "Runic".

SAMARITAN

Unicode script "Samaritan".

SAURASHTRA

Unicode script "Saurashtra".

SHARADA

Unicode script "Sharada".

SHAVIAN

Unicode script "Shavian".

SIDDHAM

Unicode script "Siddham".

SIGNWRITING

Unicode script "SignWriting".

SINHALA

Unicode script "Sinhala".

SORA_SOMPENG

Unicode script "Sora Sompeng".

SOYOMBO

Unicode script "Soyombo".

SUNDANESE

Unicode script "Sundanese".

SYLOTI_NAGRI

Unicode script "Syloti_Nagri".

SYRIAC

Unicode script "Syriac".

TAGALOG

Unicode script "Tagalog".

TAGBANWA

Unicode script "Tagbanwa".

TAI_LE

Unicode script "Tai_Le".

TAI_THAM

Unicode script "Tai_Tham".

TAI_VIET

Unicode script "Tai_Viet".

TAKRI

Unicode script "Takri".

TAMIL

Unicode script "Tamil".

TANGUT

Unicode script "Tangut".

TELUGU

Unicode script "Telugu".

THAANA

Unicode script "Thaana".

THAI

Unicode script "Thai".

TIBETAN

Unicode script "Tibetan".

TIFINAGH

Unicode script "Tifinagh".

TIRHUTA

Unicode script "Tirhuta".

UGARITIC

Unicode script "Ugaritic".

UNKNOWN

Unicode script "Unknown".

VAI

Unicode script "Vai".

WARANG_CITI

Unicode script "Warang Citi".

YI

Unicode script "Yi".

ZANABAZAR_SQUARE

Unicode script "Zanabazar Square".

---

#### Enum Constant Summary

Unicode script "Adlam".

Unicode script "Ahom".

Unicode script "Anatolian Hieroglyphs".

Unicode script "Arabic".

Unicode script "Armenian".

Unicode script "Avestan".

Unicode script "Balinese".

Unicode script "Bamum".

Unicode script "Bassa Vah".

Unicode script "Batak".

Unicode script "Bengali".

Unicode script "Bhaiksuki".

Unicode script "Bopomofo".

Unicode script "Brahmi".

Unicode script "Braille".

Unicode script "Buginese".

Unicode script "Buhid".

Unicode script "Canadian_Aboriginal".

Unicode script "Carian".

Unicode script "Caucasian Albanian".

Unicode script "Chakma".

Unicode script "Cham".

Unicode script "Cherokee".

Unicode script "Common".

Unicode script "Coptic".

Unicode script "Cuneiform".

Unicode script "Cypriot".

Unicode script "Cyrillic".

Unicode script "Deseret".

Unicode script "Devanagari".

Unicode script "Duployan".

Unicode script "Egyptian_Hieroglyphs".

Unicode script "Elbasan".

Unicode script "Ethiopic".

Unicode script "Georgian".

Unicode script "Glagolitic".

Unicode script "Gothic".

Unicode script "Grantha".

Unicode script "Greek".

Unicode script "Gujarati".

Unicode script "Gurmukhi".

Unicode script "Han".

Unicode script "Hangul".

Unicode script "Hanunoo".

Unicode script "Hatran".

Unicode script "Hebrew".

Unicode script "Hiragana".

Unicode script "Imperial_Aramaic".

Unicode script "Inherited".

Unicode script "Inscriptional_Pahlavi".

Unicode script "Inscriptional_Parthian".

Unicode script "Javanese".

Unicode script "Kaithi".

Unicode script "Kannada".

Unicode script "Katakana".

Unicode script "Kayah_Li".

Unicode script "Kharoshthi".

Unicode script "Khmer".

Unicode script "Khojki".

Unicode script "Khudawadi".

Unicode script "Lao".

Unicode script "Latin".

Unicode script "Lepcha".

Unicode script "Limbu".

Unicode script "Linear A".

Unicode script "Linear_B".

Unicode script "Lisu".

Unicode script "Lycian".

Unicode script "Lydian".

Unicode script "Mahajani".

Unicode script "Malayalam".

Unicode script "Mandaic".

Unicode script "Manichaean".

Unicode script "Marchen".

Unicode script "Masaram Gondi".

Unicode script "Meetei_Mayek".

Unicode script "Mende Kikakui".

Unicode script "Meroitic Cursive".

Unicode script "Meroitic Hieroglyphs".

Unicode script "Miao".

Unicode script "Modi".

Unicode script "Mongolian".

Unicode script "Mro".

Unicode script "Multani".

Unicode script "Myanmar".

Unicode script "Nabataean".

Unicode script "New_Tai_Lue".

Unicode script "Newa".

Unicode script "Nko".

Unicode script "Nushu".

Unicode script "Ogham".

Unicode script "Ol_Chiki".

Unicode script "Old Hungarian".

Unicode script "Old_Italic".

Unicode script "Old North Arabian".

Unicode script "Old Permic".

Unicode script "Old_Persian".

Unicode script "Old_South_Arabian".

Unicode script "Old_Turkic".

Unicode script "Oriya".

Unicode script "Osage".

Unicode script "Osmanya".

Unicode script "Pahawh Hmong".

Unicode script "Palmyrene".

Unicode script "Pau Cin Hau".

Unicode script "Phags_Pa".

Unicode script "Phoenician".

Unicode script "Psalter Pahlavi".

Unicode script "Rejang".

Unicode script "Runic".

Unicode script "Samaritan".

Unicode script "Saurashtra".

Unicode script "Sharada".

Unicode script "Shavian".

Unicode script "Siddham".

Unicode script "SignWriting".

Unicode script "Sinhala".

Unicode script "Sora Sompeng".

Unicode script "Soyombo".

Unicode script "Sundanese".

Unicode script "Syloti_Nagri".

Unicode script "Syriac".

Unicode script "Tagalog".

Unicode script "Tagbanwa".

Unicode script "Tai_Le".

Unicode script "Tai_Tham".

Unicode script "Tai_Viet".

Unicode script "Takri".

Unicode script "Tamil".

Unicode script "Tangut".

Unicode script "Telugu".

Unicode script "Thaana".

Unicode script "Thai".

Unicode script "Tibetan".

Unicode script "Tifinagh".

Unicode script "Tirhuta".

Unicode script "Ugaritic".

Unicode script "Unknown".

Unicode script "Vai".

Unicode script "Warang Citi".

Unicode script "Yi".

Unicode script "Zanabazar Square".

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Character.UnicodeScript

forName

​(

String

scriptName)

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias.

static

Character.UnicodeScript

of

​(int codePoint)

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

static

Character.UnicodeScript

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Character.UnicodeScript

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

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias.

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

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

- COMMON

```java
public static final
Character.UnicodeScript
COMMON
```

Unicode script "Common".

- LATIN

```java
public static final
Character.UnicodeScript
LATIN
```

Unicode script "Latin".

- GREEK

```java
public static final
Character.UnicodeScript
GREEK
```

Unicode script "Greek".

- CYRILLIC

```java
public static final
Character.UnicodeScript
CYRILLIC
```

Unicode script "Cyrillic".

- ARMENIAN

```java
public static final
Character.UnicodeScript
ARMENIAN
```

Unicode script "Armenian".

- HEBREW

```java
public static final
Character.UnicodeScript
HEBREW
```

Unicode script "Hebrew".

- ARABIC

```java
public static final
Character.UnicodeScript
ARABIC
```

Unicode script "Arabic".

- SYRIAC

```java
public static final
Character.UnicodeScript
SYRIAC
```

Unicode script "Syriac".

- THAANA

```java
public static final
Character.UnicodeScript
THAANA
```

Unicode script "Thaana".

- DEVANAGARI

```java
public static final
Character.UnicodeScript
DEVANAGARI
```

Unicode script "Devanagari".

- BENGALI

```java
public static final
Character.UnicodeScript
BENGALI
```

Unicode script "Bengali".

- GURMUKHI

```java
public static final
Character.UnicodeScript
GURMUKHI
```

Unicode script "Gurmukhi".

- GUJARATI

```java
public static final
Character.UnicodeScript
GUJARATI
```

Unicode script "Gujarati".

- ORIYA

```java
public static final
Character.UnicodeScript
ORIYA
```

Unicode script "Oriya".

- TAMIL

```java
public static final
Character.UnicodeScript
TAMIL
```

Unicode script "Tamil".

- TELUGU

```java
public static final
Character.UnicodeScript
TELUGU
```

Unicode script "Telugu".

- KANNADA

```java
public static final
Character.UnicodeScript
KANNADA
```

Unicode script "Kannada".

- MALAYALAM

```java
public static final
Character.UnicodeScript
MALAYALAM
```

Unicode script "Malayalam".

- SINHALA

```java
public static final
Character.UnicodeScript
SINHALA
```

Unicode script "Sinhala".

- THAI

```java
public static final
Character.UnicodeScript
THAI
```

Unicode script "Thai".

- LAO

```java
public static final
Character.UnicodeScript
LAO
```

Unicode script "Lao".

- TIBETAN

```java
public static final
Character.UnicodeScript
TIBETAN
```

Unicode script "Tibetan".

- MYANMAR

```java
public static final
Character.UnicodeScript
MYANMAR
```

Unicode script "Myanmar".

- GEORGIAN

```java
public static final
Character.UnicodeScript
GEORGIAN
```

Unicode script "Georgian".

- HANGUL

```java
public static final
Character.UnicodeScript
HANGUL
```

Unicode script "Hangul".

- ETHIOPIC

```java
public static final
Character.UnicodeScript
ETHIOPIC
```

Unicode script "Ethiopic".

- CHEROKEE

```java
public static final
Character.UnicodeScript
CHEROKEE
```

Unicode script "Cherokee".

- CANADIAN_ABORIGINAL

```java
public static final
Character.UnicodeScript
CANADIAN_ABORIGINAL
```

Unicode script "Canadian_Aboriginal".

- OGHAM

```java
public static final
Character.UnicodeScript
OGHAM
```

Unicode script "Ogham".

- RUNIC

```java
public static final
Character.UnicodeScript
RUNIC
```

Unicode script "Runic".

- KHMER

```java
public static final
Character.UnicodeScript
KHMER
```

Unicode script "Khmer".

- MONGOLIAN

```java
public static final
Character.UnicodeScript
MONGOLIAN
```

Unicode script "Mongolian".

- HIRAGANA

```java
public static final
Character.UnicodeScript
HIRAGANA
```

Unicode script "Hiragana".

- KATAKANA

```java
public static final
Character.UnicodeScript
KATAKANA
```

Unicode script "Katakana".

- BOPOMOFO

```java
public static final
Character.UnicodeScript
BOPOMOFO
```

Unicode script "Bopomofo".

- HAN

```java
public static final
Character.UnicodeScript
HAN
```

Unicode script "Han".

- YI

```java
public static final
Character.UnicodeScript
YI
```

Unicode script "Yi".

- OLD_ITALIC

```java
public static final
Character.UnicodeScript
OLD_ITALIC
```

Unicode script "Old_Italic".

- GOTHIC

```java
public static final
Character.UnicodeScript
GOTHIC
```

Unicode script "Gothic".

- DESERET

```java
public static final
Character.UnicodeScript
DESERET
```

Unicode script "Deseret".

- INHERITED

```java
public static final
Character.UnicodeScript
INHERITED
```

Unicode script "Inherited".

- TAGALOG

```java
public static final
Character.UnicodeScript
TAGALOG
```

Unicode script "Tagalog".

- HANUNOO

```java
public static final
Character.UnicodeScript
HANUNOO
```

Unicode script "Hanunoo".

- BUHID

```java
public static final
Character.UnicodeScript
BUHID
```

Unicode script "Buhid".

- TAGBANWA

```java
public static final
Character.UnicodeScript
TAGBANWA
```

Unicode script "Tagbanwa".

- LIMBU

```java
public static final
Character.UnicodeScript
LIMBU
```

Unicode script "Limbu".

- TAI_LE

```java
public static final
Character.UnicodeScript
TAI_LE
```

Unicode script "Tai_Le".

- LINEAR_B

```java
public static final
Character.UnicodeScript
LINEAR_B
```

Unicode script "Linear_B".

- UGARITIC

```java
public static final
Character.UnicodeScript
UGARITIC
```

Unicode script "Ugaritic".

- SHAVIAN

```java
public static final
Character.UnicodeScript
SHAVIAN
```

Unicode script "Shavian".

- OSMANYA

```java
public static final
Character.UnicodeScript
OSMANYA
```

Unicode script "Osmanya".

- CYPRIOT

```java
public static final
Character.UnicodeScript
CYPRIOT
```

Unicode script "Cypriot".

- BRAILLE

```java
public static final
Character.UnicodeScript
BRAILLE
```

Unicode script "Braille".

- BUGINESE

```java
public static final
Character.UnicodeScript
BUGINESE
```

Unicode script "Buginese".

- COPTIC

```java
public static final
Character.UnicodeScript
COPTIC
```

Unicode script "Coptic".

- NEW_TAI_LUE

```java
public static final
Character.UnicodeScript
NEW_TAI_LUE
```

Unicode script "New_Tai_Lue".

- GLAGOLITIC

```java
public static final
Character.UnicodeScript
GLAGOLITIC
```

Unicode script "Glagolitic".

- TIFINAGH

```java
public static final
Character.UnicodeScript
TIFINAGH
```

Unicode script "Tifinagh".

- SYLOTI_NAGRI

```java
public static final
Character.UnicodeScript
SYLOTI_NAGRI
```

Unicode script "Syloti_Nagri".

- OLD_PERSIAN

```java
public static final
Character.UnicodeScript
OLD_PERSIAN
```

Unicode script "Old_Persian".

- KHAROSHTHI

```java
public static final
Character.UnicodeScript
KHAROSHTHI
```

Unicode script "Kharoshthi".

- BALINESE

```java
public static final
Character.UnicodeScript
BALINESE
```

Unicode script "Balinese".

- CUNEIFORM

```java
public static final
Character.UnicodeScript
CUNEIFORM
```

Unicode script "Cuneiform".

- PHOENICIAN

```java
public static final
Character.UnicodeScript
PHOENICIAN
```

Unicode script "Phoenician".

- PHAGS_PA

```java
public static final
Character.UnicodeScript
PHAGS_PA
```

Unicode script "Phags_Pa".

- NKO

```java
public static final
Character.UnicodeScript
NKO
```

Unicode script "Nko".

- SUNDANESE

```java
public static final
Character.UnicodeScript
SUNDANESE
```

Unicode script "Sundanese".

- BATAK

```java
public static final
Character.UnicodeScript
BATAK
```

Unicode script "Batak".

- LEPCHA

```java
public static final
Character.UnicodeScript
LEPCHA
```

Unicode script "Lepcha".

- OL_CHIKI

```java
public static final
Character.UnicodeScript
OL_CHIKI
```

Unicode script "Ol_Chiki".

- VAI

```java
public static final
Character.UnicodeScript
VAI
```

Unicode script "Vai".

- SAURASHTRA

```java
public static final
Character.UnicodeScript
SAURASHTRA
```

Unicode script "Saurashtra".

- KAYAH_LI

```java
public static final
Character.UnicodeScript
KAYAH_LI
```

Unicode script "Kayah_Li".

- REJANG

```java
public static final
Character.UnicodeScript
REJANG
```

Unicode script "Rejang".

- LYCIAN

```java
public static final
Character.UnicodeScript
LYCIAN
```

Unicode script "Lycian".

- CARIAN

```java
public static final
Character.UnicodeScript
CARIAN
```

Unicode script "Carian".

- LYDIAN

```java
public static final
Character.UnicodeScript
LYDIAN
```

Unicode script "Lydian".

- CHAM

```java
public static final
Character.UnicodeScript
CHAM
```

Unicode script "Cham".

- TAI_THAM

```java
public static final
Character.UnicodeScript
TAI_THAM
```

Unicode script "Tai_Tham".

- TAI_VIET

```java
public static final
Character.UnicodeScript
TAI_VIET
```

Unicode script "Tai_Viet".

- AVESTAN

```java
public static final
Character.UnicodeScript
AVESTAN
```

Unicode script "Avestan".

- EGYPTIAN_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
EGYPTIAN_HIEROGLYPHS
```

Unicode script "Egyptian_Hieroglyphs".

- SAMARITAN

```java
public static final
Character.UnicodeScript
SAMARITAN
```

Unicode script "Samaritan".

- MANDAIC

```java
public static final
Character.UnicodeScript
MANDAIC
```

Unicode script "Mandaic".

- LISU

```java
public static final
Character.UnicodeScript
LISU
```

Unicode script "Lisu".

- BAMUM

```java
public static final
Character.UnicodeScript
BAMUM
```

Unicode script "Bamum".

- JAVANESE

```java
public static final
Character.UnicodeScript
JAVANESE
```

Unicode script "Javanese".

- MEETEI_MAYEK

```java
public static final
Character.UnicodeScript
MEETEI_MAYEK
```

Unicode script "Meetei_Mayek".

- IMPERIAL_ARAMAIC

```java
public static final
Character.UnicodeScript
IMPERIAL_ARAMAIC
```

Unicode script "Imperial_Aramaic".

- OLD_SOUTH_ARABIAN

```java
public static final
Character.UnicodeScript
OLD_SOUTH_ARABIAN
```

Unicode script "Old_South_Arabian".

- INSCRIPTIONAL_PARTHIAN

```java
public static final
Character.UnicodeScript
INSCRIPTIONAL_PARTHIAN
```

Unicode script "Inscriptional_Parthian".

- INSCRIPTIONAL_PAHLAVI

```java
public static final
Character.UnicodeScript
INSCRIPTIONAL_PAHLAVI
```

Unicode script "Inscriptional_Pahlavi".

- OLD_TURKIC

```java
public static final
Character.UnicodeScript
OLD_TURKIC
```

Unicode script "Old_Turkic".

- BRAHMI

```java
public static final
Character.UnicodeScript
BRAHMI
```

Unicode script "Brahmi".

- KAITHI

```java
public static final
Character.UnicodeScript
KAITHI
```

Unicode script "Kaithi".

- MEROITIC_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
MEROITIC_HIEROGLYPHS
```

Unicode script "Meroitic Hieroglyphs".

**Since:** 1.8

- MEROITIC_CURSIVE

```java
public static final
Character.UnicodeScript
MEROITIC_CURSIVE
```

Unicode script "Meroitic Cursive".

**Since:** 1.8

- SORA_SOMPENG

```java
public static final
Character.UnicodeScript
SORA_SOMPENG
```

Unicode script "Sora Sompeng".

**Since:** 1.8

- CHAKMA

```java
public static final
Character.UnicodeScript
CHAKMA
```

Unicode script "Chakma".

**Since:** 1.8

- SHARADA

```java
public static final
Character.UnicodeScript
SHARADA
```

Unicode script "Sharada".

**Since:** 1.8

- TAKRI

```java
public static final
Character.UnicodeScript
TAKRI
```

Unicode script "Takri".

**Since:** 1.8

- MIAO

```java
public static final
Character.UnicodeScript
MIAO
```

Unicode script "Miao".

**Since:** 1.8

- CAUCASIAN_ALBANIAN

```java
public static final
Character.UnicodeScript
CAUCASIAN_ALBANIAN
```

Unicode script "Caucasian Albanian".

**Since:** 9

- BASSA_VAH

```java
public static final
Character.UnicodeScript
BASSA_VAH
```

Unicode script "Bassa Vah".

**Since:** 9

- DUPLOYAN

```java
public static final
Character.UnicodeScript
DUPLOYAN
```

Unicode script "Duployan".

**Since:** 9

- ELBASAN

```java
public static final
Character.UnicodeScript
ELBASAN
```

Unicode script "Elbasan".

**Since:** 9

- GRANTHA

```java
public static final
Character.UnicodeScript
GRANTHA
```

Unicode script "Grantha".

**Since:** 9

- PAHAWH_HMONG

```java
public static final
Character.UnicodeScript
PAHAWH_HMONG
```

Unicode script "Pahawh Hmong".

**Since:** 9

- KHOJKI

```java
public static final
Character.UnicodeScript
KHOJKI
```

Unicode script "Khojki".

**Since:** 9

- LINEAR_A

```java
public static final
Character.UnicodeScript
LINEAR_A
```

Unicode script "Linear A".

**Since:** 9

- MAHAJANI

```java
public static final
Character.UnicodeScript
MAHAJANI
```

Unicode script "Mahajani".

**Since:** 9

- MANICHAEAN

```java
public static final
Character.UnicodeScript
MANICHAEAN
```

Unicode script "Manichaean".

**Since:** 9

- MENDE_KIKAKUI

```java
public static final
Character.UnicodeScript
MENDE_KIKAKUI
```

Unicode script "Mende Kikakui".

**Since:** 9

- MODI

```java
public static final
Character.UnicodeScript
MODI
```

Unicode script "Modi".

**Since:** 9

- MRO

```java
public static final
Character.UnicodeScript
MRO
```

Unicode script "Mro".

**Since:** 9

- OLD_NORTH_ARABIAN

```java
public static final
Character.UnicodeScript
OLD_NORTH_ARABIAN
```

Unicode script "Old North Arabian".

**Since:** 9

- NABATAEAN

```java
public static final
Character.UnicodeScript
NABATAEAN
```

Unicode script "Nabataean".

**Since:** 9

- PALMYRENE

```java
public static final
Character.UnicodeScript
PALMYRENE
```

Unicode script "Palmyrene".

**Since:** 9

- PAU_CIN_HAU

```java
public static final
Character.UnicodeScript
PAU_CIN_HAU
```

Unicode script "Pau Cin Hau".

**Since:** 9

- OLD_PERMIC

```java
public static final
Character.UnicodeScript
OLD_PERMIC
```

Unicode script "Old Permic".

**Since:** 9

- PSALTER_PAHLAVI

```java
public static final
Character.UnicodeScript
PSALTER_PAHLAVI
```

Unicode script "Psalter Pahlavi".

**Since:** 9

- SIDDHAM

```java
public static final
Character.UnicodeScript
SIDDHAM
```

Unicode script "Siddham".

**Since:** 9

- KHUDAWADI

```java
public static final
Character.UnicodeScript
KHUDAWADI
```

Unicode script "Khudawadi".

**Since:** 9

- TIRHUTA

```java
public static final
Character.UnicodeScript
TIRHUTA
```

Unicode script "Tirhuta".

**Since:** 9

- WARANG_CITI

```java
public static final
Character.UnicodeScript
WARANG_CITI
```

Unicode script "Warang Citi".

**Since:** 9

- AHOM

```java
public static final
Character.UnicodeScript
AHOM
```

Unicode script "Ahom".

**Since:** 9

- ANATOLIAN_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
ANATOLIAN_HIEROGLYPHS
```

Unicode script "Anatolian Hieroglyphs".

**Since:** 9

- HATRAN

```java
public static final
Character.UnicodeScript
HATRAN
```

Unicode script "Hatran".

**Since:** 9

- MULTANI

```java
public static final
Character.UnicodeScript
MULTANI
```

Unicode script "Multani".

**Since:** 9

- OLD_HUNGARIAN

```java
public static final
Character.UnicodeScript
OLD_HUNGARIAN
```

Unicode script "Old Hungarian".

**Since:** 9

- SIGNWRITING

```java
public static final
Character.UnicodeScript
SIGNWRITING
```

Unicode script "SignWriting".

**Since:** 9

- ADLAM

```java
public static final
Character.UnicodeScript
ADLAM
```

Unicode script "Adlam".

**Since:** 11

- BHAIKSUKI

```java
public static final
Character.UnicodeScript
BHAIKSUKI
```

Unicode script "Bhaiksuki".

**Since:** 11

- MARCHEN

```java
public static final
Character.UnicodeScript
MARCHEN
```

Unicode script "Marchen".

**Since:** 11

- NEWA

```java
public static final
Character.UnicodeScript
NEWA
```

Unicode script "Newa".

**Since:** 11

- OSAGE

```java
public static final
Character.UnicodeScript
OSAGE
```

Unicode script "Osage".

**Since:** 11

- TANGUT

```java
public static final
Character.UnicodeScript
TANGUT
```

Unicode script "Tangut".

**Since:** 11

- MASARAM_GONDI

```java
public static final
Character.UnicodeScript
MASARAM_GONDI
```

Unicode script "Masaram Gondi".

**Since:** 11

- NUSHU

```java
public static final
Character.UnicodeScript
NUSHU
```

Unicode script "Nushu".

**Since:** 11

- SOYOMBO

```java
public static final
Character.UnicodeScript
SOYOMBO
```

Unicode script "Soyombo".

**Since:** 11

- ZANABAZAR_SQUARE

```java
public static final
Character.UnicodeScript
ZANABAZAR_SQUARE
```

Unicode script "Zanabazar Square".

**Since:** 11

- UNKNOWN

```java
public static final
Character.UnicodeScript
UNKNOWN
```

Unicode script "Unknown".

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Character.UnicodeScript
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Character.UnicodeScript c : Character.UnicodeScript.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Character.UnicodeScript
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

- of

```java
public static
Character.UnicodeScript
of​(int codePoint)
```

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

**Parameters:** codePoint

- the character (Unicode code point) in question.
**Returns:** The

UnicodeScript

constant representing the
Unicode script of which this character is assigned to.
**Throws:** IllegalArgumentException

- if the specified

codePoint

is an invalid Unicode code point.
**See Also:** Character.isValidCodePoint(int)

- forName

```java
public static final
Character.UnicodeScript
forName​(
String
scriptName)
```

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias. Script names and their aliases are
determined by The Unicode Standard. The files

Scripts<version>.txt

and

PropertyValueAliases<version>.txt

define script names
and the script name aliases for a particular version of the
standard. The

Character

class specifies the version of
the standard that it supports.

Character case is ignored for all of the valid script names.
The en_US locale's case mapping rules are used to provide
case-insensitive string comparisons for script name validation.

**Parameters:** scriptName

- A

UnicodeScript

name.
**Returns:** The

UnicodeScript

constant identified
by

scriptName
**Throws:** IllegalArgumentException

- if

scriptName

is an
invalid name
**Throws:** NullPointerException

- if

scriptName

is null

Enum Constant Detail

- COMMON

```java
public static final
Character.UnicodeScript
COMMON
```

Unicode script "Common".

- LATIN

```java
public static final
Character.UnicodeScript
LATIN
```

Unicode script "Latin".

- GREEK

```java
public static final
Character.UnicodeScript
GREEK
```

Unicode script "Greek".

- CYRILLIC

```java
public static final
Character.UnicodeScript
CYRILLIC
```

Unicode script "Cyrillic".

- ARMENIAN

```java
public static final
Character.UnicodeScript
ARMENIAN
```

Unicode script "Armenian".

- HEBREW

```java
public static final
Character.UnicodeScript
HEBREW
```

Unicode script "Hebrew".

- ARABIC

```java
public static final
Character.UnicodeScript
ARABIC
```

Unicode script "Arabic".

- SYRIAC

```java
public static final
Character.UnicodeScript
SYRIAC
```

Unicode script "Syriac".

- THAANA

```java
public static final
Character.UnicodeScript
THAANA
```

Unicode script "Thaana".

- DEVANAGARI

```java
public static final
Character.UnicodeScript
DEVANAGARI
```

Unicode script "Devanagari".

- BENGALI

```java
public static final
Character.UnicodeScript
BENGALI
```

Unicode script "Bengali".

- GURMUKHI

```java
public static final
Character.UnicodeScript
GURMUKHI
```

Unicode script "Gurmukhi".

- GUJARATI

```java
public static final
Character.UnicodeScript
GUJARATI
```

Unicode script "Gujarati".

- ORIYA

```java
public static final
Character.UnicodeScript
ORIYA
```

Unicode script "Oriya".

- TAMIL

```java
public static final
Character.UnicodeScript
TAMIL
```

Unicode script "Tamil".

- TELUGU

```java
public static final
Character.UnicodeScript
TELUGU
```

Unicode script "Telugu".

- KANNADA

```java
public static final
Character.UnicodeScript
KANNADA
```

Unicode script "Kannada".

- MALAYALAM

```java
public static final
Character.UnicodeScript
MALAYALAM
```

Unicode script "Malayalam".

- SINHALA

```java
public static final
Character.UnicodeScript
SINHALA
```

Unicode script "Sinhala".

- THAI

```java
public static final
Character.UnicodeScript
THAI
```

Unicode script "Thai".

- LAO

```java
public static final
Character.UnicodeScript
LAO
```

Unicode script "Lao".

- TIBETAN

```java
public static final
Character.UnicodeScript
TIBETAN
```

Unicode script "Tibetan".

- MYANMAR

```java
public static final
Character.UnicodeScript
MYANMAR
```

Unicode script "Myanmar".

- GEORGIAN

```java
public static final
Character.UnicodeScript
GEORGIAN
```

Unicode script "Georgian".

- HANGUL

```java
public static final
Character.UnicodeScript
HANGUL
```

Unicode script "Hangul".

- ETHIOPIC

```java
public static final
Character.UnicodeScript
ETHIOPIC
```

Unicode script "Ethiopic".

- CHEROKEE

```java
public static final
Character.UnicodeScript
CHEROKEE
```

Unicode script "Cherokee".

- CANADIAN_ABORIGINAL

```java
public static final
Character.UnicodeScript
CANADIAN_ABORIGINAL
```

Unicode script "Canadian_Aboriginal".

- OGHAM

```java
public static final
Character.UnicodeScript
OGHAM
```

Unicode script "Ogham".

- RUNIC

```java
public static final
Character.UnicodeScript
RUNIC
```

Unicode script "Runic".

- KHMER

```java
public static final
Character.UnicodeScript
KHMER
```

Unicode script "Khmer".

- MONGOLIAN

```java
public static final
Character.UnicodeScript
MONGOLIAN
```

Unicode script "Mongolian".

- HIRAGANA

```java
public static final
Character.UnicodeScript
HIRAGANA
```

Unicode script "Hiragana".

- KATAKANA

```java
public static final
Character.UnicodeScript
KATAKANA
```

Unicode script "Katakana".

- BOPOMOFO

```java
public static final
Character.UnicodeScript
BOPOMOFO
```

Unicode script "Bopomofo".

- HAN

```java
public static final
Character.UnicodeScript
HAN
```

Unicode script "Han".

- YI

```java
public static final
Character.UnicodeScript
YI
```

Unicode script "Yi".

- OLD_ITALIC

```java
public static final
Character.UnicodeScript
OLD_ITALIC
```

Unicode script "Old_Italic".

- GOTHIC

```java
public static final
Character.UnicodeScript
GOTHIC
```

Unicode script "Gothic".

- DESERET

```java
public static final
Character.UnicodeScript
DESERET
```

Unicode script "Deseret".

- INHERITED

```java
public static final
Character.UnicodeScript
INHERITED
```

Unicode script "Inherited".

- TAGALOG

```java
public static final
Character.UnicodeScript
TAGALOG
```

Unicode script "Tagalog".

- HANUNOO

```java
public static final
Character.UnicodeScript
HANUNOO
```

Unicode script "Hanunoo".

- BUHID

```java
public static final
Character.UnicodeScript
BUHID
```

Unicode script "Buhid".

- TAGBANWA

```java
public static final
Character.UnicodeScript
TAGBANWA
```

Unicode script "Tagbanwa".

- LIMBU

```java
public static final
Character.UnicodeScript
LIMBU
```

Unicode script "Limbu".

- TAI_LE

```java
public static final
Character.UnicodeScript
TAI_LE
```

Unicode script "Tai_Le".

- LINEAR_B

```java
public static final
Character.UnicodeScript
LINEAR_B
```

Unicode script "Linear_B".

- UGARITIC

```java
public static final
Character.UnicodeScript
UGARITIC
```

Unicode script "Ugaritic".

- SHAVIAN

```java
public static final
Character.UnicodeScript
SHAVIAN
```

Unicode script "Shavian".

- OSMANYA

```java
public static final
Character.UnicodeScript
OSMANYA
```

Unicode script "Osmanya".

- CYPRIOT

```java
public static final
Character.UnicodeScript
CYPRIOT
```

Unicode script "Cypriot".

- BRAILLE

```java
public static final
Character.UnicodeScript
BRAILLE
```

Unicode script "Braille".

- BUGINESE

```java
public static final
Character.UnicodeScript
BUGINESE
```

Unicode script "Buginese".

- COPTIC

```java
public static final
Character.UnicodeScript
COPTIC
```

Unicode script "Coptic".

- NEW_TAI_LUE

```java
public static final
Character.UnicodeScript
NEW_TAI_LUE
```

Unicode script "New_Tai_Lue".

- GLAGOLITIC

```java
public static final
Character.UnicodeScript
GLAGOLITIC
```

Unicode script "Glagolitic".

- TIFINAGH

```java
public static final
Character.UnicodeScript
TIFINAGH
```

Unicode script "Tifinagh".

- SYLOTI_NAGRI

```java
public static final
Character.UnicodeScript
SYLOTI_NAGRI
```

Unicode script "Syloti_Nagri".

- OLD_PERSIAN

```java
public static final
Character.UnicodeScript
OLD_PERSIAN
```

Unicode script "Old_Persian".

- KHAROSHTHI

```java
public static final
Character.UnicodeScript
KHAROSHTHI
```

Unicode script "Kharoshthi".

- BALINESE

```java
public static final
Character.UnicodeScript
BALINESE
```

Unicode script "Balinese".

- CUNEIFORM

```java
public static final
Character.UnicodeScript
CUNEIFORM
```

Unicode script "Cuneiform".

- PHOENICIAN

```java
public static final
Character.UnicodeScript
PHOENICIAN
```

Unicode script "Phoenician".

- PHAGS_PA

```java
public static final
Character.UnicodeScript
PHAGS_PA
```

Unicode script "Phags_Pa".

- NKO

```java
public static final
Character.UnicodeScript
NKO
```

Unicode script "Nko".

- SUNDANESE

```java
public static final
Character.UnicodeScript
SUNDANESE
```

Unicode script "Sundanese".

- BATAK

```java
public static final
Character.UnicodeScript
BATAK
```

Unicode script "Batak".

- LEPCHA

```java
public static final
Character.UnicodeScript
LEPCHA
```

Unicode script "Lepcha".

- OL_CHIKI

```java
public static final
Character.UnicodeScript
OL_CHIKI
```

Unicode script "Ol_Chiki".

- VAI

```java
public static final
Character.UnicodeScript
VAI
```

Unicode script "Vai".

- SAURASHTRA

```java
public static final
Character.UnicodeScript
SAURASHTRA
```

Unicode script "Saurashtra".

- KAYAH_LI

```java
public static final
Character.UnicodeScript
KAYAH_LI
```

Unicode script "Kayah_Li".

- REJANG

```java
public static final
Character.UnicodeScript
REJANG
```

Unicode script "Rejang".

- LYCIAN

```java
public static final
Character.UnicodeScript
LYCIAN
```

Unicode script "Lycian".

- CARIAN

```java
public static final
Character.UnicodeScript
CARIAN
```

Unicode script "Carian".

- LYDIAN

```java
public static final
Character.UnicodeScript
LYDIAN
```

Unicode script "Lydian".

- CHAM

```java
public static final
Character.UnicodeScript
CHAM
```

Unicode script "Cham".

- TAI_THAM

```java
public static final
Character.UnicodeScript
TAI_THAM
```

Unicode script "Tai_Tham".

- TAI_VIET

```java
public static final
Character.UnicodeScript
TAI_VIET
```

Unicode script "Tai_Viet".

- AVESTAN

```java
public static final
Character.UnicodeScript
AVESTAN
```

Unicode script "Avestan".

- EGYPTIAN_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
EGYPTIAN_HIEROGLYPHS
```

Unicode script "Egyptian_Hieroglyphs".

- SAMARITAN

```java
public static final
Character.UnicodeScript
SAMARITAN
```

Unicode script "Samaritan".

- MANDAIC

```java
public static final
Character.UnicodeScript
MANDAIC
```

Unicode script "Mandaic".

- LISU

```java
public static final
Character.UnicodeScript
LISU
```

Unicode script "Lisu".

- BAMUM

```java
public static final
Character.UnicodeScript
BAMUM
```

Unicode script "Bamum".

- JAVANESE

```java
public static final
Character.UnicodeScript
JAVANESE
```

Unicode script "Javanese".

- MEETEI_MAYEK

```java
public static final
Character.UnicodeScript
MEETEI_MAYEK
```

Unicode script "Meetei_Mayek".

- IMPERIAL_ARAMAIC

```java
public static final
Character.UnicodeScript
IMPERIAL_ARAMAIC
```

Unicode script "Imperial_Aramaic".

- OLD_SOUTH_ARABIAN

```java
public static final
Character.UnicodeScript
OLD_SOUTH_ARABIAN
```

Unicode script "Old_South_Arabian".

- INSCRIPTIONAL_PARTHIAN

```java
public static final
Character.UnicodeScript
INSCRIPTIONAL_PARTHIAN
```

Unicode script "Inscriptional_Parthian".

- INSCRIPTIONAL_PAHLAVI

```java
public static final
Character.UnicodeScript
INSCRIPTIONAL_PAHLAVI
```

Unicode script "Inscriptional_Pahlavi".

- OLD_TURKIC

```java
public static final
Character.UnicodeScript
OLD_TURKIC
```

Unicode script "Old_Turkic".

- BRAHMI

```java
public static final
Character.UnicodeScript
BRAHMI
```

Unicode script "Brahmi".

- KAITHI

```java
public static final
Character.UnicodeScript
KAITHI
```

Unicode script "Kaithi".

- MEROITIC_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
MEROITIC_HIEROGLYPHS
```

Unicode script "Meroitic Hieroglyphs".

**Since:** 1.8

- MEROITIC_CURSIVE

```java
public static final
Character.UnicodeScript
MEROITIC_CURSIVE
```

Unicode script "Meroitic Cursive".

**Since:** 1.8

- SORA_SOMPENG

```java
public static final
Character.UnicodeScript
SORA_SOMPENG
```

Unicode script "Sora Sompeng".

**Since:** 1.8

- CHAKMA

```java
public static final
Character.UnicodeScript
CHAKMA
```

Unicode script "Chakma".

**Since:** 1.8

- SHARADA

```java
public static final
Character.UnicodeScript
SHARADA
```

Unicode script "Sharada".

**Since:** 1.8

- TAKRI

```java
public static final
Character.UnicodeScript
TAKRI
```

Unicode script "Takri".

**Since:** 1.8

- MIAO

```java
public static final
Character.UnicodeScript
MIAO
```

Unicode script "Miao".

**Since:** 1.8

- CAUCASIAN_ALBANIAN

```java
public static final
Character.UnicodeScript
CAUCASIAN_ALBANIAN
```

Unicode script "Caucasian Albanian".

**Since:** 9

- BASSA_VAH

```java
public static final
Character.UnicodeScript
BASSA_VAH
```

Unicode script "Bassa Vah".

**Since:** 9

- DUPLOYAN

```java
public static final
Character.UnicodeScript
DUPLOYAN
```

Unicode script "Duployan".

**Since:** 9

- ELBASAN

```java
public static final
Character.UnicodeScript
ELBASAN
```

Unicode script "Elbasan".

**Since:** 9

- GRANTHA

```java
public static final
Character.UnicodeScript
GRANTHA
```

Unicode script "Grantha".

**Since:** 9

- PAHAWH_HMONG

```java
public static final
Character.UnicodeScript
PAHAWH_HMONG
```

Unicode script "Pahawh Hmong".

**Since:** 9

- KHOJKI

```java
public static final
Character.UnicodeScript
KHOJKI
```

Unicode script "Khojki".

**Since:** 9

- LINEAR_A

```java
public static final
Character.UnicodeScript
LINEAR_A
```

Unicode script "Linear A".

**Since:** 9

- MAHAJANI

```java
public static final
Character.UnicodeScript
MAHAJANI
```

Unicode script "Mahajani".

**Since:** 9

- MANICHAEAN

```java
public static final
Character.UnicodeScript
MANICHAEAN
```

Unicode script "Manichaean".

**Since:** 9

- MENDE_KIKAKUI

```java
public static final
Character.UnicodeScript
MENDE_KIKAKUI
```

Unicode script "Mende Kikakui".

**Since:** 9

- MODI

```java
public static final
Character.UnicodeScript
MODI
```

Unicode script "Modi".

**Since:** 9

- MRO

```java
public static final
Character.UnicodeScript
MRO
```

Unicode script "Mro".

**Since:** 9

- OLD_NORTH_ARABIAN

```java
public static final
Character.UnicodeScript
OLD_NORTH_ARABIAN
```

Unicode script "Old North Arabian".

**Since:** 9

- NABATAEAN

```java
public static final
Character.UnicodeScript
NABATAEAN
```

Unicode script "Nabataean".

**Since:** 9

- PALMYRENE

```java
public static final
Character.UnicodeScript
PALMYRENE
```

Unicode script "Palmyrene".

**Since:** 9

- PAU_CIN_HAU

```java
public static final
Character.UnicodeScript
PAU_CIN_HAU
```

Unicode script "Pau Cin Hau".

**Since:** 9

- OLD_PERMIC

```java
public static final
Character.UnicodeScript
OLD_PERMIC
```

Unicode script "Old Permic".

**Since:** 9

- PSALTER_PAHLAVI

```java
public static final
Character.UnicodeScript
PSALTER_PAHLAVI
```

Unicode script "Psalter Pahlavi".

**Since:** 9

- SIDDHAM

```java
public static final
Character.UnicodeScript
SIDDHAM
```

Unicode script "Siddham".

**Since:** 9

- KHUDAWADI

```java
public static final
Character.UnicodeScript
KHUDAWADI
```

Unicode script "Khudawadi".

**Since:** 9

- TIRHUTA

```java
public static final
Character.UnicodeScript
TIRHUTA
```

Unicode script "Tirhuta".

**Since:** 9

- WARANG_CITI

```java
public static final
Character.UnicodeScript
WARANG_CITI
```

Unicode script "Warang Citi".

**Since:** 9

- AHOM

```java
public static final
Character.UnicodeScript
AHOM
```

Unicode script "Ahom".

**Since:** 9

- ANATOLIAN_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
ANATOLIAN_HIEROGLYPHS
```

Unicode script "Anatolian Hieroglyphs".

**Since:** 9

- HATRAN

```java
public static final
Character.UnicodeScript
HATRAN
```

Unicode script "Hatran".

**Since:** 9

- MULTANI

```java
public static final
Character.UnicodeScript
MULTANI
```

Unicode script "Multani".

**Since:** 9

- OLD_HUNGARIAN

```java
public static final
Character.UnicodeScript
OLD_HUNGARIAN
```

Unicode script "Old Hungarian".

**Since:** 9

- SIGNWRITING

```java
public static final
Character.UnicodeScript
SIGNWRITING
```

Unicode script "SignWriting".

**Since:** 9

- ADLAM

```java
public static final
Character.UnicodeScript
ADLAM
```

Unicode script "Adlam".

**Since:** 11

- BHAIKSUKI

```java
public static final
Character.UnicodeScript
BHAIKSUKI
```

Unicode script "Bhaiksuki".

**Since:** 11

- MARCHEN

```java
public static final
Character.UnicodeScript
MARCHEN
```

Unicode script "Marchen".

**Since:** 11

- NEWA

```java
public static final
Character.UnicodeScript
NEWA
```

Unicode script "Newa".

**Since:** 11

- OSAGE

```java
public static final
Character.UnicodeScript
OSAGE
```

Unicode script "Osage".

**Since:** 11

- TANGUT

```java
public static final
Character.UnicodeScript
TANGUT
```

Unicode script "Tangut".

**Since:** 11

- MASARAM_GONDI

```java
public static final
Character.UnicodeScript
MASARAM_GONDI
```

Unicode script "Masaram Gondi".

**Since:** 11

- NUSHU

```java
public static final
Character.UnicodeScript
NUSHU
```

Unicode script "Nushu".

**Since:** 11

- SOYOMBO

```java
public static final
Character.UnicodeScript
SOYOMBO
```

Unicode script "Soyombo".

**Since:** 11

- ZANABAZAR_SQUARE

```java
public static final
Character.UnicodeScript
ZANABAZAR_SQUARE
```

Unicode script "Zanabazar Square".

**Since:** 11

- UNKNOWN

```java
public static final
Character.UnicodeScript
UNKNOWN
```

Unicode script "Unknown".

---

#### Enum Constant Detail

COMMON

```java
public static final
Character.UnicodeScript
COMMON
```

Unicode script "Common".

---

#### COMMON

public static final

Character.UnicodeScript

COMMON

Unicode script "Common".

LATIN

```java
public static final
Character.UnicodeScript
LATIN
```

Unicode script "Latin".

---

#### LATIN

public static final

Character.UnicodeScript

LATIN

Unicode script "Latin".

GREEK

```java
public static final
Character.UnicodeScript
GREEK
```

Unicode script "Greek".

---

#### GREEK

public static final

Character.UnicodeScript

GREEK

Unicode script "Greek".

CYRILLIC

```java
public static final
Character.UnicodeScript
CYRILLIC
```

Unicode script "Cyrillic".

---

#### CYRILLIC

public static final

Character.UnicodeScript

CYRILLIC

Unicode script "Cyrillic".

ARMENIAN

```java
public static final
Character.UnicodeScript
ARMENIAN
```

Unicode script "Armenian".

---

#### ARMENIAN

public static final

Character.UnicodeScript

ARMENIAN

Unicode script "Armenian".

HEBREW

```java
public static final
Character.UnicodeScript
HEBREW
```

Unicode script "Hebrew".

---

#### HEBREW

public static final

Character.UnicodeScript

HEBREW

Unicode script "Hebrew".

ARABIC

```java
public static final
Character.UnicodeScript
ARABIC
```

Unicode script "Arabic".

---

#### ARABIC

public static final

Character.UnicodeScript

ARABIC

Unicode script "Arabic".

SYRIAC

```java
public static final
Character.UnicodeScript
SYRIAC
```

Unicode script "Syriac".

---

#### SYRIAC

public static final

Character.UnicodeScript

SYRIAC

Unicode script "Syriac".

THAANA

```java
public static final
Character.UnicodeScript
THAANA
```

Unicode script "Thaana".

---

#### THAANA

public static final

Character.UnicodeScript

THAANA

Unicode script "Thaana".

DEVANAGARI

```java
public static final
Character.UnicodeScript
DEVANAGARI
```

Unicode script "Devanagari".

---

#### DEVANAGARI

public static final

Character.UnicodeScript

DEVANAGARI

Unicode script "Devanagari".

BENGALI

```java
public static final
Character.UnicodeScript
BENGALI
```

Unicode script "Bengali".

---

#### BENGALI

public static final

Character.UnicodeScript

BENGALI

Unicode script "Bengali".

GURMUKHI

```java
public static final
Character.UnicodeScript
GURMUKHI
```

Unicode script "Gurmukhi".

---

#### GURMUKHI

public static final

Character.UnicodeScript

GURMUKHI

Unicode script "Gurmukhi".

GUJARATI

```java
public static final
Character.UnicodeScript
GUJARATI
```

Unicode script "Gujarati".

---

#### GUJARATI

public static final

Character.UnicodeScript

GUJARATI

Unicode script "Gujarati".

ORIYA

```java
public static final
Character.UnicodeScript
ORIYA
```

Unicode script "Oriya".

---

#### ORIYA

public static final

Character.UnicodeScript

ORIYA

Unicode script "Oriya".

TAMIL

```java
public static final
Character.UnicodeScript
TAMIL
```

Unicode script "Tamil".

---

#### TAMIL

public static final

Character.UnicodeScript

TAMIL

Unicode script "Tamil".

TELUGU

```java
public static final
Character.UnicodeScript
TELUGU
```

Unicode script "Telugu".

---

#### TELUGU

public static final

Character.UnicodeScript

TELUGU

Unicode script "Telugu".

KANNADA

```java
public static final
Character.UnicodeScript
KANNADA
```

Unicode script "Kannada".

---

#### KANNADA

public static final

Character.UnicodeScript

KANNADA

Unicode script "Kannada".

MALAYALAM

```java
public static final
Character.UnicodeScript
MALAYALAM
```

Unicode script "Malayalam".

---

#### MALAYALAM

public static final

Character.UnicodeScript

MALAYALAM

Unicode script "Malayalam".

SINHALA

```java
public static final
Character.UnicodeScript
SINHALA
```

Unicode script "Sinhala".

---

#### SINHALA

public static final

Character.UnicodeScript

SINHALA

Unicode script "Sinhala".

THAI

```java
public static final
Character.UnicodeScript
THAI
```

Unicode script "Thai".

---

#### THAI

public static final

Character.UnicodeScript

THAI

Unicode script "Thai".

LAO

```java
public static final
Character.UnicodeScript
LAO
```

Unicode script "Lao".

---

#### LAO

public static final

Character.UnicodeScript

LAO

Unicode script "Lao".

TIBETAN

```java
public static final
Character.UnicodeScript
TIBETAN
```

Unicode script "Tibetan".

---

#### TIBETAN

public static final

Character.UnicodeScript

TIBETAN

Unicode script "Tibetan".

MYANMAR

```java
public static final
Character.UnicodeScript
MYANMAR
```

Unicode script "Myanmar".

---

#### MYANMAR

public static final

Character.UnicodeScript

MYANMAR

Unicode script "Myanmar".

GEORGIAN

```java
public static final
Character.UnicodeScript
GEORGIAN
```

Unicode script "Georgian".

---

#### GEORGIAN

public static final

Character.UnicodeScript

GEORGIAN

Unicode script "Georgian".

HANGUL

```java
public static final
Character.UnicodeScript
HANGUL
```

Unicode script "Hangul".

---

#### HANGUL

public static final

Character.UnicodeScript

HANGUL

Unicode script "Hangul".

ETHIOPIC

```java
public static final
Character.UnicodeScript
ETHIOPIC
```

Unicode script "Ethiopic".

---

#### ETHIOPIC

public static final

Character.UnicodeScript

ETHIOPIC

Unicode script "Ethiopic".

CHEROKEE

```java
public static final
Character.UnicodeScript
CHEROKEE
```

Unicode script "Cherokee".

---

#### CHEROKEE

public static final

Character.UnicodeScript

CHEROKEE

Unicode script "Cherokee".

CANADIAN_ABORIGINAL

```java
public static final
Character.UnicodeScript
CANADIAN_ABORIGINAL
```

Unicode script "Canadian_Aboriginal".

---

#### CANADIAN_ABORIGINAL

public static final

Character.UnicodeScript

CANADIAN_ABORIGINAL

Unicode script "Canadian_Aboriginal".

OGHAM

```java
public static final
Character.UnicodeScript
OGHAM
```

Unicode script "Ogham".

---

#### OGHAM

public static final

Character.UnicodeScript

OGHAM

Unicode script "Ogham".

RUNIC

```java
public static final
Character.UnicodeScript
RUNIC
```

Unicode script "Runic".

---

#### RUNIC

public static final

Character.UnicodeScript

RUNIC

Unicode script "Runic".

KHMER

```java
public static final
Character.UnicodeScript
KHMER
```

Unicode script "Khmer".

---

#### KHMER

public static final

Character.UnicodeScript

KHMER

Unicode script "Khmer".

MONGOLIAN

```java
public static final
Character.UnicodeScript
MONGOLIAN
```

Unicode script "Mongolian".

---

#### MONGOLIAN

public static final

Character.UnicodeScript

MONGOLIAN

Unicode script "Mongolian".

HIRAGANA

```java
public static final
Character.UnicodeScript
HIRAGANA
```

Unicode script "Hiragana".

---

#### HIRAGANA

public static final

Character.UnicodeScript

HIRAGANA

Unicode script "Hiragana".

KATAKANA

```java
public static final
Character.UnicodeScript
KATAKANA
```

Unicode script "Katakana".

---

#### KATAKANA

public static final

Character.UnicodeScript

KATAKANA

Unicode script "Katakana".

BOPOMOFO

```java
public static final
Character.UnicodeScript
BOPOMOFO
```

Unicode script "Bopomofo".

---

#### BOPOMOFO

public static final

Character.UnicodeScript

BOPOMOFO

Unicode script "Bopomofo".

HAN

```java
public static final
Character.UnicodeScript
HAN
```

Unicode script "Han".

---

#### HAN

public static final

Character.UnicodeScript

HAN

Unicode script "Han".

YI

```java
public static final
Character.UnicodeScript
YI
```

Unicode script "Yi".

---

#### YI

public static final

Character.UnicodeScript

YI

Unicode script "Yi".

OLD_ITALIC

```java
public static final
Character.UnicodeScript
OLD_ITALIC
```

Unicode script "Old_Italic".

---

#### OLD_ITALIC

public static final

Character.UnicodeScript

OLD_ITALIC

Unicode script "Old_Italic".

GOTHIC

```java
public static final
Character.UnicodeScript
GOTHIC
```

Unicode script "Gothic".

---

#### GOTHIC

public static final

Character.UnicodeScript

GOTHIC

Unicode script "Gothic".

DESERET

```java
public static final
Character.UnicodeScript
DESERET
```

Unicode script "Deseret".

---

#### DESERET

public static final

Character.UnicodeScript

DESERET

Unicode script "Deseret".

INHERITED

```java
public static final
Character.UnicodeScript
INHERITED
```

Unicode script "Inherited".

---

#### INHERITED

public static final

Character.UnicodeScript

INHERITED

Unicode script "Inherited".

TAGALOG

```java
public static final
Character.UnicodeScript
TAGALOG
```

Unicode script "Tagalog".

---

#### TAGALOG

public static final

Character.UnicodeScript

TAGALOG

Unicode script "Tagalog".

HANUNOO

```java
public static final
Character.UnicodeScript
HANUNOO
```

Unicode script "Hanunoo".

---

#### HANUNOO

public static final

Character.UnicodeScript

HANUNOO

Unicode script "Hanunoo".

BUHID

```java
public static final
Character.UnicodeScript
BUHID
```

Unicode script "Buhid".

---

#### BUHID

public static final

Character.UnicodeScript

BUHID

Unicode script "Buhid".

TAGBANWA

```java
public static final
Character.UnicodeScript
TAGBANWA
```

Unicode script "Tagbanwa".

---

#### TAGBANWA

public static final

Character.UnicodeScript

TAGBANWA

Unicode script "Tagbanwa".

LIMBU

```java
public static final
Character.UnicodeScript
LIMBU
```

Unicode script "Limbu".

---

#### LIMBU

public static final

Character.UnicodeScript

LIMBU

Unicode script "Limbu".

TAI_LE

```java
public static final
Character.UnicodeScript
TAI_LE
```

Unicode script "Tai_Le".

---

#### TAI_LE

public static final

Character.UnicodeScript

TAI_LE

Unicode script "Tai_Le".

LINEAR_B

```java
public static final
Character.UnicodeScript
LINEAR_B
```

Unicode script "Linear_B".

---

#### LINEAR_B

public static final

Character.UnicodeScript

LINEAR_B

Unicode script "Linear_B".

UGARITIC

```java
public static final
Character.UnicodeScript
UGARITIC
```

Unicode script "Ugaritic".

---

#### UGARITIC

public static final

Character.UnicodeScript

UGARITIC

Unicode script "Ugaritic".

SHAVIAN

```java
public static final
Character.UnicodeScript
SHAVIAN
```

Unicode script "Shavian".

---

#### SHAVIAN

public static final

Character.UnicodeScript

SHAVIAN

Unicode script "Shavian".

OSMANYA

```java
public static final
Character.UnicodeScript
OSMANYA
```

Unicode script "Osmanya".

---

#### OSMANYA

public static final

Character.UnicodeScript

OSMANYA

Unicode script "Osmanya".

CYPRIOT

```java
public static final
Character.UnicodeScript
CYPRIOT
```

Unicode script "Cypriot".

---

#### CYPRIOT

public static final

Character.UnicodeScript

CYPRIOT

Unicode script "Cypriot".

BRAILLE

```java
public static final
Character.UnicodeScript
BRAILLE
```

Unicode script "Braille".

---

#### BRAILLE

public static final

Character.UnicodeScript

BRAILLE

Unicode script "Braille".

BUGINESE

```java
public static final
Character.UnicodeScript
BUGINESE
```

Unicode script "Buginese".

---

#### BUGINESE

public static final

Character.UnicodeScript

BUGINESE

Unicode script "Buginese".

COPTIC

```java
public static final
Character.UnicodeScript
COPTIC
```

Unicode script "Coptic".

---

#### COPTIC

public static final

Character.UnicodeScript

COPTIC

Unicode script "Coptic".

NEW_TAI_LUE

```java
public static final
Character.UnicodeScript
NEW_TAI_LUE
```

Unicode script "New_Tai_Lue".

---

#### NEW_TAI_LUE

public static final

Character.UnicodeScript

NEW_TAI_LUE

Unicode script "New_Tai_Lue".

GLAGOLITIC

```java
public static final
Character.UnicodeScript
GLAGOLITIC
```

Unicode script "Glagolitic".

---

#### GLAGOLITIC

public static final

Character.UnicodeScript

GLAGOLITIC

Unicode script "Glagolitic".

TIFINAGH

```java
public static final
Character.UnicodeScript
TIFINAGH
```

Unicode script "Tifinagh".

---

#### TIFINAGH

public static final

Character.UnicodeScript

TIFINAGH

Unicode script "Tifinagh".

SYLOTI_NAGRI

```java
public static final
Character.UnicodeScript
SYLOTI_NAGRI
```

Unicode script "Syloti_Nagri".

---

#### SYLOTI_NAGRI

public static final

Character.UnicodeScript

SYLOTI_NAGRI

Unicode script "Syloti_Nagri".

OLD_PERSIAN

```java
public static final
Character.UnicodeScript
OLD_PERSIAN
```

Unicode script "Old_Persian".

---

#### OLD_PERSIAN

public static final

Character.UnicodeScript

OLD_PERSIAN

Unicode script "Old_Persian".

KHAROSHTHI

```java
public static final
Character.UnicodeScript
KHAROSHTHI
```

Unicode script "Kharoshthi".

---

#### KHAROSHTHI

public static final

Character.UnicodeScript

KHAROSHTHI

Unicode script "Kharoshthi".

BALINESE

```java
public static final
Character.UnicodeScript
BALINESE
```

Unicode script "Balinese".

---

#### BALINESE

public static final

Character.UnicodeScript

BALINESE

Unicode script "Balinese".

CUNEIFORM

```java
public static final
Character.UnicodeScript
CUNEIFORM
```

Unicode script "Cuneiform".

---

#### CUNEIFORM

public static final

Character.UnicodeScript

CUNEIFORM

Unicode script "Cuneiform".

PHOENICIAN

```java
public static final
Character.UnicodeScript
PHOENICIAN
```

Unicode script "Phoenician".

---

#### PHOENICIAN

public static final

Character.UnicodeScript

PHOENICIAN

Unicode script "Phoenician".

PHAGS_PA

```java
public static final
Character.UnicodeScript
PHAGS_PA
```

Unicode script "Phags_Pa".

---

#### PHAGS_PA

public static final

Character.UnicodeScript

PHAGS_PA

Unicode script "Phags_Pa".

NKO

```java
public static final
Character.UnicodeScript
NKO
```

Unicode script "Nko".

---

#### NKO

public static final

Character.UnicodeScript

NKO

Unicode script "Nko".

SUNDANESE

```java
public static final
Character.UnicodeScript
SUNDANESE
```

Unicode script "Sundanese".

---

#### SUNDANESE

public static final

Character.UnicodeScript

SUNDANESE

Unicode script "Sundanese".

BATAK

```java
public static final
Character.UnicodeScript
BATAK
```

Unicode script "Batak".

---

#### BATAK

public static final

Character.UnicodeScript

BATAK

Unicode script "Batak".

LEPCHA

```java
public static final
Character.UnicodeScript
LEPCHA
```

Unicode script "Lepcha".

---

#### LEPCHA

public static final

Character.UnicodeScript

LEPCHA

Unicode script "Lepcha".

OL_CHIKI

```java
public static final
Character.UnicodeScript
OL_CHIKI
```

Unicode script "Ol_Chiki".

---

#### OL_CHIKI

public static final

Character.UnicodeScript

OL_CHIKI

Unicode script "Ol_Chiki".

VAI

```java
public static final
Character.UnicodeScript
VAI
```

Unicode script "Vai".

---

#### VAI

public static final

Character.UnicodeScript

VAI

Unicode script "Vai".

SAURASHTRA

```java
public static final
Character.UnicodeScript
SAURASHTRA
```

Unicode script "Saurashtra".

---

#### SAURASHTRA

public static final

Character.UnicodeScript

SAURASHTRA

Unicode script "Saurashtra".

KAYAH_LI

```java
public static final
Character.UnicodeScript
KAYAH_LI
```

Unicode script "Kayah_Li".

---

#### KAYAH_LI

public static final

Character.UnicodeScript

KAYAH_LI

Unicode script "Kayah_Li".

REJANG

```java
public static final
Character.UnicodeScript
REJANG
```

Unicode script "Rejang".

---

#### REJANG

public static final

Character.UnicodeScript

REJANG

Unicode script "Rejang".

LYCIAN

```java
public static final
Character.UnicodeScript
LYCIAN
```

Unicode script "Lycian".

---

#### LYCIAN

public static final

Character.UnicodeScript

LYCIAN

Unicode script "Lycian".

CARIAN

```java
public static final
Character.UnicodeScript
CARIAN
```

Unicode script "Carian".

---

#### CARIAN

public static final

Character.UnicodeScript

CARIAN

Unicode script "Carian".

LYDIAN

```java
public static final
Character.UnicodeScript
LYDIAN
```

Unicode script "Lydian".

---

#### LYDIAN

public static final

Character.UnicodeScript

LYDIAN

Unicode script "Lydian".

CHAM

```java
public static final
Character.UnicodeScript
CHAM
```

Unicode script "Cham".

---

#### CHAM

public static final

Character.UnicodeScript

CHAM

Unicode script "Cham".

TAI_THAM

```java
public static final
Character.UnicodeScript
TAI_THAM
```

Unicode script "Tai_Tham".

---

#### TAI_THAM

public static final

Character.UnicodeScript

TAI_THAM

Unicode script "Tai_Tham".

TAI_VIET

```java
public static final
Character.UnicodeScript
TAI_VIET
```

Unicode script "Tai_Viet".

---

#### TAI_VIET

public static final

Character.UnicodeScript

TAI_VIET

Unicode script "Tai_Viet".

AVESTAN

```java
public static final
Character.UnicodeScript
AVESTAN
```

Unicode script "Avestan".

---

#### AVESTAN

public static final

Character.UnicodeScript

AVESTAN

Unicode script "Avestan".

EGYPTIAN_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
EGYPTIAN_HIEROGLYPHS
```

Unicode script "Egyptian_Hieroglyphs".

---

#### EGYPTIAN_HIEROGLYPHS

public static final

Character.UnicodeScript

EGYPTIAN_HIEROGLYPHS

Unicode script "Egyptian_Hieroglyphs".

SAMARITAN

```java
public static final
Character.UnicodeScript
SAMARITAN
```

Unicode script "Samaritan".

---

#### SAMARITAN

public static final

Character.UnicodeScript

SAMARITAN

Unicode script "Samaritan".

MANDAIC

```java
public static final
Character.UnicodeScript
MANDAIC
```

Unicode script "Mandaic".

---

#### MANDAIC

public static final

Character.UnicodeScript

MANDAIC

Unicode script "Mandaic".

LISU

```java
public static final
Character.UnicodeScript
LISU
```

Unicode script "Lisu".

---

#### LISU

public static final

Character.UnicodeScript

LISU

Unicode script "Lisu".

BAMUM

```java
public static final
Character.UnicodeScript
BAMUM
```

Unicode script "Bamum".

---

#### BAMUM

public static final

Character.UnicodeScript

BAMUM

Unicode script "Bamum".

JAVANESE

```java
public static final
Character.UnicodeScript
JAVANESE
```

Unicode script "Javanese".

---

#### JAVANESE

public static final

Character.UnicodeScript

JAVANESE

Unicode script "Javanese".

MEETEI_MAYEK

```java
public static final
Character.UnicodeScript
MEETEI_MAYEK
```

Unicode script "Meetei_Mayek".

---

#### MEETEI_MAYEK

public static final

Character.UnicodeScript

MEETEI_MAYEK

Unicode script "Meetei_Mayek".

IMPERIAL_ARAMAIC

```java
public static final
Character.UnicodeScript
IMPERIAL_ARAMAIC
```

Unicode script "Imperial_Aramaic".

---

#### IMPERIAL_ARAMAIC

public static final

Character.UnicodeScript

IMPERIAL_ARAMAIC

Unicode script "Imperial_Aramaic".

OLD_SOUTH_ARABIAN

```java
public static final
Character.UnicodeScript
OLD_SOUTH_ARABIAN
```

Unicode script "Old_South_Arabian".

---

#### OLD_SOUTH_ARABIAN

public static final

Character.UnicodeScript

OLD_SOUTH_ARABIAN

Unicode script "Old_South_Arabian".

INSCRIPTIONAL_PARTHIAN

```java
public static final
Character.UnicodeScript
INSCRIPTIONAL_PARTHIAN
```

Unicode script "Inscriptional_Parthian".

---

#### INSCRIPTIONAL_PARTHIAN

public static final

Character.UnicodeScript

INSCRIPTIONAL_PARTHIAN

Unicode script "Inscriptional_Parthian".

INSCRIPTIONAL_PAHLAVI

```java
public static final
Character.UnicodeScript
INSCRIPTIONAL_PAHLAVI
```

Unicode script "Inscriptional_Pahlavi".

---

#### INSCRIPTIONAL_PAHLAVI

public static final

Character.UnicodeScript

INSCRIPTIONAL_PAHLAVI

Unicode script "Inscriptional_Pahlavi".

OLD_TURKIC

```java
public static final
Character.UnicodeScript
OLD_TURKIC
```

Unicode script "Old_Turkic".

---

#### OLD_TURKIC

public static final

Character.UnicodeScript

OLD_TURKIC

Unicode script "Old_Turkic".

BRAHMI

```java
public static final
Character.UnicodeScript
BRAHMI
```

Unicode script "Brahmi".

---

#### BRAHMI

public static final

Character.UnicodeScript

BRAHMI

Unicode script "Brahmi".

KAITHI

```java
public static final
Character.UnicodeScript
KAITHI
```

Unicode script "Kaithi".

---

#### KAITHI

public static final

Character.UnicodeScript

KAITHI

Unicode script "Kaithi".

MEROITIC_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
MEROITIC_HIEROGLYPHS
```

Unicode script "Meroitic Hieroglyphs".

**Since:** 1.8

---

#### MEROITIC_HIEROGLYPHS

public static final

Character.UnicodeScript

MEROITIC_HIEROGLYPHS

Unicode script "Meroitic Hieroglyphs".

MEROITIC_CURSIVE

```java
public static final
Character.UnicodeScript
MEROITIC_CURSIVE
```

Unicode script "Meroitic Cursive".

**Since:** 1.8

---

#### MEROITIC_CURSIVE

public static final

Character.UnicodeScript

MEROITIC_CURSIVE

Unicode script "Meroitic Cursive".

SORA_SOMPENG

```java
public static final
Character.UnicodeScript
SORA_SOMPENG
```

Unicode script "Sora Sompeng".

**Since:** 1.8

---

#### SORA_SOMPENG

public static final

Character.UnicodeScript

SORA_SOMPENG

Unicode script "Sora Sompeng".

CHAKMA

```java
public static final
Character.UnicodeScript
CHAKMA
```

Unicode script "Chakma".

**Since:** 1.8

---

#### CHAKMA

public static final

Character.UnicodeScript

CHAKMA

Unicode script "Chakma".

SHARADA

```java
public static final
Character.UnicodeScript
SHARADA
```

Unicode script "Sharada".

**Since:** 1.8

---

#### SHARADA

public static final

Character.UnicodeScript

SHARADA

Unicode script "Sharada".

TAKRI

```java
public static final
Character.UnicodeScript
TAKRI
```

Unicode script "Takri".

**Since:** 1.8

---

#### TAKRI

public static final

Character.UnicodeScript

TAKRI

Unicode script "Takri".

MIAO

```java
public static final
Character.UnicodeScript
MIAO
```

Unicode script "Miao".

**Since:** 1.8

---

#### MIAO

public static final

Character.UnicodeScript

MIAO

Unicode script "Miao".

CAUCASIAN_ALBANIAN

```java
public static final
Character.UnicodeScript
CAUCASIAN_ALBANIAN
```

Unicode script "Caucasian Albanian".

**Since:** 9

---

#### CAUCASIAN_ALBANIAN

public static final

Character.UnicodeScript

CAUCASIAN_ALBANIAN

Unicode script "Caucasian Albanian".

BASSA_VAH

```java
public static final
Character.UnicodeScript
BASSA_VAH
```

Unicode script "Bassa Vah".

**Since:** 9

---

#### BASSA_VAH

public static final

Character.UnicodeScript

BASSA_VAH

Unicode script "Bassa Vah".

DUPLOYAN

```java
public static final
Character.UnicodeScript
DUPLOYAN
```

Unicode script "Duployan".

**Since:** 9

---

#### DUPLOYAN

public static final

Character.UnicodeScript

DUPLOYAN

Unicode script "Duployan".

ELBASAN

```java
public static final
Character.UnicodeScript
ELBASAN
```

Unicode script "Elbasan".

**Since:** 9

---

#### ELBASAN

public static final

Character.UnicodeScript

ELBASAN

Unicode script "Elbasan".

GRANTHA

```java
public static final
Character.UnicodeScript
GRANTHA
```

Unicode script "Grantha".

**Since:** 9

---

#### GRANTHA

public static final

Character.UnicodeScript

GRANTHA

Unicode script "Grantha".

PAHAWH_HMONG

```java
public static final
Character.UnicodeScript
PAHAWH_HMONG
```

Unicode script "Pahawh Hmong".

**Since:** 9

---

#### PAHAWH_HMONG

public static final

Character.UnicodeScript

PAHAWH_HMONG

Unicode script "Pahawh Hmong".

KHOJKI

```java
public static final
Character.UnicodeScript
KHOJKI
```

Unicode script "Khojki".

**Since:** 9

---

#### KHOJKI

public static final

Character.UnicodeScript

KHOJKI

Unicode script "Khojki".

LINEAR_A

```java
public static final
Character.UnicodeScript
LINEAR_A
```

Unicode script "Linear A".

**Since:** 9

---

#### LINEAR_A

public static final

Character.UnicodeScript

LINEAR_A

Unicode script "Linear A".

MAHAJANI

```java
public static final
Character.UnicodeScript
MAHAJANI
```

Unicode script "Mahajani".

**Since:** 9

---

#### MAHAJANI

public static final

Character.UnicodeScript

MAHAJANI

Unicode script "Mahajani".

MANICHAEAN

```java
public static final
Character.UnicodeScript
MANICHAEAN
```

Unicode script "Manichaean".

**Since:** 9

---

#### MANICHAEAN

public static final

Character.UnicodeScript

MANICHAEAN

Unicode script "Manichaean".

MENDE_KIKAKUI

```java
public static final
Character.UnicodeScript
MENDE_KIKAKUI
```

Unicode script "Mende Kikakui".

**Since:** 9

---

#### MENDE_KIKAKUI

public static final

Character.UnicodeScript

MENDE_KIKAKUI

Unicode script "Mende Kikakui".

MODI

```java
public static final
Character.UnicodeScript
MODI
```

Unicode script "Modi".

**Since:** 9

---

#### MODI

public static final

Character.UnicodeScript

MODI

Unicode script "Modi".

MRO

```java
public static final
Character.UnicodeScript
MRO
```

Unicode script "Mro".

**Since:** 9

---

#### MRO

public static final

Character.UnicodeScript

MRO

Unicode script "Mro".

OLD_NORTH_ARABIAN

```java
public static final
Character.UnicodeScript
OLD_NORTH_ARABIAN
```

Unicode script "Old North Arabian".

**Since:** 9

---

#### OLD_NORTH_ARABIAN

public static final

Character.UnicodeScript

OLD_NORTH_ARABIAN

Unicode script "Old North Arabian".

NABATAEAN

```java
public static final
Character.UnicodeScript
NABATAEAN
```

Unicode script "Nabataean".

**Since:** 9

---

#### NABATAEAN

public static final

Character.UnicodeScript

NABATAEAN

Unicode script "Nabataean".

PALMYRENE

```java
public static final
Character.UnicodeScript
PALMYRENE
```

Unicode script "Palmyrene".

**Since:** 9

---

#### PALMYRENE

public static final

Character.UnicodeScript

PALMYRENE

Unicode script "Palmyrene".

PAU_CIN_HAU

```java
public static final
Character.UnicodeScript
PAU_CIN_HAU
```

Unicode script "Pau Cin Hau".

**Since:** 9

---

#### PAU_CIN_HAU

public static final

Character.UnicodeScript

PAU_CIN_HAU

Unicode script "Pau Cin Hau".

OLD_PERMIC

```java
public static final
Character.UnicodeScript
OLD_PERMIC
```

Unicode script "Old Permic".

**Since:** 9

---

#### OLD_PERMIC

public static final

Character.UnicodeScript

OLD_PERMIC

Unicode script "Old Permic".

PSALTER_PAHLAVI

```java
public static final
Character.UnicodeScript
PSALTER_PAHLAVI
```

Unicode script "Psalter Pahlavi".

**Since:** 9

---

#### PSALTER_PAHLAVI

public static final

Character.UnicodeScript

PSALTER_PAHLAVI

Unicode script "Psalter Pahlavi".

SIDDHAM

```java
public static final
Character.UnicodeScript
SIDDHAM
```

Unicode script "Siddham".

**Since:** 9

---

#### SIDDHAM

public static final

Character.UnicodeScript

SIDDHAM

Unicode script "Siddham".

KHUDAWADI

```java
public static final
Character.UnicodeScript
KHUDAWADI
```

Unicode script "Khudawadi".

**Since:** 9

---

#### KHUDAWADI

public static final

Character.UnicodeScript

KHUDAWADI

Unicode script "Khudawadi".

TIRHUTA

```java
public static final
Character.UnicodeScript
TIRHUTA
```

Unicode script "Tirhuta".

**Since:** 9

---

#### TIRHUTA

public static final

Character.UnicodeScript

TIRHUTA

Unicode script "Tirhuta".

WARANG_CITI

```java
public static final
Character.UnicodeScript
WARANG_CITI
```

Unicode script "Warang Citi".

**Since:** 9

---

#### WARANG_CITI

public static final

Character.UnicodeScript

WARANG_CITI

Unicode script "Warang Citi".

AHOM

```java
public static final
Character.UnicodeScript
AHOM
```

Unicode script "Ahom".

**Since:** 9

---

#### AHOM

public static final

Character.UnicodeScript

AHOM

Unicode script "Ahom".

ANATOLIAN_HIEROGLYPHS

```java
public static final
Character.UnicodeScript
ANATOLIAN_HIEROGLYPHS
```

Unicode script "Anatolian Hieroglyphs".

**Since:** 9

---

#### ANATOLIAN_HIEROGLYPHS

public static final

Character.UnicodeScript

ANATOLIAN_HIEROGLYPHS

Unicode script "Anatolian Hieroglyphs".

HATRAN

```java
public static final
Character.UnicodeScript
HATRAN
```

Unicode script "Hatran".

**Since:** 9

---

#### HATRAN

public static final

Character.UnicodeScript

HATRAN

Unicode script "Hatran".

MULTANI

```java
public static final
Character.UnicodeScript
MULTANI
```

Unicode script "Multani".

**Since:** 9

---

#### MULTANI

public static final

Character.UnicodeScript

MULTANI

Unicode script "Multani".

OLD_HUNGARIAN

```java
public static final
Character.UnicodeScript
OLD_HUNGARIAN
```

Unicode script "Old Hungarian".

**Since:** 9

---

#### OLD_HUNGARIAN

public static final

Character.UnicodeScript

OLD_HUNGARIAN

Unicode script "Old Hungarian".

SIGNWRITING

```java
public static final
Character.UnicodeScript
SIGNWRITING
```

Unicode script "SignWriting".

**Since:** 9

---

#### SIGNWRITING

public static final

Character.UnicodeScript

SIGNWRITING

Unicode script "SignWriting".

ADLAM

```java
public static final
Character.UnicodeScript
ADLAM
```

Unicode script "Adlam".

**Since:** 11

---

#### ADLAM

public static final

Character.UnicodeScript

ADLAM

Unicode script "Adlam".

BHAIKSUKI

```java
public static final
Character.UnicodeScript
BHAIKSUKI
```

Unicode script "Bhaiksuki".

**Since:** 11

---

#### BHAIKSUKI

public static final

Character.UnicodeScript

BHAIKSUKI

Unicode script "Bhaiksuki".

MARCHEN

```java
public static final
Character.UnicodeScript
MARCHEN
```

Unicode script "Marchen".

**Since:** 11

---

#### MARCHEN

public static final

Character.UnicodeScript

MARCHEN

Unicode script "Marchen".

NEWA

```java
public static final
Character.UnicodeScript
NEWA
```

Unicode script "Newa".

**Since:** 11

---

#### NEWA

public static final

Character.UnicodeScript

NEWA

Unicode script "Newa".

OSAGE

```java
public static final
Character.UnicodeScript
OSAGE
```

Unicode script "Osage".

**Since:** 11

---

#### OSAGE

public static final

Character.UnicodeScript

OSAGE

Unicode script "Osage".

TANGUT

```java
public static final
Character.UnicodeScript
TANGUT
```

Unicode script "Tangut".

**Since:** 11

---

#### TANGUT

public static final

Character.UnicodeScript

TANGUT

Unicode script "Tangut".

MASARAM_GONDI

```java
public static final
Character.UnicodeScript
MASARAM_GONDI
```

Unicode script "Masaram Gondi".

**Since:** 11

---

#### MASARAM_GONDI

public static final

Character.UnicodeScript

MASARAM_GONDI

Unicode script "Masaram Gondi".

NUSHU

```java
public static final
Character.UnicodeScript
NUSHU
```

Unicode script "Nushu".

**Since:** 11

---

#### NUSHU

public static final

Character.UnicodeScript

NUSHU

Unicode script "Nushu".

SOYOMBO

```java
public static final
Character.UnicodeScript
SOYOMBO
```

Unicode script "Soyombo".

**Since:** 11

---

#### SOYOMBO

public static final

Character.UnicodeScript

SOYOMBO

Unicode script "Soyombo".

ZANABAZAR_SQUARE

```java
public static final
Character.UnicodeScript
ZANABAZAR_SQUARE
```

Unicode script "Zanabazar Square".

**Since:** 11

---

#### ZANABAZAR_SQUARE

public static final

Character.UnicodeScript

ZANABAZAR_SQUARE

Unicode script "Zanabazar Square".

UNKNOWN

```java
public static final
Character.UnicodeScript
UNKNOWN
```

Unicode script "Unknown".

---

#### UNKNOWN

public static final

Character.UnicodeScript

UNKNOWN

Unicode script "Unknown".

Method Detail

- values

```java
public static
Character.UnicodeScript
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Character.UnicodeScript c : Character.UnicodeScript.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Character.UnicodeScript
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

- of

```java
public static
Character.UnicodeScript
of​(int codePoint)
```

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

**Parameters:** codePoint

- the character (Unicode code point) in question.
**Returns:** The

UnicodeScript

constant representing the
Unicode script of which this character is assigned to.
**Throws:** IllegalArgumentException

- if the specified

codePoint

is an invalid Unicode code point.
**See Also:** Character.isValidCodePoint(int)

- forName

```java
public static final
Character.UnicodeScript
forName​(
String
scriptName)
```

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias. Script names and their aliases are
determined by The Unicode Standard. The files

Scripts<version>.txt

and

PropertyValueAliases<version>.txt

define script names
and the script name aliases for a particular version of the
standard. The

Character

class specifies the version of
the standard that it supports.

Character case is ignored for all of the valid script names.
The en_US locale's case mapping rules are used to provide
case-insensitive string comparisons for script name validation.

**Parameters:** scriptName

- A

UnicodeScript

name.
**Returns:** The

UnicodeScript

constant identified
by

scriptName
**Throws:** IllegalArgumentException

- if

scriptName

is an
invalid name
**Throws:** NullPointerException

- if

scriptName

is null

---

#### Method Detail

values

```java
public static
Character.UnicodeScript
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Character.UnicodeScript c : Character.UnicodeScript.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Character.UnicodeScript

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Character.UnicodeScript c : Character.UnicodeScript.values())
System.out.println(c);
```

for (Character.UnicodeScript c : Character.UnicodeScript.values())
System.out.println(c);

valueOf

```java
public static
Character.UnicodeScript
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

Character.UnicodeScript

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

of

```java
public static
Character.UnicodeScript
of​(int codePoint)
```

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

**Parameters:** codePoint

- the character (Unicode code point) in question.
**Returns:** The

UnicodeScript

constant representing the
Unicode script of which this character is assigned to.
**Throws:** IllegalArgumentException

- if the specified

codePoint

is an invalid Unicode code point.
**See Also:** Character.isValidCodePoint(int)

---

#### of

public static

Character.UnicodeScript

of​(int codePoint)

Returns the enum constant representing the Unicode script of which
the given character (Unicode code point) is assigned to.

forName

```java
public static final
Character.UnicodeScript
forName​(
String
scriptName)
```

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias. Script names and their aliases are
determined by The Unicode Standard. The files

Scripts<version>.txt

and

PropertyValueAliases<version>.txt

define script names
and the script name aliases for a particular version of the
standard. The

Character

class specifies the version of
the standard that it supports.

Character case is ignored for all of the valid script names.
The en_US locale's case mapping rules are used to provide
case-insensitive string comparisons for script name validation.

**Parameters:** scriptName

- A

UnicodeScript

name.
**Returns:** The

UnicodeScript

constant identified
by

scriptName
**Throws:** IllegalArgumentException

- if

scriptName

is an
invalid name
**Throws:** NullPointerException

- if

scriptName

is null

---

#### forName

public static final

Character.UnicodeScript

forName​(

String

scriptName)

Returns the UnicodeScript constant with the given Unicode script
name or the script name alias. Script names and their aliases are
determined by The Unicode Standard. The files

Scripts<version>.txt

and

PropertyValueAliases<version>.txt

define script names
and the script name aliases for a particular version of the
standard. The

Character

class specifies the version of
the standard that it supports.

Character case is ignored for all of the valid script names.
The en_US locale's case mapping rules are used to provide
case-insensitive string comparisons for script name validation.

Character case is ignored for all of the valid script names.
The en_US locale's case mapping rules are used to provide
case-insensitive string comparisons for script name validation.

---

