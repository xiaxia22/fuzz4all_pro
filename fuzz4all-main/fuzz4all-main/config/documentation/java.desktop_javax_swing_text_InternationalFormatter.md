# Class InternationalFormatter

**Source:** `java.desktop\javax\swing\text\InternationalFormatter.html`

### Class Description

```java
public class
InternationalFormatter

extends
DefaultFormatter
```

InternationalFormatter

extends

DefaultFormatter

,
using an instance of

java.text.Format

to handle the
conversion to a String, and the conversion from a String.

If

getAllowsInvalid()

is false, this will ask the

Format

to format the current text on every edit.

You can specify a minimum and maximum value by way of the

setMinimum

and

setMaximum

methods. In order
for this to work the values returned from

stringToValue

must be
comparable to the min/max values by way of the

Comparable

interface.

Be careful how you configure the

Format

and the

InternationalFormatter

, as it is possible to create a
situation where certain values can not be input. Consider the date
format 'M/d/yy', an

InternationalFormatter

that is always
valid (

setAllowsInvalid(false)

), is in overwrite mode
(

setOverwriteMode(true)

) and the date 7/1/99. In this
case the user will not be able to enter a two digit month or day of
month. To avoid this, the format should be 'MM/dd/yy'.

If

InternationalFormatter

is configured to only allow valid
values (

setAllowsInvalid(false)

), every valid edit will result
in the text of the

JFormattedTextField

being completely reset
from the

Format

.
The cursor position will also be adjusted as literal characters are
added/removed from the resulting String.

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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

#### public InternationalFormatter()

Creates an

InternationalFormatter

with no

Format

specified.

---

#### public InternationalFormatter​(
Format
format)

Creates an

InternationalFormatter

with the specified

Format

instance.

**Parameters:**
- format

- Format instance used for converting from/to Strings

---

### Method Details

#### public void setFormat​(
Format
format)

Sets the format that dictates the legal values that can be edited
and displayed.

**Parameters:**
- format

-

Format

instance used for converting
from/to Strings

---

#### public
Format
getFormat()

Returns the format that dictates the legal values that can be edited
and displayed.

**Returns:**
- Format instance used for converting from/to Strings

---

#### public void setMinimum​(
Comparable
<?> minimum)

Sets the minimum permissible value. If the

valueClass

has
not been specified, and

minimum

is non null, the

valueClass

will be set to that of the class of

minimum

.

**Parameters:**
- minimum

- Minimum legal value that can be input

**See Also:**
- DefaultFormatter.setValueClass(java.lang.Class<?>)

---

#### public
Comparable
<?> getMinimum()

Returns the minimum permissible value.

**Returns:**
- Minimum legal value that can be input

---

#### public void setMaximum​(
Comparable
<?> max)

Sets the maximum permissible value. If the

valueClass

has
not been specified, and

max

is non null, the

valueClass

will be set to that of the class of

max

.

**Parameters:**
- max

- Maximum legal value that can be input

**See Also:**
- DefaultFormatter.setValueClass(java.lang.Class<?>)

---

#### public
Comparable
<?> getMaximum()

Returns the maximum permissible value.

**Returns:**
- Maximum legal value that can be input

---

#### public void install​(
JFormattedTextField
ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:**
- install

in class

DefaultFormatter

**Parameters:**
- ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

---

#### public
String
valueToString​(
Object
value)
throws
ParseException

Returns a String representation of the Object

value

.
This invokes

format

on the current

Format

.

**Overrides:**
- valueToString

in class

DefaultFormatter

**Parameters:**
- value

- Value to convert

**Returns:**
- String representation of value

**Throws:**
- ParseException

- if there is an error in the conversion

---

#### public
Object
stringToValue​(
String
text)
throws
ParseException

Returns the

Object

representation of the

String

text

.

**Overrides:**
- stringToValue

in class

DefaultFormatter

**Parameters:**
- text

-

String

to convert

**Returns:**
- Object

representation of text

**Throws:**
- ParseException

- if there is an error in the conversion

---

#### public
Format.Field
[] getFields​(int offset)

Returns the

Format.Field

constants associated with
the text at

offset

. If

offset

is not
a valid location into the current text, this will return an
empty array.

