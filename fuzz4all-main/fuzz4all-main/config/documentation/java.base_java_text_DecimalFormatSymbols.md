# Class DecimalFormatSymbols

**Source:** `java.base\java\text\DecimalFormatSymbols.html`

### Class Description

```java
public class
DecimalFormatSymbols

extends
Object

implements
Cloneable
,
Serializable
```

This class represents the set of symbols (such as the decimal separator,
the grouping separator, and so on) needed by

DecimalFormat

to format numbers.

DecimalFormat

creates for itself an instance of

DecimalFormatSymbols

from its locale data. If you need to change any
of these symbols, you can get the

DecimalFormatSymbols

object from
your

DecimalFormat

and modify it.

If the locale contains "rg" (region override)

Unicode extension

,
the symbols are overridden for the designated region.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DecimalFormatSymbols()

Create a DecimalFormatSymbols object for the default

FORMAT

locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.

This is equivalent to calling

DecimalFormatSymbols(Locale.getDefault(Locale.Category.FORMAT))

.

**See Also:**
- Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

---

#### public DecimalFormatSymbols​(
Locale
locale)

Create a DecimalFormatSymbols object for the given locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:**
- locale

- the desired locale

**Throws:**
- NullPointerException

- if

locale

is null

---

### Method Details

#### public static
Locale
[] getAvailableLocales()

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

DecimalFormatSymbolsProvider

implementations. It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:**
- an array of locales for which localized

DecimalFormatSymbols

instances are available.

**Since:**
- 1.6

---

#### public static final
DecimalFormatSymbols
getInstance()

Gets the

DecimalFormatSymbols

instance for the default
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.

This is equivalent to calling

getInstance(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:**
- a

DecimalFormatSymbols

instance.

**See Also:**
- Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

**Since:**
- 1.6

---

#### public static final
DecimalFormatSymbols
getInstance​(
Locale
locale)

Gets the

DecimalFormatSymbols

instance for the specified
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:**
- locale

- the desired locale.

**Returns:**
- a

DecimalFormatSymbols

instance.

**Throws:**
- NullPointerException

- if

locale

is null

**Since:**
- 1.6

---

#### public char getZeroDigit()

Gets the character used for zero. Different for Arabic, etc.

**Returns:**
- the character used for zero

---

#### public void setZeroDigit​(char zeroDigit)

Sets the character used for zero. Different for Arabic, etc.

**Parameters:**
- zeroDigit

- the character used for zero

---

#### public char getGroupingSeparator()

Gets the character used for thousands separator. Different for French, etc.

**Returns:**
- the grouping separator

---

#### public void setGroupingSeparator​(char groupingSeparator)

Sets the character used for thousands separator. Different for French, etc.

**Parameters:**
- groupingSeparator

- the grouping separator

---

#### public char getDecimalSeparator()

Gets the character used for decimal sign. Different for French, etc.

**Returns:**
- the character used for decimal sign

---

#### public void setDecimalSeparator​(char decimalSeparator)

Sets the character used for decimal sign. Different for French, etc.

**Parameters:**
- decimalSeparator

- the character used for decimal sign

---

#### public char getPerMill()

Gets the character used for per mille sign. Different for Arabic, etc.

**Returns:**
- the character used for per mille sign

---

#### public void setPerMill​(char perMill)

Sets the character used for per mille sign. Different for Arabic, etc.

**Parameters:**
- perMill

- the character used for per mille sign

---

#### public char getPercent()

Gets the character used for percent sign. Different for Arabic, etc.

**Returns:**
- the character used for percent sign

---

#### public void setPercent​(char percent)

Sets the character used for percent sign. Different for Arabic, etc.

**Parameters:**
- percent

- the character used for percent sign

---

#### public char getDigit()

Gets the character used for a digit in a pattern.

**Returns:**
- the character used for a digit in a pattern

---

#### public void setDigit​(char digit)

Sets the character used for a digit in a pattern.

**Parameters:**
- digit

- the character used for a digit in a pattern

---

#### public char getPatternSeparator()

Gets the character used to separate positive and negative subpatterns
in a pattern.

**Returns:**
- the pattern separator

---

#### public void setPatternSeparator​(char patternSeparator)

Sets the character used to separate positive and negative subpatterns
in a pattern.

**Parameters:**
- patternSeparator

- the pattern separator

---

#### public
String
getInfinity()

Gets the string used to represent infinity. Almost always left
unchanged.

**Returns:**
- the string representing infinity

---

#### public void setInfinity​(
String
infinity)

Sets the string used to represent infinity. Almost always left
unchanged.

**Parameters:**
- infinity

- the string representing infinity

---

#### public
String
getNaN()

Gets the string used to represent "not a number". Almost always left
unchanged.

**Returns:**
- the string representing "not a number"

---

#### public void setNaN​(
String
NaN)

Sets the string used to represent "not a number". Almost always left
unchanged.

**Parameters:**
- NaN

- the string representing "not a number"

---

#### public char getMinusSign()

Gets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Returns:**
- the character representing minus sign

---

#### public void setMinusSign​(char minusSign)

Sets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Parameters:**
- minusSign

- the character representing minus sign

---

#### public
String
getCurrencySymbol()

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Returns:**
- the currency symbol

**Since:**
- 1.2

---

#### public void setCurrencySymbol​(
String
currency)

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Parameters:**
- currency

- the currency symbol

**Since:**
- 1.2

---

#### public
String
getInternationalCurrencySymbol()

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

**Returns:**
- the currency code

**Since:**
- 1.2

---

#### public void setInternationalCurrencySymbol​(
String
currencyCode)

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.
If the currency code is valid (as defined by

Currency.getInstance

),
this also sets the currency attribute to the corresponding Currency
instance and the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale. If the currency code is not valid,
then the currency attribute is set to null and the currency symbol
attribute is not modified.

