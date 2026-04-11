# Class NumberFormatter

**Source:** `java.desktop\javax\swing\text\NumberFormatter.html`

### Class Description

```java
public class
NumberFormatter

extends
InternationalFormatter
```

NumberFormatter

subclasses

InternationalFormatter

adding special behavior for numbers. Among the specializations are
(these are only used if the

NumberFormatter

does not display
invalid numbers, for example,

setAllowsInvalid(false)

):

- Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in any field but the exponent
field will attempt to change the sign of the number to
positive/negative.

Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in the exponent field will
attempt to change the sign of the exponent to positive/negative.

If you are displaying scientific numbers, you may wish to turn on
overwrite mode,

setOverwriteMode(true)

. For example:

```java
DecimalFormat decimalFormat = new DecimalFormat("0.000E0");
NumberFormatter textFormatter = new NumberFormatter(decimalFormat);
textFormatter.setOverwriteMode(true);
textFormatter.setAllowsInvalid(false);
```

If you are going to allow the user to enter decimal
values, you should either force the DecimalFormat to contain at least
one decimal (

#.0###

), or allow the value to be invalid

setAllowsInvalid(true)

. Otherwise users may not be able to
input decimal values.

NumberFormatter

provides slightly different behavior to

stringToValue

than that of its superclass. If you have
specified a Class for values,

DefaultFormatter.setValueClass(java.lang.Class<?>)

, that is one of
of

Integer

,

Long

,

Float

,

Double

,

Byte

or

Short

and
the Format's

parseObject

returns an instance of

Number

, the corresponding instance of the value class
will be created using the constructor appropriate for the primitive
type the value class represents. For example:

setValueClass(Integer.class)

will cause the resulting
value to be created via

Integer.valueOf(((Number)formatter.parseObject(string)).intValue())

.
This is typically useful if you
wish to set a min/max value as the various

Number

implementations are generally not comparable to each other. This is also
useful if for some reason you need a specific

Number

implementation for your values.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NumberFormatter()

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

---

#### public NumberFormatter​(
NumberFormat
format)

Creates a NumberFormatter with the specified Format instance.

**Parameters:**
- format

- Format used to dictate legal values

---

### Method Details

#### public void setFormat​(
Format
format)

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

NumberFormat.getNumberInstance()

method.

**Overrides:**
- setFormat

in class

InternationalFormatter

**Parameters:**
- format

- NumberFormat instance used to dictate legal values

---

### Additional Sections

#### Class NumberFormatter

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatter
- - javax.swing.text.DefaultFormatter
- - javax.swing.text.InternationalFormatter
- - javax.swing.text.NumberFormatter

javax.swing.JFormattedTextField.AbstractFormatter

- javax.swing.text.DefaultFormatter
- - javax.swing.text.InternationalFormatter
- - javax.swing.text.NumberFormatter

javax.swing.text.DefaultFormatter

- javax.swing.text.InternationalFormatter
- - javax.swing.text.NumberFormatter

javax.swing.text.InternationalFormatter

- javax.swing.text.NumberFormatter

javax.swing.text.NumberFormatter

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
NumberFormatter