**Parameters:**
- offset

- offset into text to be examined

**Returns:**
- Format.Field constants associated with the text at the
given position.

---

#### public
Object
clone()
throws
CloneNotSupportedException

Creates a copy of the DefaultFormatter.

**Overrides:**
- clone

in class

DefaultFormatter

**Returns:**
- copy of the DefaultFormatter

**Throws:**
- CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.

**See Also:**
- Cloneable

---

#### protected
Action
[] getActions()

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

**Overrides:**
- getActions

in class

JFormattedTextField.AbstractFormatter

**Returns:**
- Array of Actions to install on JFormattedTextField

---

### Additional Sections

#### Class InternationalFormatter

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatter
- - javax.swing.text.DefaultFormatter
- - javax.swing.text.InternationalFormatter

javax.swing.JFormattedTextField.AbstractFormatter

- javax.swing.text.DefaultFormatter
- - javax.swing.text.InternationalFormatter

javax.swing.text.DefaultFormatter

- javax.swing.text.InternationalFormatter

javax.swing.text.InternationalFormatter

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** DateFormatter

,

NumberFormatter

```java
public class
InternationalFormatter

extends
DefaultFormatter
```

InternationalFormatter

extends

DefaultFormatter

,
using an instance of

java.text.Format

to handle the
conversion to a String, and the conversion from a String.

If

getAllowsInvalid()

is false, this will ask the

Format

to format the current text on every edit.

You can specify a minimum and maximum value by way of the

setMinimum

and

setMaximum

methods. In order
for this to work the values returned from

stringToValue

must be
comparable to the min/max values by way of the

Comparable

interface.

Be careful how you configure the

Format

and the

InternationalFormatter

, as it is possible to create a
situation where certain values can not be input. Consider the date
format 'M/d/yy', an

InternationalFormatter

that is always
valid (

setAllowsInvalid(false)

), is in overwrite mode
(

setOverwriteMode(true)

) and the date 7/1/99. In this
case the user will not be able to enter a two digit month or day of
month. To avoid this, the format should be 'MM/dd/yy'.

If

InternationalFormatter

is configured to only allow valid
values (

setAllowsInvalid(false)

), every valid edit will result
in the text of the

JFormattedTextField

being completely reset
from the

Format

.
The cursor position will also be adjusted as literal characters are
added/removed from the resulting String.

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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
**See Also:** Format

,

Comparable

,

Serialized Form

public class

InternationalFormatter

extends

DefaultFormatter

InternationalFormatter

extends

DefaultFormatter

,
using an instance of

java.text.Format

to handle the
conversion to a String, and the conversion from a String.

If

getAllowsInvalid()

is false, this will ask the

Format

to format the current text on every edit.

You can specify a minimum and maximum value by way of the

setMinimum

and

setMaximum

methods. In order
for this to work the values returned from

stringToValue

must be
comparable to the min/max values by way of the

Comparable

interface.

Be careful how you configure the

Format

and the

InternationalFormatter

, as it is possible to create a
situation where certain values can not be input. Consider the date
format 'M/d/yy', an

InternationalFormatter

that is always
valid (

setAllowsInvalid(false)

), is in overwrite mode
(

setOverwriteMode(true)

) and the date 7/1/99. In this
case the user will not be able to enter a two digit month or day of
month. To avoid this, the format should be 'MM/dd/yy'.

If

InternationalFormatter

is configured to only allow valid
values (

setAllowsInvalid(false)

), every valid edit will result
in the text of the

JFormattedTextField

being completely reset
from the

Format

.
The cursor position will also be adjusted as literal characters are
added/removed from the resulting String.

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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

If

getAllowsInvalid()

is false, this will ask the

Format

to format the current text on every edit.

You can specify a minimum and maximum value by way of the

setMinimum

and

setMaximum

methods. In order
for this to work the values returned from

stringToValue

must be
comparable to the min/max values by way of the

Comparable

interface.

Be careful how you configure the

Format

and the

InternationalFormatter

, as it is possible to create a
situation where certain values can not be input. Consider the date
format 'M/d/yy', an

InternationalFormatter

