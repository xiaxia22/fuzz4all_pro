# Class DecimalStyle

**Source:** `java.base\java\time\format\DecimalStyle.html`

### Class Description

```java
public final class
DecimalStyle

extends
Object
```

Localized decimal style used in date and time formatting.

A significant part of dealing with dates and times is the localization.
This class acts as a central point for accessing the information.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8

---

### Field Details

#### public static final
DecimalStyle
STANDARD

The standard set of non-localized decimal style symbols.

This uses standard ASCII characters for zero, positive, negative and a dot for the decimal point.

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
Set
<
Locale
> getAvailableLocales()

Lists all the locales that are supported.

The locale 'en_US' will always be present.

**Returns:**
- a Set of Locales for which localization is supported

---

#### public static
DecimalStyle
ofDefaultLocale()

Obtains the DecimalStyle for the default

FORMAT

locale.

This method provides access to locale sensitive decimal style symbols.

This is equivalent to calling

of(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:**
- the decimal style, not null

**See Also:**
- Locale.Category.FORMAT

---

#### public static
DecimalStyle
of​(
Locale
locale)

Obtains the DecimalStyle for the specified locale.

This method provides access to locale sensitive decimal style symbols.
If the locale contains "nu" (Numbering System) and/or "rg"
(Region Override)

Unicode extensions

, returned instance will reflect the values specified with
those extensions. If both "nu" and "rg" are specified, the value from
the "nu" extension supersedes the implicit one from the "rg" extension.

**Parameters:**
- locale

- the locale, not null

**Returns:**
- the decimal style, not null

---

#### public char getZeroDigit()

Gets the character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Returns:**
- the character for zero

---

#### public
DecimalStyle
withZeroDigit​(char zeroDigit)

Returns a copy of the info with a new character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Parameters:**
- zeroDigit

- the character for zero

**Returns:**
- a copy with a new character that represents zero, not null

---

#### public char getPositiveSign()

Gets the character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Returns:**
- the character for the positive sign

---

#### public
DecimalStyle
withPositiveSign​(char positiveSign)

Returns a copy of the info with a new character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Parameters:**
- positiveSign

- the character for the positive sign

**Returns:**
- a copy with a new character that represents the positive sign, not null

---

#### public char getNegativeSign()

Gets the character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Returns:**
- the character for the negative sign

---

#### public
DecimalStyle
withNegativeSign​(char negativeSign)

Returns a copy of the info with a new character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Parameters:**
- negativeSign

- the character for the negative sign

**Returns:**
- a copy with a new character that represents the negative sign, not null

---

#### public char getDecimalSeparator()

Gets the character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Returns:**
- the character for the decimal point

---

#### public
DecimalStyle
withDecimalSeparator​(char decimalSeparator)

Returns a copy of the info with a new character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Parameters:**
- decimalSeparator

- the character for the decimal point

**Returns:**
- a copy with a new character that represents the decimal point, not null

---

#### public boolean equals​(
Object
obj)

Checks if this DecimalStyle is equal to another DecimalStyle.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to check, null returns false

**Returns:**
- true if this is equal to the other date

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

A hash code for this DecimalStyle.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a suitable hash code

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string describing this DecimalStyle.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string description, not null

---

### Additional Sections

#### Class DecimalStyle

java.lang.Object

- java.time.format.DecimalStyle

java.time.format.DecimalStyle

```java
public final class
DecimalStyle

extends
Object
```

Localized decimal style used in date and time formatting.

A significant part of dealing with dates and times is the localization.
This class acts as a central point for accessing the information.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8

public final class

DecimalStyle

extends

Object

Localized decimal style used in date and time formatting.

A significant part of dealing with dates and times is the localization.
This class acts as a central point for accessing the information.

A significant part of dealing with dates and times is the localization.
This class acts as a central point for accessing the information.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

DecimalStyle

STANDARD

The standard set of non-localized decimal style symbols.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks if this DecimalStyle is equal to another DecimalStyle.

static

Set

<

Locale

>

getAvailableLocales

()

Lists all the locales that are supported.

char

getDecimalSeparator

()