extends
InternationalFormatter
```

NumberFormatter

subclasses

InternationalFormatter

adding special behavior for numbers. Among the specializations are
(these are only used if the

NumberFormatter

does not display
invalid numbers, for example,

setAllowsInvalid(false)

):

- Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in any field but the exponent
field will attempt to change the sign of the number to
positive/negative.

Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in the exponent field will
attempt to change the sign of the exponent to positive/negative.

If you are displaying scientific numbers, you may wish to turn on
overwrite mode,

setOverwriteMode(true)

. For example:

```java
DecimalFormat decimalFormat = new DecimalFormat("0.000E0");
NumberFormatter textFormatter = new NumberFormatter(decimalFormat);
textFormatter.setOverwriteMode(true);
textFormatter.setAllowsInvalid(false);
```

If you are going to allow the user to enter decimal
values, you should either force the DecimalFormat to contain at least
one decimal (

#.0###

), or allow the value to be invalid

setAllowsInvalid(true)

. Otherwise users may not be able to
input decimal values.

NumberFormatter

provides slightly different behavior to

stringToValue

than that of its superclass. If you have
specified a Class for values,

DefaultFormatter.setValueClass(java.lang.Class<?>)

, that is one of
of

Integer

,

Long

,

Float

,

Double

,

Byte

or

Short

and
the Format's

parseObject

returns an instance of

Number

, the corresponding instance of the value class
will be created using the constructor appropriate for the primitive
type the value class represents. For example:

setValueClass(Integer.class)

will cause the resulting
value to be created via

Integer.valueOf(((Number)formatter.parseObject(string)).intValue())

.
This is typically useful if you
wish to set a min/max value as the various

Number

implementations are generally not comparable to each other. This is also
useful if for some reason you need a specific

Number

implementation for your values.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.4
**See Also:** Serialized Form

public class

NumberFormatter

extends

InternationalFormatter

NumberFormatter

subclasses

InternationalFormatter

adding special behavior for numbers. Among the specializations are
(these are only used if the

NumberFormatter

does not display
invalid numbers, for example,

setAllowsInvalid(false)

):

- Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in any field but the exponent
field will attempt to change the sign of the number to
positive/negative.

Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in the exponent field will
attempt to change the sign of the exponent to positive/negative.

If you are displaying scientific numbers, you may wish to turn on
overwrite mode,

setOverwriteMode(true)

. For example:

```java
DecimalFormat decimalFormat = new DecimalFormat("0.000E0");
NumberFormatter textFormatter = new NumberFormatter(decimalFormat);
textFormatter.setOverwriteMode(true);
textFormatter.setAllowsInvalid(false);
```

If you are going to allow the user to enter decimal
values, you should either force the DecimalFormat to contain at least
one decimal (

#.0###

), or allow the value to be invalid

setAllowsInvalid(true)

. Otherwise users may not be able to
input decimal values.

NumberFormatter

provides slightly different behavior to

stringToValue

than that of its superclass. If you have
specified a Class for values,

DefaultFormatter.setValueClass(java.lang.Class<?>)

, that is one of
of

Integer

,

Long

,

Float

,

Double

,

Byte

or

Short

and
the Format's

parseObject

returns an instance of

Number

, the corresponding instance of the value class
will be created using the constructor appropriate for the primitive
type the value class represents. For example:

setValueClass(Integer.class)

will cause the resulting
value to be created via

Integer.valueOf(((Number)formatter.parseObject(string)).intValue())

.
This is typically useful if you
wish to set a min/max value as the various

Number

implementations are generally not comparable to each other. This is also
useful if for some reason you need a specific

Number

implementation for your values.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in any field but the exponent
field will attempt to change the sign of the number to
positive/negative.

Pressing +/- (- is determined from the

DecimalFormatSymbols

associated with the

DecimalFormat

) in the exponent field will
attempt to change the sign of the exponent to positive/negative.

If you are displaying scientific numbers, you may wish to turn on
overwrite mode,

setOverwriteMode(true)

. For example:

```java
DecimalFormat decimalFormat = new DecimalFormat("0.000E0");
NumberFormatter textFormatter = new NumberFormatter(decimalFormat);
textFormatter.setOverwriteMode(true);
textFormatter.setAllowsInvalid(false);
```

If you are going to allow the user to enter decimal
values, you should either force the DecimalFormat to contain at least
one decimal (

#.0###

), or allow the value to be invalid

setAllowsInvalid(true)

. Otherwise users may not be able to
input decimal values.

NumberFormatter

provides slightly different behavior to

stringToValue

than that of its superclass. If you have
specified a Class for values,

DefaultFormatter.setValueClass(java.lang.Class<?>)

, that is one of
of

Integer

,

Long

,

Float

,

Double

,

Byte

or

Short

and
the Format's

parseObject

returns an instance of

Number

, the corresponding instance of the value class
will be created using the constructor appropriate for the primitive
type the value class represents. For example:

setValueClass(Integer.class)

will cause the resulting
value to be created via

Integer.valueOf(((Number)formatter.parseObject(string)).intValue())

.
This is typically useful if you
wish to set a min/max value as the various

Number

implementations are generally not comparable to each other. This is also
useful if for some reason you need a specific

Number

implementation for your values.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

DecimalFormat decimalFormat = new DecimalFormat("0.000E0");
NumberFormatter textFormatter = new NumberFormatter(decimalFormat);
textFormatter.setOverwriteMode(true);
textFormatter.setAllowsInvalid(false);

If you are going to allow the user to enter decimal
values, you should either force the DecimalFormat to contain at least
one decimal (

#.0###

), or allow the value to be invalid

setAllowsInvalid(true)

. Otherwise users may not be able to
input decimal values.

NumberFormatter

provides slightly different behavior to

stringToValue

than that of its superclass. If you have
specified a Class for values,

DefaultFormatter.setValueClass(java.lang.Class<?>)

, that is one of
of

Integer

,

Long

,

Float

,

Double

,

Byte

or

Short

and
the Format's

parseObject

returns an instance of

Number

, the corresponding instance of the value class
will be created using the constructor appropriate for the primitive
type the value class represents. For example:

setValueClass(Integer.class)

will cause the resulting
value to be created via

Integer.valueOf(((Number)formatter.parseObject(string)).intValue())

.
This is typically useful if you
wish to set a min/max value as the various

Number

implementations are generally not comparable to each other. This is also
useful if for some reason you need a specific

Number

implementation for your values.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

NumberFormatter

provides slightly different behavior to

stringToValue

than that of its superclass. If you have
specified a Class for values,

DefaultFormatter.setValueClass(java.lang.Class<?>)

, that is one of
of

Integer

,

Long

,

Float

,

Double

,

Byte

or

Short

and
the Format's

parseObject

returns an instance of

Number

, the corresponding instance of the value class
will be created using the constructor appropriate for the primitive
type the value class represents. For example:

setValueClass(Integer.class)

will cause the resulting
value to be created via

Integer.valueOf(((Number)formatter.parseObject(string)).intValue())

.
This is typically useful if you
wish to set a min/max value as the various

Number

implementations are generally not comparable to each other. This is also
useful if for some reason you need a specific

Number

implementation for your values.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NumberFormatter

()

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

NumberFormatter

​(

NumberFormat

format)

Creates a NumberFormatter with the specified Format instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

setFormat

​(

Format

format)

Sets the format that dictates the legal values that can be edited
and displayed.

- Methods declared in class javax.swing.text.

InternationalFormatter

clone

,

getActions

,

getFields

,

getFormat

,

getMaximum

,

getMinimum

,

install

,

setMaximum

,

setMinimum

,

stringToValue

,

valueToString

- Methods declared in class javax.swing.text.

DefaultFormatter

getAllowsInvalid

,

getCommitsOnValidEdit

,

getDocumentFilter

,

getNavigationFilter

,

getOverwriteMode

,

getValueClass

,

setAllowsInvalid

,

setCommitsOnValidEdit

,

setOverwriteMode

,

setValueClass

- Methods declared in class javax.swing.

JFormattedTextField.AbstractFormatter

getFormattedTextField

,

invalidEdit

,

setEditValid

,

uninstall

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

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

NumberFormatter

()

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

NumberFormatter

​(

NumberFormat

format)

Creates a NumberFormatter with the specified Format instance.

---

#### Constructor Summary

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

Creates a NumberFormatter with the specified Format instance.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

setFormat

​(

Format

format)

Sets the format that dictates the legal values that can be edited
and displayed.

- Methods declared in class javax.swing.text.

InternationalFormatter

clone

,

getActions

,

getFields

,

getFormat

,

getMaximum

,

getMinimum

,

install

,

setMaximum

,

setMinimum

,

stringToValue

,

valueToString

- Methods declared in class javax.swing.text.

DefaultFormatter

getAllowsInvalid

,

getCommitsOnValidEdit

,

getDocumentFilter

,

getNavigationFilter

,

getOverwriteMode

,

getValueClass

,

setAllowsInvalid

,

setCommitsOnValidEdit

,

setOverwriteMode

,

setValueClass

- Methods declared in class javax.swing.

JFormattedTextField.AbstractFormatter

getFormattedTextField

,

invalidEdit

,

setEditValid

,

uninstall

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

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

Sets the format that dictates the legal values that can be edited
and displayed.

Methods declared in class javax.swing.text.

InternationalFormatter

clone

,

getActions

,

getFields

,

getFormat

,

getMaximum

,

getMinimum

,

install

,

setMaximum

,

setMinimum

,

stringToValue

,

valueToString

---

#### Methods declared in class javax.swing.text. InternationalFormatter

Methods declared in class javax.swing.text.

DefaultFormatter

getAllowsInvalid

,

getCommitsOnValidEdit

,

getDocumentFilter

,

getNavigationFilter

,

getOverwriteMode

,

getValueClass

,

setAllowsInvalid

,

setCommitsOnValidEdit

,

setOverwriteMode

,

setValueClass

---

#### Methods declared in class javax.swing.text. DefaultFormatter

Methods declared in class javax.swing.

JFormattedTextField.AbstractFormatter

getFormattedTextField

,

invalidEdit

,

setEditValid

,

uninstall

---

#### Methods declared in class javax.swing. JFormattedTextField.AbstractFormatter

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

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

- NumberFormatter

```java
public NumberFormatter()
```

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

- NumberFormatter

```java
public NumberFormatter​(
NumberFormat
format)
```

Creates a NumberFormatter with the specified Format instance.

**Parameters:** format

- Format used to dictate legal values

============ METHOD DETAIL ==========

- Method Detail

- setFormat

```java
public void setFormat​(
Format
format)
```

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

NumberFormat.getNumberInstance()

method.

**Overrides:** setFormat

in class

InternationalFormatter
**Parameters:** format

- NumberFormat instance used to dictate legal values

Constructor Detail

- NumberFormatter

```java
public NumberFormatter()
```

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

- NumberFormatter

```java
public NumberFormatter​(
NumberFormat
format)
```

Creates a NumberFormatter with the specified Format instance.

**Parameters:** format

- Format used to dictate legal values

---

#### Constructor Detail

NumberFormatter

```java
public NumberFormatter()
```

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

---

#### NumberFormatter

public NumberFormatter()

Creates a

NumberFormatter

with the a default

NumberFormat

instance obtained from

NumberFormat.getNumberInstance()

.

NumberFormatter

```java
public NumberFormatter​(
NumberFormat
format)
```

Creates a NumberFormatter with the specified Format instance.

**Parameters:** format

- Format used to dictate legal values

---

#### NumberFormatter

public NumberFormatter​(

NumberFormat

format)

Creates a NumberFormatter with the specified Format instance.

Method Detail

- setFormat

```java
public void setFormat​(
Format
format)
```

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

NumberFormat.getNumberInstance()

method.

**Overrides:** setFormat

in class

InternationalFormatter
**Parameters:** format

- NumberFormat instance used to dictate legal values

---

#### Method Detail

setFormat

```java
public void setFormat​(
Format
format)
```

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

NumberFormat.getNumberInstance()

method.

**Overrides:** setFormat

in class

InternationalFormatter
**Parameters:** format

- NumberFormat instance used to dictate legal values

---

#### setFormat

public void setFormat​(

Format

format)

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

NumberFormat.getNumberInstance()

method.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

NumberFormat.getNumberInstance()

method.

---