that is always
valid (

setAllowsInvalid(false)

), is in overwrite mode
(

setOverwriteMode(true)

) and the date 7/1/99. In this
case the user will not be able to enter a two digit month or day of
month. To avoid this, the format should be 'MM/dd/yy'.

If

InternationalFormatter

is configured to only allow valid
values (

setAllowsInvalid(false)

), every valid edit will result
in the text of the

JFormattedTextField

being completely reset
from the

Format

.
The cursor position will also be adjusted as literal characters are
added/removed from the resulting String.

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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

You can specify a minimum and maximum value by way of the

setMinimum

and

setMaximum

methods. In order
for this to work the values returned from

stringToValue

must be
comparable to the min/max values by way of the

Comparable

interface.

Be careful how you configure the

Format

and the

InternationalFormatter

, as it is possible to create a
situation where certain values can not be input. Consider the date
format 'M/d/yy', an

InternationalFormatter

that is always
valid (

setAllowsInvalid(false)

), is in overwrite mode
(

setOverwriteMode(true)

) and the date 7/1/99. In this
case the user will not be able to enter a two digit month or day of
month. To avoid this, the format should be 'MM/dd/yy'.

If

InternationalFormatter

is configured to only allow valid
values (

setAllowsInvalid(false)

), every valid edit will result
in the text of the

JFormattedTextField

being completely reset
from the

Format

.
The cursor position will also be adjusted as literal characters are
added/removed from the resulting String.

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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

Be careful how you configure the

Format

and the

InternationalFormatter

, as it is possible to create a
situation where certain values can not be input. Consider the date
format 'M/d/yy', an

InternationalFormatter

that is always
valid (

setAllowsInvalid(false)

), is in overwrite mode
(

setOverwriteMode(true)

) and the date 7/1/99. In this
case the user will not be able to enter a two digit month or day of
month. To avoid this, the format should be 'MM/dd/yy'.

If

InternationalFormatter

is configured to only allow valid
values (

setAllowsInvalid(false)

), every valid edit will result
in the text of the

JFormattedTextField

being completely reset
from the

Format

.
The cursor position will also be adjusted as literal characters are
added/removed from the resulting String.

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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

If

InternationalFormatter

is configured to only allow valid
values (

setAllowsInvalid(false)

), every valid edit will result
in the text of the

JFormattedTextField

being completely reset
from the

Format

.
The cursor position will also be adjusted as literal characters are
added/removed from the resulting String.

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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

InternationalFormatter

's behavior of

stringToValue

is slightly different than that of

DefaultTextFormatter

, it does the following:

- parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

InternationalFormatter

implements

stringToValue

in this manner so that you can specify an alternate Class than

Format

may return.

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

parseObject

is invoked on the

Format

specified by

setFormat

If a Class has been set for the values (

setValueClass

),
supers implementation is invoked to convert the value returned
from

parseObject

to the appropriate class.

If a

ParseException

has not been thrown, and the value
is outside the min/max a

ParseException

is thrown.

The value is returned.

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

InternationalFormatter

()

Creates an

InternationalFormatter

with no

Format

specified.

InternationalFormatter

​(

Format

format)

Creates an

InternationalFormatter

with the specified

Format

instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the DefaultFormatter.

protected

Action

[]

getActions

()

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

Format.Field

[]

getFields

​(int offset)

Returns the

Format.Field

constants associated with
the text at

offset

.

Format

getFormat

()

Returns the format that dictates the legal values that can be edited
and displayed.

Comparable

<?>

getMaximum

()

Returns the maximum permissible value.

Comparable

<?>

getMinimum

()

Returns the minimum permissible value.

void

install