Gets the character that represents the decimal point.

char

getNegativeSign

()

Gets the character that represents the negative sign.

char

getPositiveSign

()

Gets the character that represents the positive sign.

char

getZeroDigit

()

Gets the character that represents zero.

int

hashCode

()

A hash code for this DecimalStyle.

static

DecimalStyle

of

​(

Locale

locale)

Obtains the DecimalStyle for the specified locale.

static

DecimalStyle

ofDefaultLocale

()

Obtains the DecimalStyle for the default

FORMAT

locale.

String

toString

()

Returns a string describing this DecimalStyle.

DecimalStyle

withDecimalSeparator

​(char decimalSeparator)

Returns a copy of the info with a new character that represents the decimal point.

DecimalStyle

withNegativeSign

​(char negativeSign)

Returns a copy of the info with a new character that represents the negative sign.

DecimalStyle

withPositiveSign

​(char positiveSign)

Returns a copy of the info with a new character that represents the positive sign.

DecimalStyle

withZeroDigit

​(char zeroDigit)

Returns a copy of the info with a new character that represents zero.

- Methods declared in class java.lang.

Object

clone

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

DecimalStyle

STANDARD

The standard set of non-localized decimal style symbols.

---

#### Field Summary

The standard set of non-localized decimal style symbols.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks if this DecimalStyle is equal to another DecimalStyle.

static

Set

<

Locale

>

getAvailableLocales

()

Lists all the locales that are supported.

char

getDecimalSeparator

()

Gets the character that represents the decimal point.

char

getNegativeSign

()

Gets the character that represents the negative sign.

char

getPositiveSign

()

Gets the character that represents the positive sign.

char

getZeroDigit

()

Gets the character that represents zero.

int

hashCode

()

A hash code for this DecimalStyle.

static

DecimalStyle

of

​(

Locale

locale)

Obtains the DecimalStyle for the specified locale.

static

DecimalStyle

ofDefaultLocale

()

Obtains the DecimalStyle for the default

FORMAT

locale.

String

toString

()

Returns a string describing this DecimalStyle.

DecimalStyle

withDecimalSeparator

​(char decimalSeparator)

Returns a copy of the info with a new character that represents the decimal point.

DecimalStyle

withNegativeSign

​(char negativeSign)

Returns a copy of the info with a new character that represents the negative sign.

DecimalStyle

withPositiveSign

​(char positiveSign)

Returns a copy of the info with a new character that represents the positive sign.

DecimalStyle

withZeroDigit

​(char zeroDigit)

Returns a copy of the info with a new character that represents zero.

- Methods declared in class java.lang.

Object

clone

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

Checks if this DecimalStyle is equal to another DecimalStyle.

Lists all the locales that are supported.

Gets the character that represents the decimal point.

Gets the character that represents the negative sign.

Gets the character that represents the positive sign.

Gets the character that represents zero.

A hash code for this DecimalStyle.

Obtains the DecimalStyle for the specified locale.

Obtains the DecimalStyle for the default

FORMAT

locale.

Returns a string describing this DecimalStyle.

Returns a copy of the info with a new character that represents the decimal point.

Returns a copy of the info with a new character that represents the negative sign.

Returns a copy of the info with a new character that represents the positive sign.

Returns a copy of the info with a new character that represents zero.

Methods declared in class java.lang.

Object

clone

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

- STANDARD

```java
public static final
DecimalStyle
STANDARD
```

The standard set of non-localized decimal style symbols.

This uses standard ASCII characters for zero, positive, negative and a dot for the decimal point.

============ METHOD DETAIL ==========

- Method Detail

- getAvailableLocales

```java
public static
Set
<
Locale
> getAvailableLocales()
```

Lists all the locales that are supported.

The locale 'en_US' will always be present.

**Returns:** a Set of Locales for which localization is supported

- ofDefaultLocale

```java
public static
DecimalStyle
ofDefaultLocale()
```

Obtains the DecimalStyle for the default

FORMAT

locale.

This method provides access to locale sensitive decimal style symbols.

This is equivalent to calling

