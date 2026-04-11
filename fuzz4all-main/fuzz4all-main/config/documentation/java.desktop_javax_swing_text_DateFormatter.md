# Class DateFormatter

**Source:** `java.desktop\javax\swing\text\DateFormatter.html`

### Class Description

```java
public class
DateFormatter

extends
InternationalFormatter
```

DateFormatter is an

InternationalFormatter

that does its
formatting by way of an instance of

java.text.DateFormat

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

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DateFormatter()

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

---

#### public DateFormatter​(
DateFormat
format)

Returns a DateFormatter configured with the specified

Format

instance.

**Parameters:**
- format

- Format used to dictate legal values

---

### Method Details

#### public void setFormat​(
DateFormat
format)

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

Dateformat.getDateInstance()

method.

**Parameters:**
- format

- DateFormat instance used for converting from/to Strings

---

### Additional Sections

#### Class DateFormatter

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatter
- - javax.swing.text.DefaultFormatter
- - javax.swing.text.InternationalFormatter
- - javax.swing.text.DateFormatter

javax.swing.JFormattedTextField.AbstractFormatter

- javax.swing.text.DefaultFormatter
- - javax.swing.text.InternationalFormatter
- - javax.swing.text.DateFormatter

javax.swing.text.DefaultFormatter

- javax.swing.text.InternationalFormatter
- - javax.swing.text.DateFormatter

javax.swing.text.InternationalFormatter

- javax.swing.text.DateFormatter

javax.swing.text.DateFormatter

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
DateFormatter

extends
InternationalFormatter
```

DateFormatter is an

InternationalFormatter

that does its
formatting by way of an instance of

java.text.DateFormat

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

**Since:** 1.4
**See Also:** DateFormat

,

Serialized Form

public class

DateFormatter

extends

InternationalFormatter

DateFormatter is an

InternationalFormatter

that does its
formatting by way of an instance of

java.text.DateFormat

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

DateFormatter

()

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

DateFormatter

​(

DateFormat

format)

Returns a DateFormatter configured with the specified

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

void

setFormat

​(

DateFormat

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

setFormat

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

DateFormatter

()

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

DateFormatter

​(

DateFormat

format)

Returns a DateFormatter configured with the specified

Format

instance.

---

#### Constructor Summary

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

Returns a DateFormatter configured with the specified

Format

instance.

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

DateFormat

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

setFormat

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

setFormat

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

- DateFormatter

```java
public DateFormatter()
```

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

- DateFormatter

```java
public DateFormatter​(
DateFormat
format)
```

Returns a DateFormatter configured with the specified

Format

instance.

**Parameters:** format

- Format used to dictate legal values

============ METHOD DETAIL ==========

- Method Detail

- setFormat

```java
public void setFormat​(
DateFormat
format)
```

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

Dateformat.getDateInstance()

method.

**Parameters:** format

- DateFormat instance used for converting from/to Strings

Constructor Detail

- DateFormatter

```java
public DateFormatter()
```

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

- DateFormatter

```java
public DateFormatter​(
DateFormat
format)
```

Returns a DateFormatter configured with the specified

Format

instance.

**Parameters:** format

- Format used to dictate legal values

---

#### Constructor Detail

DateFormatter

```java
public DateFormatter()
```

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

---

#### DateFormatter

public DateFormatter()

This is shorthand for

new DateFormatter(DateFormat.getDateInstance())

.

DateFormatter

```java
public DateFormatter​(
DateFormat
format)
```

Returns a DateFormatter configured with the specified

Format

instance.

**Parameters:** format

- Format used to dictate legal values

---

#### DateFormatter

public DateFormatter​(

DateFormat

format)

Returns a DateFormatter configured with the specified

Format

instance.

Method Detail

- setFormat

```java
public void setFormat​(
DateFormat
format)
```

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

Dateformat.getDateInstance()

method.

**Parameters:** format

- DateFormat instance used for converting from/to Strings

---

#### Method Detail

setFormat

```java
public void setFormat​(
DateFormat
format)
```

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

Dateformat.getDateInstance()

method.

**Parameters:** format

- DateFormat instance used for converting from/to Strings

---

#### setFormat

public void setFormat​(

DateFormat

format)

Sets the format that dictates the legal values that can be edited
and displayed.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

Dateformat.getDateInstance()

method.

If you have used the nullary constructor the value of this property
will be determined for the current locale by way of the

Dateformat.getDateInstance()

method.

---