​(

JFormattedTextField

ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.

void

setFormat

​(

Format

format)

Sets the format that dictates the legal values that can be edited
and displayed.

void

setMaximum

​(

Comparable

<?> max)

Sets the maximum permissible value.

void

setMinimum

​(

Comparable

<?> minimum)

Sets the minimum permissible value.

Object

stringToValue

​(

String

text)

Returns the

Object

representation of the

String

text

.

String

valueToString

​(

Object

value)

Returns a String representation of the Object

value

.

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

InternationalFormatter

()

Creates an

InternationalFormatter

with no

Format

specified.

InternationalFormatter

​(

Format

format)

Creates an

InternationalFormatter

with the specified

Format

instance.

---

#### Constructor Summary

Creates an

InternationalFormatter

with no

Format

specified.

Creates an

InternationalFormatter

with the specified

Format

instance.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the DefaultFormatter.

protected

Action

[]

getActions

()

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

Format.Field

[]

getFields

​(int offset)

Returns the

Format.Field

constants associated with
the text at

offset

.

Format

getFormat

()

Returns the format that dictates the legal values that can be edited
and displayed.

Comparable

<?>

getMaximum

()

Returns the maximum permissible value.

Comparable

<?>

getMinimum

()

Returns the minimum permissible value.

void

install

​(

JFormattedTextField

ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.

void

setFormat

​(

Format

format)

Sets the format that dictates the legal values that can be edited
and displayed.

void

setMaximum

​(

Comparable

<?> max)

Sets the maximum permissible value.

void

setMinimum

​(

Comparable

<?> minimum)

Sets the minimum permissible value.

Object

stringToValue

​(

String

text)

Returns the

Object

representation of the

String

text

.

String

valueToString

​(

Object

value)

Returns a String representation of the Object

value

.

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

Creates a copy of the DefaultFormatter.

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

Returns the

Format.Field

constants associated with
the text at

offset

.

Returns the format that dictates the legal values that can be edited
and displayed.

Returns the maximum permissible value.

Returns the minimum permissible value.

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.

Sets the format that dictates the legal values that can be edited
and displayed.

Sets the maximum permissible value.

Sets the minimum permissible value.

Returns the

Object

representation of the

String

text

.

Returns a String representation of the Object

value

.

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

- InternationalFormatter

```java
public InternationalFormatter()
```

Creates an

InternationalFormatter

with no

Format

specified.

- InternationalFormatter

```java
public InternationalFormatter​(
Format
format)
```

Creates an

InternationalFormatter

with the specified

Format

instance.

**Parameters:** format

- Format instance used for converting from/to Strings

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

**Parameters:** format

-

Format

instance used for converting
from/to Strings

- getFormat

```java
public
Format
getFormat()
```

Returns the format that dictates the legal values that can be edited
and displayed.

**Returns:** Format instance used for converting from/to Strings

- setMinimum

```java
public void setMinimum​(
Comparable
<?> minimum)
```

Sets the minimum permissible value. If the

valueClass

has
not been specified, and

minimum

is non null, the

valueClass

will be set to that of the class of

minimum

.

**Parameters:** minimum

- Minimum legal value that can be input
**See Also:** DefaultFormatter.setValueClass(java.lang.Class<?>)

- getMinimum

```java
public
Comparable
<?> getMinimum()
```

Returns the minimum permissible value.

**Returns:** Minimum legal value that can be input

- setMaximum

```java
public void setMaximum​(
Comparable
<?> max)
```

Sets the maximum permissible value. If the

valueClass

has
not been specified, and

max

is non null, the

valueClass

will be set to that of the class of

max

.

**Parameters:** max

- Maximum legal value that can be input
**See Also:** DefaultFormatter.setValueClass(java.lang.Class<?>)

- getMaximum

```java
public
Comparable
<?> getMaximum()
```

Returns the maximum permissible value.

**Returns:** Maximum legal value that can be input

- install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:** install

in class

DefaultFormatter
**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

- valueToString

```java
public
String
valueToString​(
Object
value)
throws
ParseException
```

Returns a String representation of the Object

value

.
This invokes

format

on the current

Format

.

**Overrides:** valueToString

in class

DefaultFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

- stringToValue

```java
public
Object
stringToValue​(
String
text)
throws
ParseException
```

Returns the

Object

representation of the

String

text

.

**Overrides:** stringToValue

in class

DefaultFormatter
**Parameters:** text

-

String

to convert
**Returns:** Object

representation of text
**Throws:** ParseException

- if there is an error in the conversion

- getFields

```java
public
Format.Field
[] getFields​(int offset)
```

Returns the

Format.Field

constants associated with
the text at

offset

. If

offset

is not
a valid location into the current text, this will return an
empty array.

**Parameters:** offset

- offset into text to be examined
**Returns:** Format.Field constants associated with the text at the
given position.

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Creates a copy of the DefaultFormatter.

**Overrides:** clone

in class

DefaultFormatter
**Returns:** copy of the DefaultFormatter
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

- getActions

```java
protected
Action
[] getActions()
```

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

**Overrides:** getActions

in class

JFormattedTextField.AbstractFormatter
**Returns:** Array of Actions to install on JFormattedTextField

Constructor Detail

- InternationalFormatter

```java
public InternationalFormatter()
```

Creates an

InternationalFormatter

with no

Format

specified.

- InternationalFormatter

```java
public InternationalFormatter​(
Format
format)
```

Creates an

InternationalFormatter

with the specified

Format

instance.

**Parameters:** format

- Format instance used for converting from/to Strings

---

#### Constructor Detail

InternationalFormatter

```java
public InternationalFormatter()
```

Creates an

InternationalFormatter

with no

Format

specified.

---

#### InternationalFormatter

public InternationalFormatter()

Creates an

InternationalFormatter

with no

Format

specified.

InternationalFormatter

```java
public InternationalFormatter​(
Format
format)
```

Creates an

InternationalFormatter

with the specified

Format

instance.

**Parameters:** format

- Format instance used for converting from/to Strings

---

#### InternationalFormatter

public InternationalFormatter​(

Format

format)

Creates an

InternationalFormatter

with the specified

Format

instance.

Method Detail

- setFormat

```java
public void setFormat​(
Format
format)
```

Sets the format that dictates the legal values that can be edited
and displayed.

**Parameters:** format

-

Format

instance used for converting
from/to Strings

- getFormat

```java
public
Format
getFormat()
```

Returns the format that dictates the legal values that can be edited
and displayed.

**Returns:** Format instance used for converting from/to Strings

- setMinimum

```java
public void setMinimum​(
Comparable
<?> minimum)
```

Sets the minimum permissible value. If the

valueClass

has
not been specified, and

minimum

is non null, the

valueClass

will be set to that of the class of

minimum

.

**Parameters:** minimum

- Minimum legal value that can be input
**See Also:** DefaultFormatter.setValueClass(java.lang.Class<?>)

- getMinimum

```java
public
Comparable
<?> getMinimum()
```

Returns the minimum permissible value.

**Returns:** Minimum legal value that can be input

- setMaximum

```java
public void setMaximum​(
Comparable
<?> max)
```

Sets the maximum permissible value. If the

valueClass

has
not been specified, and

max

is non null, the

valueClass

will be set to that of the class of

max

.

**Parameters:** max

- Maximum legal value that can be input
**See Also:** DefaultFormatter.setValueClass(java.lang.Class<?>)

- getMaximum

```java
public
Comparable
<?> getMaximum()
```

Returns the maximum permissible value.

**Returns:** Maximum legal value that can be input

- install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:** install

in class

DefaultFormatter
**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

- valueToString

```java
public
String
valueToString​(
Object
value)
throws
ParseException
```

Returns a String representation of the Object

value

.
This invokes

format

on the current

Format

.

**Overrides:** valueToString

in class

DefaultFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

- stringToValue

```java
public
Object
stringToValue​(
String
text)
throws
ParseException
```

Returns the

Object

representation of the

String

text

.

**Overrides:** stringToValue

in class

DefaultFormatter
**Parameters:** text

-

String

to convert
**Returns:** Object

representation of text
**Throws:** ParseException

- if there is an error in the conversion

- getFields

```java
public
Format.Field
[] getFields​(int offset)
```

Returns the

Format.Field

constants associated with
the text at

offset

. If

offset

is not
a valid location into the current text, this will return an
empty array.

**Parameters:** offset

- offset into text to be examined
**Returns:** Format.Field constants associated with the text at the
given position.

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Creates a copy of the DefaultFormatter.

**Overrides:** clone

in class

DefaultFormatter
**Returns:** copy of the DefaultFormatter
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

- getActions

```java
protected
Action
[] getActions()
```

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

**Overrides:** getActions

in class

JFormattedTextField.AbstractFormatter
**Returns:** Array of Actions to install on JFormattedTextField

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

**Parameters:** format

-

Format

instance used for converting
from/to Strings

---

#### setFormat

public void setFormat​(

Format

format)

Sets the format that dictates the legal values that can be edited
and displayed.

getFormat

```java
public
Format
getFormat()
```

Returns the format that dictates the legal values that can be edited
and displayed.

**Returns:** Format instance used for converting from/to Strings

---

#### getFormat

public

Format

getFormat()

Returns the format that dictates the legal values that can be edited
and displayed.

setMinimum

```java
public void setMinimum​(
Comparable
<?> minimum)
```

Sets the minimum permissible value. If the

valueClass

has
not been specified, and

minimum

is non null, the

valueClass

will be set to that of the class of

minimum

.

**Parameters:** minimum

- Minimum legal value that can be input
**See Also:** DefaultFormatter.setValueClass(java.lang.Class<?>)

---

#### setMinimum

public void setMinimum​(

Comparable

<?> minimum)

Sets the minimum permissible value. If the

valueClass

has
not been specified, and

minimum

is non null, the

valueClass

will be set to that of the class of

minimum

.

getMinimum

```java
public
Comparable
<?> getMinimum()
```

Returns the minimum permissible value.

**Returns:** Minimum legal value that can be input

---

#### getMinimum

public

Comparable

<?> getMinimum()

Returns the minimum permissible value.

setMaximum

```java
public void setMaximum​(
Comparable
<?> max)
```

Sets the maximum permissible value. If the

valueClass

has
not been specified, and

max

is non null, the

valueClass

will be set to that of the class of

max

.

**Parameters:** max

- Maximum legal value that can be input
**See Also:** DefaultFormatter.setValueClass(java.lang.Class<?>)

---

#### setMaximum

public void setMaximum​(

Comparable

<?> max)

Sets the maximum permissible value. If the

valueClass

has
not been specified, and

max

is non null, the

valueClass

will be set to that of the class of

max

.

getMaximum

```java
public
Comparable
<?> getMaximum()
```

Returns the maximum permissible value.

**Returns:** Maximum legal value that can be input

---

#### getMaximum

public

Comparable

<?> getMaximum()

Returns the maximum permissible value.

install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:** install

in class

DefaultFormatter
**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

---

#### install

public void install​(

JFormattedTextField

ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

valueToString

```java
public
String
valueToString​(
Object
value)
throws
ParseException
```

Returns a String representation of the Object

value

.
This invokes

format

on the current

Format

.

**Overrides:** valueToString

in class

DefaultFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

---

#### valueToString

public

String

valueToString​(

Object

value)
throws

ParseException

Returns a String representation of the Object

value

.
This invokes

format

on the current

Format

.

stringToValue

```java
public
Object
stringToValue​(
String
text)
throws
ParseException
```

Returns the

Object

representation of the

String

text

.

**Overrides:** stringToValue

in class

DefaultFormatter
**Parameters:** text

-

String

to convert
**Returns:** Object

representation of text
**Throws:** ParseException

- if there is an error in the conversion

---

#### stringToValue

public

Object

stringToValue​(

String

text)
throws

ParseException

Returns the

Object

representation of the

String

text

.

getFields

```java
public
Format.Field
[] getFields​(int offset)
```

Returns the

Format.Field

constants associated with
the text at

offset

. If

offset

is not
a valid location into the current text, this will return an
empty array.

**Parameters:** offset

- offset into text to be examined
**Returns:** Format.Field constants associated with the text at the
given position.

---

#### getFields

public

Format.Field

[] getFields​(int offset)

Returns the

Format.Field

constants associated with
the text at

offset

. If

offset

is not
a valid location into the current text, this will return an
empty array.

clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Creates a copy of the DefaultFormatter.

**Overrides:** clone

in class

DefaultFormatter
**Returns:** copy of the DefaultFormatter
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

---

#### clone

public

Object

clone()
throws

CloneNotSupportedException

Creates a copy of the DefaultFormatter.

getActions

```java
protected
Action
[] getActions()
```

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

**Overrides:** getActions

in class

JFormattedTextField.AbstractFormatter
**Returns:** Array of Actions to install on JFormattedTextField

---

#### getActions

protected

Action

[] getActions()

If

getSupportsIncrement

returns true, this returns
two Actions suitable for incrementing/decrementing the value.

---