**Parameters:**
- currencyCode

- the currency code

**See Also:**
- setCurrency(java.util.Currency)

,

setCurrencySymbol(java.lang.String)

**Since:**
- 1.2

---

#### public
Currency
getCurrency()

Gets the currency of these DecimalFormatSymbols. May be null if the
currency symbol attribute was previously set to a value that's not
a valid ISO 4217 currency code.

**Returns:**
- the currency used, or null

**Since:**
- 1.4

---

#### public void setCurrency​(
Currency
currency)

Sets the currency of these DecimalFormatSymbols.
This also sets the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale, and the international currency
symbol attribute to the currency's ISO 4217 currency code.

**Parameters:**
- currency

- the new currency to be used

**Throws:**
- NullPointerException

- if

currency

is null

**See Also:**
- setCurrencySymbol(java.lang.String)

,

setInternationalCurrencySymbol(java.lang.String)

**Since:**
- 1.4

---

#### public char getMonetaryDecimalSeparator()

Returns the monetary decimal separator.

**Returns:**
- the monetary decimal separator

**Since:**
- 1.2

---

#### public void setMonetaryDecimalSeparator​(char sep)

Sets the monetary decimal separator.

**Parameters:**
- sep

- the monetary decimal separator

**Since:**
- 1.2

---

#### public
String
getExponentSeparator()

Returns the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Returns:**
- the exponent separator string

**See Also:**
- setExponentSeparator(java.lang.String)

**Since:**
- 1.6

---

#### public void setExponentSeparator​(
String
exp)

Sets the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Parameters:**
- exp

- the exponent separator string

**Throws:**
- NullPointerException

- if

exp

is null

**See Also:**
- getExponentSeparator()

**Since:**
- 1.6

---

#### public
Object
clone()

Standard override.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public boolean equals​(
Object
obj)

Override equals.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Override hashCode.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class DecimalFormatSymbols

java.lang.Object

- java.text.DecimalFormatSymbols

java.text.DecimalFormatSymbols

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
DecimalFormatSymbols

extends
Object