of(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:** the decimal style, not null
**See Also:** Locale.Category.FORMAT

- of

```java
public static
DecimalStyle
of​(
Locale
locale)
```

Obtains the DecimalStyle for the specified locale.

This method provides access to locale sensitive decimal style symbols.
If the locale contains "nu" (Numbering System) and/or "rg"
(Region Override)

Unicode extensions

, returned instance will reflect the values specified with
those extensions. If both "nu" and "rg" are specified, the value from
the "nu" extension supersedes the implicit one from the "rg" extension.

**Parameters:** locale

- the locale, not null
**Returns:** the decimal style, not null

- getZeroDigit

```java
public char getZeroDigit()
```

Gets the character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Returns:** the character for zero

- withZeroDigit

```java
public
DecimalStyle
withZeroDigit​(char zeroDigit)
```

Returns a copy of the info with a new character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Parameters:** zeroDigit

- the character for zero
**Returns:** a copy with a new character that represents zero, not null

- getPositiveSign

```java
public char getPositiveSign()
```

Gets the character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Returns:** the character for the positive sign

- withPositiveSign

```java
public
DecimalStyle
withPositiveSign​(char positiveSign)
```

Returns a copy of the info with a new character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Parameters:** positiveSign

- the character for the positive sign
**Returns:** a copy with a new character that represents the positive sign, not null

- getNegativeSign

```java
public char getNegativeSign()
```

Gets the character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Returns:** the character for the negative sign

- withNegativeSign

```java
public
DecimalStyle
withNegativeSign​(char negativeSign)
```

Returns a copy of the info with a new character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Parameters:** negativeSign

- the character for the negative sign
**Returns:** a copy with a new character that represents the negative sign, not null

- getDecimalSeparator

```java
public char getDecimalSeparator()
```

Gets the character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Returns:** the character for the decimal point

- withDecimalSeparator

```java
public
DecimalStyle
withDecimalSeparator​(char decimalSeparator)
```

Returns a copy of the info with a new character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Parameters:** decimalSeparator

- the character for the decimal point
**Returns:** a copy with a new character that represents the decimal point, not null

- equals

```java
public boolean equals​(
Object
obj)
```

Checks if this DecimalStyle is equal to another DecimalStyle.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to check, null returns false
**Returns:** true if this is equal to the other date
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

A hash code for this DecimalStyle.

**Overrides:** hashCode

in class

Object
**Returns:** a suitable hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing this DecimalStyle.

**Overrides:** toString

in class

Object
**Returns:** a string description, not null

Field Detail

- STANDARD

```java
public static final
DecimalStyle
STANDARD
```

The standard set of non-localized decimal style symbols.

This uses standard ASCII characters for zero, positive, negative and a dot for the decimal point.

---

#### Field Detail

STANDARD

```java
public static final
DecimalStyle
STANDARD
```

The standard set of non-localized decimal style symbols.

This uses standard ASCII characters for zero, positive, negative and a dot for the decimal point.

---

#### STANDARD

public static final

DecimalStyle

STANDARD

The standard set of non-localized decimal style symbols.

This uses standard ASCII characters for zero, positive, negative and a dot for the decimal point.

This uses standard ASCII characters for zero, positive, negative and a dot for the decimal point.

Method Detail

- getAvailableLocales

```java
public static
Set
<
Locale
> getAvailableLocales()
```

Lists all the locales that are supported.

The locale 'en_US' will always be present.

**Returns:** a Set of Locales for which localization is supported

- ofDefaultLocale

```java
public static
DecimalStyle
ofDefaultLocale()
```

Obtains the DecimalStyle for the default

FORMAT

locale.

This method provides access to locale sensitive decimal style symbols.

This is equivalent to calling

of(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:** the decimal style, not null
**See Also:** Locale.Category.FORMAT

- of

```java
public static
DecimalStyle
of​(
Locale
locale)
```

Obtains the DecimalStyle for the specified locale.

This method provides access to locale sensitive decimal style symbols.
If the locale contains "nu" (Numbering System) and/or "rg"
(Region Override)

Unicode extensions

, returned instance will reflect the values specified with
those extensions. If both "nu" and "rg" are specified, the value from
the "nu" extension supersedes the implicit one from the "rg" extension.

**Parameters:** locale

- the locale, not null
**Returns:** the decimal style, not null

- getZeroDigit

```java
public char getZeroDigit()
```

Gets the character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Returns:** the character for zero

- withZeroDigit

```java
public
DecimalStyle
withZeroDigit​(char zeroDigit)
```

Returns a copy of the info with a new character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Parameters:** zeroDigit

- the character for zero
**Returns:** a copy with a new character that represents zero, not null

- getPositiveSign

```java
public char getPositiveSign()
```

Gets the character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Returns:** the character for the positive sign

- withPositiveSign

```java
public
DecimalStyle
withPositiveSign​(char positiveSign)
```

Returns a copy of the info with a new character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Parameters:** positiveSign

- the character for the positive sign
**Returns:** a copy with a new character that represents the positive sign, not null

- getNegativeSign

```java
public char getNegativeSign()
```

Gets the character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Returns:** the character for the negative sign

- withNegativeSign

```java
public
DecimalStyle
withNegativeSign​(char negativeSign)
```

Returns a copy of the info with a new character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Parameters:** negativeSign

- the character for the negative sign
**Returns:** a copy with a new character that represents the negative sign, not null

- getDecimalSeparator

```java
public char getDecimalSeparator()
```

Gets the character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Returns:** the character for the decimal point

- withDecimalSeparator

```java
public
DecimalStyle
withDecimalSeparator​(char decimalSeparator)
```

Returns a copy of the info with a new character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Parameters:** decimalSeparator

- the character for the decimal point
**Returns:** a copy with a new character that represents the decimal point, not null

- equals

```java
public boolean equals​(
Object
obj)
```

Checks if this DecimalStyle is equal to another DecimalStyle.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to check, null returns false
**Returns:** true if this is equal to the other date
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

A hash code for this DecimalStyle.

**Overrides:** hashCode

in class

Object
**Returns:** a suitable hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing this DecimalStyle.

**Overrides:** toString

in class

Object
**Returns:** a string description, not null

---

#### Method Detail

getAvailableLocales

```java
public static
Set
<
Locale
> getAvailableLocales()
```

Lists all the locales that are supported.

The locale 'en_US' will always be present.

**Returns:** a Set of Locales for which localization is supported

---

#### getAvailableLocales

public static

Set

<

Locale

> getAvailableLocales()

Lists all the locales that are supported.

The locale 'en_US' will always be present.

The locale 'en_US' will always be present.

ofDefaultLocale

```java
public static
DecimalStyle
ofDefaultLocale()
```

Obtains the DecimalStyle for the default

FORMAT

locale.

This method provides access to locale sensitive decimal style symbols.

This is equivalent to calling

of(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:** the decimal style, not null
**See Also:** Locale.Category.FORMAT

---

#### ofDefaultLocale

public static

DecimalStyle

ofDefaultLocale()

Obtains the DecimalStyle for the default

FORMAT

locale.

This method provides access to locale sensitive decimal style symbols.

This is equivalent to calling

of(Locale.getDefault(Locale.Category.FORMAT))

.

This method provides access to locale sensitive decimal style symbols.

This is equivalent to calling

of(Locale.getDefault(Locale.Category.FORMAT))

.

This is equivalent to calling

of(Locale.getDefault(Locale.Category.FORMAT))

.

of

```java
public static
DecimalStyle
of​(
Locale
locale)
```

Obtains the DecimalStyle for the specified locale.

This method provides access to locale sensitive decimal style symbols.
If the locale contains "nu" (Numbering System) and/or "rg"
(Region Override)

Unicode extensions

, returned instance will reflect the values specified with
those extensions. If both "nu" and "rg" are specified, the value from
the "nu" extension supersedes the implicit one from the "rg" extension.

**Parameters:** locale

- the locale, not null
**Returns:** the decimal style, not null

---

#### of

public static

DecimalStyle

of​(

Locale

locale)

Obtains the DecimalStyle for the specified locale.

This method provides access to locale sensitive decimal style symbols.
If the locale contains "nu" (Numbering System) and/or "rg"
(Region Override)

Unicode extensions

, returned instance will reflect the values specified with
those extensions. If both "nu" and "rg" are specified, the value from
the "nu" extension supersedes the implicit one from the "rg" extension.

This method provides access to locale sensitive decimal style symbols.
If the locale contains "nu" (Numbering System) and/or "rg"
(Region Override)

Unicode extensions

, returned instance will reflect the values specified with
those extensions. If both "nu" and "rg" are specified, the value from
the "nu" extension supersedes the implicit one from the "rg" extension.

getZeroDigit

```java
public char getZeroDigit()
```

Gets the character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Returns:** the character for zero

---

#### getZeroDigit

public char getZeroDigit()

Gets the character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

withZeroDigit

```java
public
DecimalStyle
withZeroDigit​(char zeroDigit)
```

Returns a copy of the info with a new character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

**Parameters:** zeroDigit

- the character for zero
**Returns:** a copy with a new character that represents zero, not null

---

#### withZeroDigit

public

DecimalStyle

withZeroDigit​(char zeroDigit)

Returns a copy of the info with a new character that represents zero.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

The character used to represent digits may vary by culture.
This method specifies the zero character to use, which implies the characters for one to nine.

getPositiveSign

```java
public char getPositiveSign()
```

Gets the character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Returns:** the character for the positive sign

---

#### getPositiveSign

public char getPositiveSign()

Gets the character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

withPositiveSign

```java
public
DecimalStyle
withPositiveSign​(char positiveSign)
```

Returns a copy of the info with a new character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

**Parameters:** positiveSign

- the character for the positive sign
**Returns:** a copy with a new character that represents the positive sign, not null

---

#### withPositiveSign

public

DecimalStyle

withPositiveSign​(char positiveSign)

Returns a copy of the info with a new character that represents the positive sign.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

The character used to represent a positive number may vary by culture.
This method specifies the character to use.

getNegativeSign

```java
public char getNegativeSign()
```

Gets the character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Returns:** the character for the negative sign

---

#### getNegativeSign

public char getNegativeSign()

Gets the character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

withNegativeSign

```java
public
DecimalStyle
withNegativeSign​(char negativeSign)
```

Returns a copy of the info with a new character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

**Parameters:** negativeSign

- the character for the negative sign
**Returns:** a copy with a new character that represents the negative sign, not null

---

#### withNegativeSign

public

DecimalStyle

withNegativeSign​(char negativeSign)

Returns a copy of the info with a new character that represents the negative sign.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

The character used to represent a negative number may vary by culture.
This method specifies the character to use.

getDecimalSeparator

```java
public char getDecimalSeparator()
```

Gets the character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Returns:** the character for the decimal point

---

#### getDecimalSeparator

public char getDecimalSeparator()

Gets the character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

withDecimalSeparator

```java
public
DecimalStyle
withDecimalSeparator​(char decimalSeparator)
```

Returns a copy of the info with a new character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

**Parameters:** decimalSeparator

- the character for the decimal point
**Returns:** a copy with a new character that represents the decimal point, not null

---

#### withDecimalSeparator

public

DecimalStyle

withDecimalSeparator​(char decimalSeparator)

Returns a copy of the info with a new character that represents the decimal point.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

The character used to represent a decimal point may vary by culture.
This method specifies the character to use.

equals

```java
public boolean equals​(
Object
obj)
```

Checks if this DecimalStyle is equal to another DecimalStyle.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to check, null returns false
**Returns:** true if this is equal to the other date
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks if this DecimalStyle is equal to another DecimalStyle.

hashCode

```java
public int hashCode()
```

A hash code for this DecimalStyle.

**Overrides:** hashCode

in class

Object
**Returns:** a suitable hash code
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

A hash code for this DecimalStyle.

toString

```java
public
String
toString()
```

Returns a string describing this DecimalStyle.

**Overrides:** toString

in class

Object
**Returns:** a string description, not null

---

#### toString

public

String

toString()

Returns a string describing this DecimalStyle.

---