implements
Cloneable
,
Serializable
```

This class represents the set of symbols (such as the decimal separator,
the grouping separator, and so on) needed by

DecimalFormat

to format numbers.

DecimalFormat

creates for itself an instance of

DecimalFormatSymbols

from its locale data. If you need to change any
of these symbols, you can get the

DecimalFormatSymbols

object from
your

DecimalFormat

and modify it.

If the locale contains "rg" (region override)

Unicode extension

,
the symbols are overridden for the designated region.

**Since:** 1.1
**See Also:** Locale

,

DecimalFormat

,

Serialized Form

public class

DecimalFormatSymbols

extends

Object

implements

Cloneable

,

Serializable

This class represents the set of symbols (such as the decimal separator,
the grouping separator, and so on) needed by

DecimalFormat

to format numbers.

DecimalFormat

creates for itself an instance of

DecimalFormatSymbols

from its locale data. If you need to change any
of these symbols, you can get the

DecimalFormatSymbols

object from
your

DecimalFormat

and modify it.

If the locale contains "rg" (region override)

Unicode extension

,
the symbols are overridden for the designated region.

If the locale contains "rg" (region override)

Unicode extension

,
the symbols are overridden for the designated region.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DecimalFormatSymbols

()

Create a DecimalFormatSymbols object for the default

FORMAT

locale.

DecimalFormatSymbols

​(

Locale

locale)

Create a DecimalFormatSymbols object for the given locale.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Standard override.

boolean

equals

​(

Object

obj)

Override equals.

static

Locale

[]

getAvailableLocales

()

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.

Currency

getCurrency

()

Gets the currency of these DecimalFormatSymbols.

String

getCurrencySymbol

()

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

char

getDecimalSeparator

()

Gets the character used for decimal sign.

char

getDigit

()

Gets the character used for a digit in a pattern.

String

getExponentSeparator

()

Returns the string used to separate the mantissa from the exponent.

char

getGroupingSeparator

()

Gets the character used for thousands separator.

String

getInfinity

()

Gets the string used to represent infinity.

static

DecimalFormatSymbols

getInstance

()

Gets the

DecimalFormatSymbols

instance for the default
locale.

static

DecimalFormatSymbols

getInstance

​(

Locale

locale)

Gets the

DecimalFormatSymbols

instance for the specified
locale.

String

getInternationalCurrencySymbol

()

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

char

getMinusSign

()

Gets the character used to represent minus sign.

char

getMonetaryDecimalSeparator

()

Returns the monetary decimal separator.

String

getNaN

()

Gets the string used to represent "not a number".

char

getPatternSeparator

()

Gets the character used to separate positive and negative subpatterns
in a pattern.

char

getPercent

()

Gets the character used for percent sign.

char

getPerMill

()

Gets the character used for per mille sign.

char

getZeroDigit

()

Gets the character used for zero.

int

hashCode

()

Override hashCode.

void

setCurrency

​(

Currency

currency)

Sets the currency of these DecimalFormatSymbols.

void

setCurrencySymbol

​(

String

currency)

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

void

setDecimalSeparator

​(char decimalSeparator)

Sets the character used for decimal sign.

void

setDigit

​(char digit)

Sets the character used for a digit in a pattern.

void

setExponentSeparator

​(

String

exp)

Sets the string used to separate the mantissa from the exponent.

void

setGroupingSeparator

​(char groupingSeparator)

Sets the character used for thousands separator.

void

setInfinity

​(

String

infinity)

Sets the string used to represent infinity.

void

setInternationalCurrencySymbol

​(

String

currencyCode)

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

void

setMinusSign

​(char minusSign)

Sets the character used to represent minus sign.

void

setMonetaryDecimalSeparator

​(char sep)

Sets the monetary decimal separator.

void

setNaN

​(

String

NaN)

Sets the string used to represent "not a number".

void

setPatternSeparator

​(char patternSeparator)

Sets the character used to separate positive and negative subpatterns
in a pattern.

void

setPercent

​(char percent)

Sets the character used for percent sign.

void

setPerMill

​(char perMill)

Sets the character used for per mille sign.

void

setZeroDigit

​(char zeroDigit)

Sets the character used for zero.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

DecimalFormatSymbols

()

Create a DecimalFormatSymbols object for the default

FORMAT

locale.

DecimalFormatSymbols

​(

Locale

locale)

Create a DecimalFormatSymbols object for the given locale.

---

#### Constructor Summary

Create a DecimalFormatSymbols object for the default

FORMAT

locale.

Create a DecimalFormatSymbols object for the given locale.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Standard override.

boolean

equals

​(

Object

obj)

Override equals.

static

Locale

[]

getAvailableLocales

()

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.

Currency

getCurrency

()

Gets the currency of these DecimalFormatSymbols.

String

getCurrencySymbol

()

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

char

getDecimalSeparator

()

Gets the character used for decimal sign.

char

getDigit

()

Gets the character used for a digit in a pattern.

String

getExponentSeparator

()

Returns the string used to separate the mantissa from the exponent.

char

getGroupingSeparator

()

Gets the character used for thousands separator.

String

getInfinity

()

Gets the string used to represent infinity.

static

DecimalFormatSymbols

getInstance

()

Gets the

DecimalFormatSymbols

instance for the default
locale.

static

DecimalFormatSymbols

getInstance

​(

Locale

locale)

Gets the

DecimalFormatSymbols

instance for the specified
locale.

String

getInternationalCurrencySymbol

()

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

char

getMinusSign

()

Gets the character used to represent minus sign.

char

getMonetaryDecimalSeparator

()

Returns the monetary decimal separator.

String

getNaN

()

Gets the string used to represent "not a number".

char

getPatternSeparator

()

Gets the character used to separate positive and negative subpatterns
in a pattern.

char

getPercent

()

Gets the character used for percent sign.

char

getPerMill

()

Gets the character used for per mille sign.

char

getZeroDigit

()

Gets the character used for zero.

int

hashCode

()

Override hashCode.

void

setCurrency

​(

Currency

currency)

Sets the currency of these DecimalFormatSymbols.

void

setCurrencySymbol

​(

String

currency)

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

void

setDecimalSeparator

​(char decimalSeparator)

Sets the character used for decimal sign.

void

setDigit

​(char digit)

Sets the character used for a digit in a pattern.

void

setExponentSeparator

​(

String

exp)

Sets the string used to separate the mantissa from the exponent.

void

setGroupingSeparator

​(char groupingSeparator)

Sets the character used for thousands separator.

void

setInfinity

​(

String

infinity)

Sets the string used to represent infinity.

void

setInternationalCurrencySymbol

​(

String

currencyCode)

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

void

setMinusSign

​(char minusSign)

Sets the character used to represent minus sign.

void

setMonetaryDecimalSeparator

​(char sep)

Sets the monetary decimal separator.

void

setNaN

​(

String

NaN)

Sets the string used to represent "not a number".

void

setPatternSeparator

​(char patternSeparator)

Sets the character used to separate positive and negative subpatterns
in a pattern.

void

setPercent

​(char percent)

Sets the character used for percent sign.

void

setPerMill

​(char perMill)

Sets the character used for per mille sign.

void

setZeroDigit

​(char zeroDigit)

Sets the character used for zero.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Standard override.

Override equals.

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.

Gets the currency of these DecimalFormatSymbols.

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

Gets the character used for decimal sign.

Gets the character used for a digit in a pattern.

Returns the string used to separate the mantissa from the exponent.

Gets the character used for thousands separator.

Gets the string used to represent infinity.

Gets the

DecimalFormatSymbols

instance for the default
locale.

Gets the

DecimalFormatSymbols

instance for the specified
locale.

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

Gets the character used to represent minus sign.

Returns the monetary decimal separator.

Gets the string used to represent "not a number".

Gets the character used to separate positive and negative subpatterns
in a pattern.

Gets the character used for percent sign.

Gets the character used for per mille sign.

Gets the character used for zero.

Override hashCode.

Sets the currency of these DecimalFormatSymbols.

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

Sets the character used for decimal sign.

Sets the character used for a digit in a pattern.

Sets the string used to separate the mantissa from the exponent.

Sets the character used for thousands separator.

Sets the string used to represent infinity.

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

Sets the character used to represent minus sign.

Sets the monetary decimal separator.

Sets the string used to represent "not a number".

Sets the character used to separate positive and negative subpatterns
in a pattern.

Sets the character used for percent sign.

Sets the character used for per mille sign.

Sets the character used for zero.

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DecimalFormatSymbols

```java
public DecimalFormatSymbols()
```

Create a DecimalFormatSymbols object for the default

FORMAT

locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.

This is equivalent to calling

DecimalFormatSymbols(Locale.getDefault(Locale.Category.FORMAT))

.

**See Also:** Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

- DecimalFormatSymbols

```java
public DecimalFormatSymbols​(
Locale
locale)
```

Create a DecimalFormatSymbols object for the given locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:** locale

- the desired locale
**Throws:** NullPointerException

- if

locale

is null

============ METHOD DETAIL ==========

- Method Detail

- getAvailableLocales

```java
public static
Locale
[] getAvailableLocales()
```

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

DecimalFormatSymbolsProvider

implementations. It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:** an array of locales for which localized

DecimalFormatSymbols

instances are available.
**Since:** 1.6

- getInstance

```java
public static final
DecimalFormatSymbols
getInstance()
```

Gets the

DecimalFormatSymbols

instance for the default
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.

This is equivalent to calling

getInstance(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:** a

DecimalFormatSymbols

instance.
**Since:** 1.6
**See Also:** Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

- getInstance

```java
public static final
DecimalFormatSymbols
getInstance​(
Locale
locale)
```

Gets the

DecimalFormatSymbols

instance for the specified
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:** locale

- the desired locale.
**Returns:** a

DecimalFormatSymbols

instance.
**Throws:** NullPointerException

- if

locale

is null
**Since:** 1.6

- getZeroDigit

```java
public char getZeroDigit()
```

Gets the character used for zero. Different for Arabic, etc.

**Returns:** the character used for zero

- setZeroDigit

```java
public void setZeroDigit​(char zeroDigit)
```

Sets the character used for zero. Different for Arabic, etc.

**Parameters:** zeroDigit

- the character used for zero

- getGroupingSeparator

```java
public char getGroupingSeparator()
```

Gets the character used for thousands separator. Different for French, etc.

**Returns:** the grouping separator

- setGroupingSeparator

```java
public void setGroupingSeparator​(char groupingSeparator)
```

Sets the character used for thousands separator. Different for French, etc.

**Parameters:** groupingSeparator

- the grouping separator

- getDecimalSeparator

```java
public char getDecimalSeparator()
```

Gets the character used for decimal sign. Different for French, etc.

**Returns:** the character used for decimal sign

- setDecimalSeparator

```java
public void setDecimalSeparator​(char decimalSeparator)
```

Sets the character used for decimal sign. Different for French, etc.

**Parameters:** decimalSeparator

- the character used for decimal sign

- getPerMill

```java
public char getPerMill()
```

Gets the character used for per mille sign. Different for Arabic, etc.

**Returns:** the character used for per mille sign

- setPerMill

```java
public void setPerMill​(char perMill)
```

Sets the character used for per mille sign. Different for Arabic, etc.

**Parameters:** perMill

- the character used for per mille sign

- getPercent

```java
public char getPercent()
```

Gets the character used for percent sign. Different for Arabic, etc.

**Returns:** the character used for percent sign

- setPercent

```java
public void setPercent​(char percent)
```

Sets the character used for percent sign. Different for Arabic, etc.

**Parameters:** percent

- the character used for percent sign

- getDigit

```java
public char getDigit()
```

Gets the character used for a digit in a pattern.

**Returns:** the character used for a digit in a pattern

- setDigit

```java
public void setDigit​(char digit)
```

Sets the character used for a digit in a pattern.

**Parameters:** digit

- the character used for a digit in a pattern

- getPatternSeparator

```java
public char getPatternSeparator()
```

Gets the character used to separate positive and negative subpatterns
in a pattern.

**Returns:** the pattern separator

- setPatternSeparator

```java
public void setPatternSeparator​(char patternSeparator)
```

Sets the character used to separate positive and negative subpatterns
in a pattern.

**Parameters:** patternSeparator

- the pattern separator

- getInfinity

```java
public
String
getInfinity()
```

Gets the string used to represent infinity. Almost always left
unchanged.

**Returns:** the string representing infinity

- setInfinity

```java
public void setInfinity​(
String
infinity)
```

Sets the string used to represent infinity. Almost always left
unchanged.

**Parameters:** infinity

- the string representing infinity

- getNaN

```java
public
String
getNaN()
```

Gets the string used to represent "not a number". Almost always left
unchanged.

**Returns:** the string representing "not a number"

- setNaN

```java
public void setNaN​(
String
NaN)
```

Sets the string used to represent "not a number". Almost always left
unchanged.

**Parameters:** NaN

- the string representing "not a number"

- getMinusSign

```java
public char getMinusSign()
```

Gets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Returns:** the character representing minus sign

- setMinusSign

```java
public void setMinusSign​(char minusSign)
```

Sets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Parameters:** minusSign

- the character representing minus sign

- getCurrencySymbol

```java
public
String
getCurrencySymbol()
```

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Returns:** the currency symbol
**Since:** 1.2

- setCurrencySymbol

```java
public void setCurrencySymbol​(
String
currency)
```

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Parameters:** currency

- the currency symbol
**Since:** 1.2

- getInternationalCurrencySymbol

```java
public
String
getInternationalCurrencySymbol()
```

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

**Returns:** the currency code
**Since:** 1.2

- setInternationalCurrencySymbol

```java
public void setInternationalCurrencySymbol​(
String
currencyCode)
```

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.
If the currency code is valid (as defined by

Currency.getInstance

),
this also sets the currency attribute to the corresponding Currency
instance and the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale. If the currency code is not valid,
then the currency attribute is set to null and the currency symbol
attribute is not modified.

**Parameters:** currencyCode

- the currency code
**Since:** 1.2
**See Also:** setCurrency(java.util.Currency)

,

setCurrencySymbol(java.lang.String)

- getCurrency

```java
public
Currency
getCurrency()
```

Gets the currency of these DecimalFormatSymbols. May be null if the
currency symbol attribute was previously set to a value that's not
a valid ISO 4217 currency code.

**Returns:** the currency used, or null
**Since:** 1.4

- setCurrency

```java
public void setCurrency​(
Currency
currency)
```

Sets the currency of these DecimalFormatSymbols.
This also sets the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale, and the international currency
symbol attribute to the currency's ISO 4217 currency code.

**Parameters:** currency

- the new currency to be used
**Throws:** NullPointerException

- if

currency

is null
**Since:** 1.4
**See Also:** setCurrencySymbol(java.lang.String)

,

setInternationalCurrencySymbol(java.lang.String)

- getMonetaryDecimalSeparator

```java
public char getMonetaryDecimalSeparator()
```

Returns the monetary decimal separator.

**Returns:** the monetary decimal separator
**Since:** 1.2

- setMonetaryDecimalSeparator

```java
public void setMonetaryDecimalSeparator​(char sep)
```

Sets the monetary decimal separator.

**Parameters:** sep

- the monetary decimal separator
**Since:** 1.2

- getExponentSeparator

```java
public
String
getExponentSeparator()
```

Returns the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Returns:** the exponent separator string
**Since:** 1.6
**See Also:** setExponentSeparator(java.lang.String)

- setExponentSeparator

```java
public void setExponentSeparator​(
String
exp)
```

Sets the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Parameters:** exp

- the exponent separator string
**Throws:** NullPointerException

- if

exp

is null
**Since:** 1.6
**See Also:** getExponentSeparator()

- clone

```java
public
Object
clone()
```

Standard override.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- equals

```java
public boolean equals​(
Object
obj)
```

Override equals.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Override hashCode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- DecimalFormatSymbols

```java
public DecimalFormatSymbols()
```

Create a DecimalFormatSymbols object for the default

FORMAT

locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.

This is equivalent to calling

DecimalFormatSymbols(Locale.getDefault(Locale.Category.FORMAT))

.

**See Also:** Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

- DecimalFormatSymbols

```java
public DecimalFormatSymbols​(
Locale
locale)
```

Create a DecimalFormatSymbols object for the given locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:** locale

- the desired locale
**Throws:** NullPointerException

- if

locale

is null

---

#### Constructor Detail

DecimalFormatSymbols

```java
public DecimalFormatSymbols()
```

Create a DecimalFormatSymbols object for the default

FORMAT

locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.

This is equivalent to calling

DecimalFormatSymbols(Locale.getDefault(Locale.Category.FORMAT))

.

**See Also:** Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

---

#### DecimalFormatSymbols

public DecimalFormatSymbols()

Create a DecimalFormatSymbols object for the default

FORMAT

locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.

This is equivalent to calling

DecimalFormatSymbols(Locale.getDefault(Locale.Category.FORMAT))

.

This is equivalent to calling

DecimalFormatSymbols(Locale.getDefault(Locale.Category.FORMAT))

.

DecimalFormatSymbols

```java
public DecimalFormatSymbols​(
Locale
locale)
```

Create a DecimalFormatSymbols object for the given locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:** locale

- the desired locale
**Throws:** NullPointerException

- if

locale

is null

---

#### DecimalFormatSymbols

public DecimalFormatSymbols​(

Locale

locale)

Create a DecimalFormatSymbols object for the given locale.
This constructor can only construct instances for the locales
supported by the Java runtime environment, not for those
supported by installed

DecimalFormatSymbolsProvider

implementations. For full locale coverage, use the

getInstance

method.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))

Method Detail

- getAvailableLocales

```java
public static
Locale
[] getAvailableLocales()
```

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

DecimalFormatSymbolsProvider

implementations. It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:** an array of locales for which localized

DecimalFormatSymbols

instances are available.
**Since:** 1.6

- getInstance

```java
public static final
DecimalFormatSymbols
getInstance()
```

Gets the

DecimalFormatSymbols

instance for the default
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.

This is equivalent to calling

getInstance(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:** a

DecimalFormatSymbols

instance.
**Since:** 1.6
**See Also:** Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

- getInstance

```java
public static final
DecimalFormatSymbols
getInstance​(
Locale
locale)
```

Gets the

DecimalFormatSymbols

instance for the specified
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:** locale

- the desired locale.
**Returns:** a

DecimalFormatSymbols

instance.
**Throws:** NullPointerException

- if

locale

is null
**Since:** 1.6

- getZeroDigit

```java
public char getZeroDigit()
```

Gets the character used for zero. Different for Arabic, etc.

**Returns:** the character used for zero

- setZeroDigit

```java
public void setZeroDigit​(char zeroDigit)
```

Sets the character used for zero. Different for Arabic, etc.

**Parameters:** zeroDigit

- the character used for zero

- getGroupingSeparator

```java
public char getGroupingSeparator()
```

Gets the character used for thousands separator. Different for French, etc.

**Returns:** the grouping separator

- setGroupingSeparator

```java
public void setGroupingSeparator​(char groupingSeparator)
```

Sets the character used for thousands separator. Different for French, etc.

**Parameters:** groupingSeparator

- the grouping separator

- getDecimalSeparator

```java
public char getDecimalSeparator()
```

Gets the character used for decimal sign. Different for French, etc.

**Returns:** the character used for decimal sign

- setDecimalSeparator

```java
public void setDecimalSeparator​(char decimalSeparator)
```

Sets the character used for decimal sign. Different for French, etc.

**Parameters:** decimalSeparator

- the character used for decimal sign

- getPerMill

```java
public char getPerMill()
```

Gets the character used for per mille sign. Different for Arabic, etc.

**Returns:** the character used for per mille sign

- setPerMill

```java
public void setPerMill​(char perMill)
```

Sets the character used for per mille sign. Different for Arabic, etc.

**Parameters:** perMill

- the character used for per mille sign

- getPercent

```java
public char getPercent()
```

Gets the character used for percent sign. Different for Arabic, etc.

**Returns:** the character used for percent sign

- setPercent

```java
public void setPercent​(char percent)
```

Sets the character used for percent sign. Different for Arabic, etc.

**Parameters:** percent

- the character used for percent sign

- getDigit

```java
public char getDigit()
```

Gets the character used for a digit in a pattern.

**Returns:** the character used for a digit in a pattern

- setDigit

```java
public void setDigit​(char digit)
```

Sets the character used for a digit in a pattern.

**Parameters:** digit

- the character used for a digit in a pattern

- getPatternSeparator

```java
public char getPatternSeparator()
```

Gets the character used to separate positive and negative subpatterns
in a pattern.

**Returns:** the pattern separator

- setPatternSeparator

```java
public void setPatternSeparator​(char patternSeparator)
```

Sets the character used to separate positive and negative subpatterns
in a pattern.

**Parameters:** patternSeparator

- the pattern separator

- getInfinity

```java
public
String
getInfinity()
```

Gets the string used to represent infinity. Almost always left
unchanged.

**Returns:** the string representing infinity

- setInfinity

```java
public void setInfinity​(
String
infinity)
```

Sets the string used to represent infinity. Almost always left
unchanged.

**Parameters:** infinity

- the string representing infinity

- getNaN

```java
public
String
getNaN()
```

Gets the string used to represent "not a number". Almost always left
unchanged.

**Returns:** the string representing "not a number"

- setNaN

```java
public void setNaN​(
String
NaN)
```

Sets the string used to represent "not a number". Almost always left
unchanged.

**Parameters:** NaN

- the string representing "not a number"

- getMinusSign

```java
public char getMinusSign()
```

Gets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Returns:** the character representing minus sign

- setMinusSign

```java
public void setMinusSign​(char minusSign)
```

Sets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Parameters:** minusSign

- the character representing minus sign

- getCurrencySymbol

```java
public
String
getCurrencySymbol()
```

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Returns:** the currency symbol
**Since:** 1.2

- setCurrencySymbol

```java
public void setCurrencySymbol​(
String
currency)
```

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Parameters:** currency

- the currency symbol
**Since:** 1.2

- getInternationalCurrencySymbol

```java
public
String
getInternationalCurrencySymbol()
```

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

**Returns:** the currency code
**Since:** 1.2

- setInternationalCurrencySymbol

```java
public void setInternationalCurrencySymbol​(
String
currencyCode)
```

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.
If the currency code is valid (as defined by

Currency.getInstance

),
this also sets the currency attribute to the corresponding Currency
instance and the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale. If the currency code is not valid,
then the currency attribute is set to null and the currency symbol
attribute is not modified.

**Parameters:** currencyCode

- the currency code
**Since:** 1.2
**See Also:** setCurrency(java.util.Currency)

,

setCurrencySymbol(java.lang.String)

- getCurrency

```java
public
Currency
getCurrency()
```

Gets the currency of these DecimalFormatSymbols. May be null if the
currency symbol attribute was previously set to a value that's not
a valid ISO 4217 currency code.

**Returns:** the currency used, or null
**Since:** 1.4

- setCurrency

```java
public void setCurrency​(
Currency
currency)
```

Sets the currency of these DecimalFormatSymbols.
This also sets the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale, and the international currency
symbol attribute to the currency's ISO 4217 currency code.

**Parameters:** currency

- the new currency to be used
**Throws:** NullPointerException

- if

currency

is null
**Since:** 1.4
**See Also:** setCurrencySymbol(java.lang.String)

,

setInternationalCurrencySymbol(java.lang.String)

- getMonetaryDecimalSeparator

```java
public char getMonetaryDecimalSeparator()
```

Returns the monetary decimal separator.

**Returns:** the monetary decimal separator
**Since:** 1.2

- setMonetaryDecimalSeparator

```java
public void setMonetaryDecimalSeparator​(char sep)
```

Sets the monetary decimal separator.

**Parameters:** sep

- the monetary decimal separator
**Since:** 1.2

- getExponentSeparator

```java
public
String
getExponentSeparator()
```

Returns the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Returns:** the exponent separator string
**Since:** 1.6
**See Also:** setExponentSeparator(java.lang.String)

- setExponentSeparator

```java
public void setExponentSeparator​(
String
exp)
```

Sets the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Parameters:** exp

- the exponent separator string
**Throws:** NullPointerException

- if

exp

is null
**Since:** 1.6
**See Also:** getExponentSeparator()

- clone

```java
public
Object
clone()
```

Standard override.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- equals

```java
public boolean equals​(
Object
obj)
```

Override equals.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Override hashCode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getAvailableLocales

```java
public static
Locale
[] getAvailableLocales()
```

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

DecimalFormatSymbolsProvider

implementations. It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:** an array of locales for which localized

DecimalFormatSymbols

instances are available.
**Since:** 1.6

---

#### getAvailableLocales

public static

Locale

[] getAvailableLocales()

Returns an array of all locales for which the

getInstance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

DecimalFormatSymbolsProvider

implementations. It must contain at least a

Locale

instance equal to

Locale.US

.

getInstance

```java
public static final
DecimalFormatSymbols
getInstance()
```

Gets the

DecimalFormatSymbols

instance for the default
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.

This is equivalent to calling

getInstance(Locale.getDefault(Locale.Category.FORMAT))

.

**Returns:** a

DecimalFormatSymbols

instance.
**Since:** 1.6
**See Also:** Locale.getDefault(java.util.Locale.Category)

,

Locale.Category.FORMAT

---

#### getInstance

public static final

DecimalFormatSymbols

getInstance()

Gets the

DecimalFormatSymbols

instance for the default
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.

This is equivalent to calling

getInstance(Locale.getDefault(Locale.Category.FORMAT))

.

This is equivalent to calling

getInstance(Locale.getDefault(Locale.Category.FORMAT))

.

getInstance

```java
public static final
DecimalFormatSymbols
getInstance​(
Locale
locale)
```

Gets the

DecimalFormatSymbols

instance for the specified
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

**Parameters:** locale

- the desired locale.
**Returns:** a

DecimalFormatSymbols

instance.
**Throws:** NullPointerException

- if

locale

is null
**Since:** 1.6

---

#### getInstance

public static final

DecimalFormatSymbols

getInstance​(

Locale

locale)

Gets the

DecimalFormatSymbols

instance for the specified
locale. This method provides access to

DecimalFormatSymbols

instances for locales supported by the Java runtime itself as well
as for those supported by installed

DecimalFormatSymbolsProvider

implementations.
If the specified locale contains the

Locale.UNICODE_LOCALE_EXTENSION

for the numbering system, the instance is initialized with the specified numbering
system if the JRE implementation supports it. For example,

```java
NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))
```

This may return a

NumberFormat

instance with the Thai numbering system,
instead of the Latin numbering system.

NumberFormat.getNumberInstance(Locale.forLanguageTag("th-TH-u-nu-thai"))

getZeroDigit

```java
public char getZeroDigit()
```

Gets the character used for zero. Different for Arabic, etc.

**Returns:** the character used for zero

---

#### getZeroDigit

public char getZeroDigit()

Gets the character used for zero. Different for Arabic, etc.

setZeroDigit

```java
public void setZeroDigit​(char zeroDigit)
```

Sets the character used for zero. Different for Arabic, etc.

**Parameters:** zeroDigit

- the character used for zero

---

#### setZeroDigit

public void setZeroDigit​(char zeroDigit)

Sets the character used for zero. Different for Arabic, etc.

getGroupingSeparator

```java
public char getGroupingSeparator()
```

Gets the character used for thousands separator. Different for French, etc.

**Returns:** the grouping separator

---

#### getGroupingSeparator

public char getGroupingSeparator()

Gets the character used for thousands separator. Different for French, etc.

setGroupingSeparator

```java
public void setGroupingSeparator​(char groupingSeparator)
```

Sets the character used for thousands separator. Different for French, etc.

**Parameters:** groupingSeparator

- the grouping separator

---

#### setGroupingSeparator

public void setGroupingSeparator​(char groupingSeparator)

Sets the character used for thousands separator. Different for French, etc.

getDecimalSeparator

```java
public char getDecimalSeparator()
```

Gets the character used for decimal sign. Different for French, etc.

**Returns:** the character used for decimal sign

---

#### getDecimalSeparator

public char getDecimalSeparator()

Gets the character used for decimal sign. Different for French, etc.

setDecimalSeparator

```java
public void setDecimalSeparator​(char decimalSeparator)
```

Sets the character used for decimal sign. Different for French, etc.

**Parameters:** decimalSeparator

- the character used for decimal sign

---

#### setDecimalSeparator

public void setDecimalSeparator​(char decimalSeparator)

Sets the character used for decimal sign. Different for French, etc.

getPerMill

```java
public char getPerMill()
```

Gets the character used for per mille sign. Different for Arabic, etc.

**Returns:** the character used for per mille sign

---

#### getPerMill

public char getPerMill()

Gets the character used for per mille sign. Different for Arabic, etc.

setPerMill

```java
public void setPerMill​(char perMill)
```

Sets the character used for per mille sign. Different for Arabic, etc.

**Parameters:** perMill

- the character used for per mille sign

---

#### setPerMill

public void setPerMill​(char perMill)

Sets the character used for per mille sign. Different for Arabic, etc.

getPercent

```java
public char getPercent()
```

Gets the character used for percent sign. Different for Arabic, etc.

**Returns:** the character used for percent sign

---

#### getPercent

public char getPercent()

Gets the character used for percent sign. Different for Arabic, etc.

setPercent

```java
public void setPercent​(char percent)
```

Sets the character used for percent sign. Different for Arabic, etc.

**Parameters:** percent

- the character used for percent sign

---

#### setPercent

public void setPercent​(char percent)

Sets the character used for percent sign. Different for Arabic, etc.

getDigit

```java
public char getDigit()
```

Gets the character used for a digit in a pattern.

**Returns:** the character used for a digit in a pattern

---

#### getDigit

public char getDigit()

Gets the character used for a digit in a pattern.

setDigit

```java
public void setDigit​(char digit)
```

Sets the character used for a digit in a pattern.

**Parameters:** digit

- the character used for a digit in a pattern

---

#### setDigit

public void setDigit​(char digit)

Sets the character used for a digit in a pattern.

getPatternSeparator

```java
public char getPatternSeparator()
```

Gets the character used to separate positive and negative subpatterns
in a pattern.

**Returns:** the pattern separator

---

#### getPatternSeparator

public char getPatternSeparator()

Gets the character used to separate positive and negative subpatterns
in a pattern.

setPatternSeparator

```java
public void setPatternSeparator​(char patternSeparator)
```

Sets the character used to separate positive and negative subpatterns
in a pattern.

**Parameters:** patternSeparator

- the pattern separator

---

#### setPatternSeparator

public void setPatternSeparator​(char patternSeparator)

Sets the character used to separate positive and negative subpatterns
in a pattern.

getInfinity

```java
public
String
getInfinity()
```

Gets the string used to represent infinity. Almost always left
unchanged.

**Returns:** the string representing infinity

---

#### getInfinity

public

String

getInfinity()

Gets the string used to represent infinity. Almost always left
unchanged.

setInfinity

```java
public void setInfinity​(
String
infinity)
```

Sets the string used to represent infinity. Almost always left
unchanged.

**Parameters:** infinity

- the string representing infinity

---

#### setInfinity

public void setInfinity​(

String

infinity)

Sets the string used to represent infinity. Almost always left
unchanged.

getNaN

```java
public
String
getNaN()
```

Gets the string used to represent "not a number". Almost always left
unchanged.

**Returns:** the string representing "not a number"

---

#### getNaN

public

String

getNaN()

Gets the string used to represent "not a number". Almost always left
unchanged.

setNaN

```java
public void setNaN​(
String
NaN)
```

Sets the string used to represent "not a number". Almost always left
unchanged.

**Parameters:** NaN

- the string representing "not a number"

---

#### setNaN

public void setNaN​(

String

NaN)

Sets the string used to represent "not a number". Almost always left
unchanged.

getMinusSign

```java
public char getMinusSign()
```

Gets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Returns:** the character representing minus sign

---

#### getMinusSign

public char getMinusSign()

Gets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

setMinusSign

```java
public void setMinusSign​(char minusSign)
```

Sets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

**Parameters:** minusSign

- the character representing minus sign

---

#### setMinusSign

public void setMinusSign​(char minusSign)

Sets the character used to represent minus sign. If no explicit
negative format is specified, one is formed by prefixing
minusSign to the positive format.

getCurrencySymbol

```java
public
String
getCurrencySymbol()
```

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Returns:** the currency symbol
**Since:** 1.2

---

#### getCurrencySymbol

public

String

getCurrencySymbol()

Returns the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

setCurrencySymbol

```java
public void setCurrencySymbol​(
String
currency)
```

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

**Parameters:** currency

- the currency symbol
**Since:** 1.2

---

#### setCurrencySymbol

public void setCurrencySymbol​(

String

currency)

Sets the currency symbol for the currency of these
DecimalFormatSymbols in their locale.

getInternationalCurrencySymbol

```java
public
String
getInternationalCurrencySymbol()
```

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

**Returns:** the currency code
**Since:** 1.2

---

#### getInternationalCurrencySymbol

public

String

getInternationalCurrencySymbol()

Returns the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.

setInternationalCurrencySymbol

```java
public void setInternationalCurrencySymbol​(
String
currencyCode)
```

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.
If the currency code is valid (as defined by

Currency.getInstance

),
this also sets the currency attribute to the corresponding Currency
instance and the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale. If the currency code is not valid,
then the currency attribute is set to null and the currency symbol
attribute is not modified.

**Parameters:** currencyCode

- the currency code
**Since:** 1.2
**See Also:** setCurrency(java.util.Currency)

,

setCurrencySymbol(java.lang.String)

---

#### setInternationalCurrencySymbol

public void setInternationalCurrencySymbol​(

String

currencyCode)

Sets the ISO 4217 currency code of the currency of these
DecimalFormatSymbols.
If the currency code is valid (as defined by

Currency.getInstance

),
this also sets the currency attribute to the corresponding Currency
instance and the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale. If the currency code is not valid,
then the currency attribute is set to null and the currency symbol
attribute is not modified.

getCurrency

```java
public
Currency
getCurrency()
```

Gets the currency of these DecimalFormatSymbols. May be null if the
currency symbol attribute was previously set to a value that's not
a valid ISO 4217 currency code.

**Returns:** the currency used, or null
**Since:** 1.4

---

#### getCurrency

public

Currency

getCurrency()

Gets the currency of these DecimalFormatSymbols. May be null if the
currency symbol attribute was previously set to a value that's not
a valid ISO 4217 currency code.

setCurrency

```java
public void setCurrency​(
Currency
currency)
```

Sets the currency of these DecimalFormatSymbols.
This also sets the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale, and the international currency
symbol attribute to the currency's ISO 4217 currency code.

**Parameters:** currency

- the new currency to be used
**Throws:** NullPointerException

- if

currency

is null
**Since:** 1.4
**See Also:** setCurrencySymbol(java.lang.String)

,

setInternationalCurrencySymbol(java.lang.String)

---

#### setCurrency

public void setCurrency​(

Currency

currency)

Sets the currency of these DecimalFormatSymbols.
This also sets the currency symbol attribute to the currency's symbol
in the DecimalFormatSymbols' locale, and the international currency
symbol attribute to the currency's ISO 4217 currency code.

getMonetaryDecimalSeparator

```java
public char getMonetaryDecimalSeparator()
```

Returns the monetary decimal separator.

**Returns:** the monetary decimal separator
**Since:** 1.2

---

#### getMonetaryDecimalSeparator

public char getMonetaryDecimalSeparator()

Returns the monetary decimal separator.

setMonetaryDecimalSeparator

```java
public void setMonetaryDecimalSeparator​(char sep)
```

Sets the monetary decimal separator.

**Parameters:** sep

- the monetary decimal separator
**Since:** 1.2

---

#### setMonetaryDecimalSeparator

public void setMonetaryDecimalSeparator​(char sep)

Sets the monetary decimal separator.

getExponentSeparator

```java
public
String
getExponentSeparator()
```

Returns the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Returns:** the exponent separator string
**Since:** 1.6
**See Also:** setExponentSeparator(java.lang.String)

---

#### getExponentSeparator

public

String

getExponentSeparator()

Returns the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

setExponentSeparator

```java
public void setExponentSeparator​(
String
exp)
```

Sets the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

**Parameters:** exp

- the exponent separator string
**Throws:** NullPointerException

- if

exp

is null
**Since:** 1.6
**See Also:** getExponentSeparator()

---

#### setExponentSeparator

public void setExponentSeparator​(

String

exp)

Sets the string used to separate the mantissa from the exponent.
Examples: "x10^" for 1.23x10^4, "E" for 1.23E4.

clone

```java
public
Object
clone()
```

Standard override.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Standard override.

equals

```java
public boolean equals​(
Object
obj)
```

Override equals.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Override equals.

hashCode

```java
public int hashCode()
```

Override hashCode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Override hashCode.

---

