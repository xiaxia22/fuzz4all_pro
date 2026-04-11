# Class MaskFormatter

**Source:** `java.desktop\javax\swing\text\MaskFormatter.html`

### Class Description

```java
public class
MaskFormatter

extends
DefaultFormatter
```

MaskFormatter

is used to format and edit strings. The behavior
of a

MaskFormatter

is controlled by way of a String mask
that specifies the valid characters that can be contained at a particular
location in the

Document

model. The following characters can
be specified:

Valid characters and their descriptions

Character

Description

#

Any valid number, uses

Character.isDigit

.

'

Escape character, used to escape any of the special formatting
characters.

U

Any character (

Character.isLetter

). All lowercase letters are
mapped to upper case.

L

Any character (

Character.isLetter

). All upper case letters
are mapped to lower case.

A

Any character or number (

Character.isLetter

or

Character.isDigit

).

?

Any character (

Character.isLetter

).

*

Anything.

H

Any hex character (0-9, a-f or A-F).

Typically characters correspond to one char, but in certain languages this
is not the case. The mask is on a per character basis, and will thus
adjust to fit as many chars as are needed.

You can further restrict the characters that can be input by the

setInvalidCharacters

and

setValidCharacters

methods.

setInvalidCharacters

allows you to specify
which characters are not legal.

setValidCharacters

allows
you to specify which characters are valid. For example, the following
code block is equivalent to a mask of '0xHHH' with no invalid/valid
characters:

```java
MaskFormatter formatter = new MaskFormatter("0x***");
formatter.setValidCharacters("0123456789abcdefABCDEF");
```

When initially formatting a value if the length of the string is
less than the length of the mask, two things can happen. Either
the placeholder string will be used, or the placeholder character will
be used. Precedence is given to the placeholder string. For example:

```java
MaskFormatter formatter = new MaskFormatter("###-####");
formatter.setPlaceholderCharacter('_');
formatter.getDisplayValue(tf, "123");
```

Would result in the string '123-____'. If

setPlaceholder("555-1212")

was invoked '123-1212' would
result. The placeholder String is only used on the initial format,
on subsequent formats only the placeholder character will be used.

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

#### public MaskFormatter()

Creates a MaskFormatter with no mask.

---

#### public MaskFormatter​(
String
mask)
throws
ParseException

Creates a

MaskFormatter

with the specified mask.
A

ParseException

will be thrown if

mask

is an invalid mask.

**Parameters:**
- mask

- the mask

**Throws:**
- ParseException

- if mask does not contain valid mask characters

---

### Method Details

#### public void setMask​(
String
mask)
throws
ParseException

Sets the mask dictating the legal characters.
This will throw a

ParseException

if

mask

is
not valid.

**Parameters:**
- mask

- the mask

**Throws:**
- ParseException

- if mask does not contain valid mask characters

---

#### public
String
getMask()

Returns the formatting mask.

**Returns:**
- Mask dictating legal character values.

---

#### public void setValidCharacters​(
String
validCharacters)

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the invalid characters.

**Parameters:**
- validCharacters

- If non-null, specifies legal characters.

---

#### public
String
getValidCharacters()

Returns the valid characters that can be input.

**Returns:**
- Legal characters

---

#### public void setInvalidCharacters​(
String
invalidCharacters)

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the valid characters.

**Parameters:**
- invalidCharacters

- If non-null, specifies illegal characters.

---

#### public
String
getInvalidCharacters()

Returns the characters that are not valid for input.

**Returns:**
- illegal characters.

---

#### public void setPlaceholder​(
String
placeholder)

Sets the string to use if the value does not completely fill in
the mask. A null value implies the placeholder char should be used.

**Parameters:**
- placeholder

- String used when formatting if the value does not
completely fill the mask

---

#### public
String
getPlaceholder()

Returns the String to use if the value does not completely fill
in the mask.

**Returns:**
- String used when formatting if the value does not
completely fill the mask

---

#### public void setPlaceholderCharacter​(char placeholder)

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in. The default value is
a space.

This is only applicable if the placeholder string has not been
specified, or does not completely fill in the mask.

**Parameters:**
- placeholder

- Character used when formatting if the value does not
completely fill the mask

---

#### public char getPlaceholderCharacter()

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

**Returns:**
- Character used when formatting if the value does not
completely fill the mask

---

#### public void setValueContainsLiteralCharacters​(boolean containsLiteralChars)

If true, the returned value and set value will also contain the literal
characters in mask.

For example, if the mask is

'(###) ###-####'

, the
current value is

'(415) 555-1212'

, and

valueContainsLiteralCharacters

is
true

stringToValue

will return

'(415) 555-1212'

. On the other hand, if

valueContainsLiteralCharacters

is false,

stringToValue

will return

'4155551212'

.

**Parameters:**
- containsLiteralChars

- Used to indicate if literal characters in
mask should be returned in stringToValue

---

#### public boolean getValueContainsLiteralCharacters()

Returns true if

stringToValue

should return literal
characters in the mask.

**Returns:**
- True if literal characters in mask should be returned in
stringToValue

---

#### public
Object
stringToValue​(
String
value)
throws
ParseException

Parses the text, returning the appropriate Object representation of
the String

value

. This strips the literal characters as
necessary and invokes supers

stringToValue

, so that if
you have specified a value class (

setValueClass

) an
instance of it will be created. This will throw a

ParseException

if the value does not match the current
mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

**Overrides:**
- stringToValue

in class

DefaultFormatter

**Parameters:**
- value

- String to convert

**Returns:**
- Object representation of text

**Throws:**
- ParseException

- if there is an error in the conversion

**See Also:**
- setValueContainsLiteralCharacters(boolean)

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

based on the mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

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

**See Also:**
- setValueContainsLiteralCharacters(boolean)

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

### Additional Sections

#### Class MaskFormatter

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatter
- - javax.swing.text.DefaultFormatter
- - javax.swing.text.MaskFormatter

javax.swing.JFormattedTextField.AbstractFormatter

- javax.swing.text.DefaultFormatter
- - javax.swing.text.MaskFormatter

javax.swing.text.DefaultFormatter

- javax.swing.text.MaskFormatter

javax.swing.text.MaskFormatter

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
MaskFormatter

extends
DefaultFormatter
```

MaskFormatter

is used to format and edit strings. The behavior
of a

MaskFormatter

is controlled by way of a String mask
that specifies the valid characters that can be contained at a particular
location in the

Document

model. The following characters can
be specified:

Valid characters and their descriptions

Character

Description

#

Any valid number, uses

Character.isDigit

.

'

Escape character, used to escape any of the special formatting
characters.

U

Any character (

Character.isLetter

). All lowercase letters are
mapped to upper case.

L

Any character (

Character.isLetter

). All upper case letters
are mapped to lower case.

A

Any character or number (

Character.isLetter

or

Character.isDigit

).

?

Any character (

Character.isLetter

).

*

Anything.

H

Any hex character (0-9, a-f or A-F).

Typically characters correspond to one char, but in certain languages this
is not the case. The mask is on a per character basis, and will thus
adjust to fit as many chars as are needed.

You can further restrict the characters that can be input by the

setInvalidCharacters

and

setValidCharacters

methods.

setInvalidCharacters

allows you to specify
which characters are not legal.

setValidCharacters

allows
you to specify which characters are valid. For example, the following
code block is equivalent to a mask of '0xHHH' with no invalid/valid
characters:

```java
MaskFormatter formatter = new MaskFormatter("0x***");
formatter.setValidCharacters("0123456789abcdefABCDEF");
```

When initially formatting a value if the length of the string is
less than the length of the mask, two things can happen. Either
the placeholder string will be used, or the placeholder character will
be used. Precedence is given to the placeholder string. For example:

```java
MaskFormatter formatter = new MaskFormatter("###-####");
formatter.setPlaceholderCharacter('_');
formatter.getDisplayValue(tf, "123");
```

Would result in the string '123-____'. If

setPlaceholder("555-1212")

was invoked '123-1212' would
result. The placeholder String is only used on the initial format,
on subsequent formats only the placeholder character will be used.

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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
**See Also:** Serialized Form

public class

MaskFormatter

extends

DefaultFormatter

MaskFormatter

is used to format and edit strings. The behavior
of a

MaskFormatter

is controlled by way of a String mask
that specifies the valid characters that can be contained at a particular
location in the

Document

model. The following characters can
be specified:

Valid characters and their descriptions

Character

Description

#

Any valid number, uses

Character.isDigit

.

'

Escape character, used to escape any of the special formatting
characters.

U

Any character (

Character.isLetter

). All lowercase letters are
mapped to upper case.

L

Any character (

Character.isLetter

). All upper case letters
are mapped to lower case.

A

Any character or number (

Character.isLetter

or

Character.isDigit

).

?

Any character (

Character.isLetter

).

*

Anything.

H

Any hex character (0-9, a-f or A-F).

Typically characters correspond to one char, but in certain languages this
is not the case. The mask is on a per character basis, and will thus
adjust to fit as many chars as are needed.

You can further restrict the characters that can be input by the

setInvalidCharacters

and

setValidCharacters

methods.

setInvalidCharacters

allows you to specify
which characters are not legal.

setValidCharacters

allows
you to specify which characters are valid. For example, the following
code block is equivalent to a mask of '0xHHH' with no invalid/valid
characters:

```java
MaskFormatter formatter = new MaskFormatter("0x***");
formatter.setValidCharacters("0123456789abcdefABCDEF");
```

When initially formatting a value if the length of the string is
less than the length of the mask, two things can happen. Either
the placeholder string will be used, or the placeholder character will
be used. Precedence is given to the placeholder string. For example:

```java
MaskFormatter formatter = new MaskFormatter("###-####");
formatter.setPlaceholderCharacter('_');
formatter.getDisplayValue(tf, "123");
```

Would result in the string '123-____'. If

setPlaceholder("555-1212")

was invoked '123-1212' would
result. The placeholder String is only used on the initial format,
on subsequent formats only the placeholder character will be used.

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

Typically characters correspond to one char, but in certain languages this
is not the case. The mask is on a per character basis, and will thus
adjust to fit as many chars as are needed.

You can further restrict the characters that can be input by the

setInvalidCharacters

and

setValidCharacters

methods.

setInvalidCharacters

allows you to specify
which characters are not legal.

setValidCharacters

allows
you to specify which characters are valid. For example, the following
code block is equivalent to a mask of '0xHHH' with no invalid/valid
characters:

```java
MaskFormatter formatter = new MaskFormatter("0x***");
formatter.setValidCharacters("0123456789abcdefABCDEF");
```

When initially formatting a value if the length of the string is
less than the length of the mask, two things can happen. Either
the placeholder string will be used, or the placeholder character will
be used. Precedence is given to the placeholder string. For example:

```java
MaskFormatter formatter = new MaskFormatter("###-####");
formatter.setPlaceholderCharacter('_');
formatter.getDisplayValue(tf, "123");
```

Would result in the string '123-____'. If

setPlaceholder("555-1212")

was invoked '123-1212' would
result. The placeholder String is only used on the initial format,
on subsequent formats only the placeholder character will be used.

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

You can further restrict the characters that can be input by the

setInvalidCharacters

and

setValidCharacters

methods.

setInvalidCharacters

allows you to specify
which characters are not legal.

setValidCharacters

allows
you to specify which characters are valid. For example, the following
code block is equivalent to a mask of '0xHHH' with no invalid/valid
characters:

```java
MaskFormatter formatter = new MaskFormatter("0x***");
formatter.setValidCharacters("0123456789abcdefABCDEF");
```

When initially formatting a value if the length of the string is
less than the length of the mask, two things can happen. Either
the placeholder string will be used, or the placeholder character will
be used. Precedence is given to the placeholder string. For example:

```java
MaskFormatter formatter = new MaskFormatter("###-####");
formatter.setPlaceholderCharacter('_');
formatter.getDisplayValue(tf, "123");
```

Would result in the string '123-____'. If

setPlaceholder("555-1212")

was invoked '123-1212' would
result. The placeholder String is only used on the initial format,
on subsequent formats only the placeholder character will be used.

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

MaskFormatter formatter = new MaskFormatter("0x***");
formatter.setValidCharacters("0123456789abcdefABCDEF");

When initially formatting a value if the length of the string is
less than the length of the mask, two things can happen. Either
the placeholder string will be used, or the placeholder character will
be used. Precedence is given to the placeholder string. For example:

```java
MaskFormatter formatter = new MaskFormatter("###-####");
formatter.setPlaceholderCharacter('_');
formatter.getDisplayValue(tf, "123");
```

Would result in the string '123-____'. If

setPlaceholder("555-1212")

was invoked '123-1212' would
result. The placeholder String is only used on the initial format,
on subsequent formats only the placeholder character will be used.

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

MaskFormatter formatter = new MaskFormatter("###-####");
formatter.setPlaceholderCharacter('_');
formatter.getDisplayValue(tf, "123");

Would result in the string '123-____'. If

setPlaceholder("555-1212")

was invoked '123-1212' would
result. The placeholder String is only used on the initial format,
on subsequent formats only the placeholder character will be used.

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

If a

MaskFormatter

is configured to only allow valid characters
(

setAllowsInvalid(false)

) literal characters will be skipped as
necessary when editing. Consider a

MaskFormatter

with
the mask "###-####" and current value "555-1212". Using the right
arrow key to navigate through the field will result in (| indicates the
position of the caret):

```java
|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212
```

The '-' is a literal (non-editable) character, and is skipped.

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

|555-1212
5|55-1212
55|5-1212
555-|1212
555-1|212

Similar behavior will result when editing. Consider inserting the string
'123-45' and '12345' into the

MaskFormatter

in the
previous example. Both inserts will result in the same String,
'123-45__'. When

MaskFormatter

is processing the insert at character position 3 (the '-'), two things can
happen:

- If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

If the inserted character is '-', it is accepted.

If the inserted character matches the mask for the next non-literal
character, it is accepted at the new location.

Anything else results in an invalid edit

By default

MaskFormatter

will not allow invalid edits, you can
change this with the

setAllowsInvalid

method, and will
commit edits on valid edits (use the

setCommitsOnValidEdit

to
change this).

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

By default,

MaskFormatter

is in overwrite mode. That is as
characters are typed a new character is not inserted, rather the character
at the current location is replaced with the newly typed character. You
can change this behavior by way of the method

setOverwriteMode

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

MaskFormatter

()

Creates a MaskFormatter with no mask.

MaskFormatter

​(

String

mask)

Creates a

MaskFormatter

with the specified mask.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getInvalidCharacters

()

Returns the characters that are not valid for input.

String

getMask

()

Returns the formatting mask.

String

getPlaceholder

()

Returns the String to use if the value does not completely fill
in the mask.

char

getPlaceholderCharacter

()

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

String

getValidCharacters

()

Returns the valid characters that can be input.

boolean

getValueContainsLiteralCharacters

()

Returns true if

stringToValue

should return literal
characters in the mask.

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

setInvalidCharacters

​(

String

invalidCharacters)

Allows for further restricting of the characters that can be input.

void

setMask

​(

String

mask)

Sets the mask dictating the legal characters.

void

setPlaceholder

​(

String

placeholder)

Sets the string to use if the value does not completely fill in
the mask.

void

setPlaceholderCharacter

​(char placeholder)

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in.

void

setValidCharacters

​(

String

validCharacters)

Allows for further restricting of the characters that can be input.

void

setValueContainsLiteralCharacters

​(boolean containsLiteralChars)

If true, the returned value and set value will also contain the literal
characters in mask.

Object

stringToValue

​(

String

value)

Parses the text, returning the appropriate Object representation of
the String

value

.

String

valueToString

​(

Object

value)

Returns a String representation of the Object

value

based on the mask.

- Methods declared in class javax.swing.text.

DefaultFormatter

clone

,

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

getActions

,

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

MaskFormatter

()

Creates a MaskFormatter with no mask.

MaskFormatter

​(

String

mask)

Creates a

MaskFormatter

with the specified mask.

---

#### Constructor Summary

Creates a MaskFormatter with no mask.

Creates a

MaskFormatter

with the specified mask.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getInvalidCharacters

()

Returns the characters that are not valid for input.

String

getMask

()

Returns the formatting mask.

String

getPlaceholder

()

Returns the String to use if the value does not completely fill
in the mask.

char

getPlaceholderCharacter

()

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

String

getValidCharacters

()

Returns the valid characters that can be input.

boolean

getValueContainsLiteralCharacters

()

Returns true if

stringToValue

should return literal
characters in the mask.

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

setInvalidCharacters

​(

String

invalidCharacters)

Allows for further restricting of the characters that can be input.

void

setMask

​(

String

mask)

Sets the mask dictating the legal characters.

void

setPlaceholder

​(

String

placeholder)

Sets the string to use if the value does not completely fill in
the mask.

void

setPlaceholderCharacter

​(char placeholder)

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in.

void

setValidCharacters

​(

String

validCharacters)

Allows for further restricting of the characters that can be input.

void

setValueContainsLiteralCharacters

​(boolean containsLiteralChars)

If true, the returned value and set value will also contain the literal
characters in mask.

Object

stringToValue

​(

String

value)

Parses the text, returning the appropriate Object representation of
the String

value

.

String

valueToString

​(

Object

value)

Returns a String representation of the Object

value

based on the mask.

- Methods declared in class javax.swing.text.

DefaultFormatter

clone

,

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

getActions

,

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

Returns the characters that are not valid for input.

Returns the formatting mask.

Returns the String to use if the value does not completely fill
in the mask.

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

Returns the valid characters that can be input.

Returns true if

stringToValue

should return literal
characters in the mask.

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.

Allows for further restricting of the characters that can be input.

Sets the mask dictating the legal characters.

Sets the string to use if the value does not completely fill in
the mask.

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in.

If true, the returned value and set value will also contain the literal
characters in mask.

Parses the text, returning the appropriate Object representation of
the String

value

.

Returns a String representation of the Object

value

based on the mask.

Methods declared in class javax.swing.text.

DefaultFormatter

clone

,

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

getActions

,

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

- MaskFormatter

```java
public MaskFormatter()
```

Creates a MaskFormatter with no mask.

- MaskFormatter

```java
public MaskFormatter​(
String
mask)
throws
ParseException
```

Creates a

MaskFormatter

with the specified mask.
A

ParseException

will be thrown if

mask

is an invalid mask.

**Parameters:** mask

- the mask
**Throws:** ParseException

- if mask does not contain valid mask characters

============ METHOD DETAIL ==========

- Method Detail

- setMask

```java
public void setMask​(
String
mask)
throws
ParseException
```

Sets the mask dictating the legal characters.
This will throw a

ParseException

if

mask

is
not valid.

**Parameters:** mask

- the mask
**Throws:** ParseException

- if mask does not contain valid mask characters

- getMask

```java
public
String
getMask()
```

Returns the formatting mask.

**Returns:** Mask dictating legal character values.

- setValidCharacters

```java
public void setValidCharacters​(
String
validCharacters)
```

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the invalid characters.

**Parameters:** validCharacters

- If non-null, specifies legal characters.

- getValidCharacters

```java
public
String
getValidCharacters()
```

Returns the valid characters that can be input.

**Returns:** Legal characters

- setInvalidCharacters

```java
public void setInvalidCharacters​(
String
invalidCharacters)
```

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the valid characters.

**Parameters:** invalidCharacters

- If non-null, specifies illegal characters.

- getInvalidCharacters

```java
public
String
getInvalidCharacters()
```

Returns the characters that are not valid for input.

**Returns:** illegal characters.

- setPlaceholder

```java
public void setPlaceholder​(
String
placeholder)
```

Sets the string to use if the value does not completely fill in
the mask. A null value implies the placeholder char should be used.

**Parameters:** placeholder

- String used when formatting if the value does not
completely fill the mask

- getPlaceholder

```java
public
String
getPlaceholder()
```

Returns the String to use if the value does not completely fill
in the mask.

**Returns:** String used when formatting if the value does not
completely fill the mask

- setPlaceholderCharacter

```java
public void setPlaceholderCharacter​(char placeholder)
```

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in. The default value is
a space.

This is only applicable if the placeholder string has not been
specified, or does not completely fill in the mask.

**Parameters:** placeholder

- Character used when formatting if the value does not
completely fill the mask

- getPlaceholderCharacter

```java
public char getPlaceholderCharacter()
```

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

**Returns:** Character used when formatting if the value does not
completely fill the mask

- setValueContainsLiteralCharacters

```java
public void setValueContainsLiteralCharacters​(boolean containsLiteralChars)
```

If true, the returned value and set value will also contain the literal
characters in mask.

For example, if the mask is

'(###) ###-####'

, the
current value is

'(415) 555-1212'

, and

valueContainsLiteralCharacters

is
true

stringToValue

will return

'(415) 555-1212'

. On the other hand, if

valueContainsLiteralCharacters

is false,

stringToValue

will return

'4155551212'

.

**Parameters:** containsLiteralChars

- Used to indicate if literal characters in
mask should be returned in stringToValue

- getValueContainsLiteralCharacters

```java
public boolean getValueContainsLiteralCharacters()
```

Returns true if

stringToValue

should return literal
characters in the mask.

**Returns:** True if literal characters in mask should be returned in
stringToValue

- stringToValue

```java
public
Object
stringToValue​(
String
value)
throws
ParseException
```

Parses the text, returning the appropriate Object representation of
the String

value

. This strips the literal characters as
necessary and invokes supers

stringToValue

, so that if
you have specified a value class (

setValueClass

) an
instance of it will be created. This will throw a

ParseException

if the value does not match the current
mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

**Overrides:** stringToValue

in class

DefaultFormatter
**Parameters:** value

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion
**See Also:** setValueContainsLiteralCharacters(boolean)

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

based on the mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

**Overrides:** valueToString

in class

DefaultFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion
**See Also:** setValueContainsLiteralCharacters(boolean)

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

Constructor Detail

- MaskFormatter

```java
public MaskFormatter()
```

Creates a MaskFormatter with no mask.

- MaskFormatter

```java
public MaskFormatter​(
String
mask)
throws
ParseException
```

Creates a

MaskFormatter

with the specified mask.
A

ParseException

will be thrown if

mask

is an invalid mask.

**Parameters:** mask

- the mask
**Throws:** ParseException

- if mask does not contain valid mask characters

---

#### Constructor Detail

MaskFormatter

```java
public MaskFormatter()
```

Creates a MaskFormatter with no mask.

---

#### MaskFormatter

public MaskFormatter()

Creates a MaskFormatter with no mask.

MaskFormatter

```java
public MaskFormatter​(
String
mask)
throws
ParseException
```

Creates a

MaskFormatter

with the specified mask.
A

ParseException

will be thrown if

mask

is an invalid mask.

**Parameters:** mask

- the mask
**Throws:** ParseException

- if mask does not contain valid mask characters

---

#### MaskFormatter

public MaskFormatter​(

String

mask)
throws

ParseException

Creates a

MaskFormatter

with the specified mask.
A

ParseException

will be thrown if

mask

is an invalid mask.

Method Detail

- setMask

```java
public void setMask​(
String
mask)
throws
ParseException
```

Sets the mask dictating the legal characters.
This will throw a

ParseException

if

mask

is
not valid.

**Parameters:** mask

- the mask
**Throws:** ParseException

- if mask does not contain valid mask characters

- getMask

```java
public
String
getMask()
```

Returns the formatting mask.

**Returns:** Mask dictating legal character values.

- setValidCharacters

```java
public void setValidCharacters​(
String
validCharacters)
```

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the invalid characters.

**Parameters:** validCharacters

- If non-null, specifies legal characters.

- getValidCharacters

```java
public
String
getValidCharacters()
```

Returns the valid characters that can be input.

**Returns:** Legal characters

- setInvalidCharacters

```java
public void setInvalidCharacters​(
String
invalidCharacters)
```

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the valid characters.

**Parameters:** invalidCharacters

- If non-null, specifies illegal characters.

- getInvalidCharacters

```java
public
String
getInvalidCharacters()
```

Returns the characters that are not valid for input.

**Returns:** illegal characters.

- setPlaceholder

```java
public void setPlaceholder​(
String
placeholder)
```

Sets the string to use if the value does not completely fill in
the mask. A null value implies the placeholder char should be used.

**Parameters:** placeholder

- String used when formatting if the value does not
completely fill the mask

- getPlaceholder

```java
public
String
getPlaceholder()
```

Returns the String to use if the value does not completely fill
in the mask.

**Returns:** String used when formatting if the value does not
completely fill the mask

- setPlaceholderCharacter

```java
public void setPlaceholderCharacter​(char placeholder)
```

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in. The default value is
a space.

This is only applicable if the placeholder string has not been
specified, or does not completely fill in the mask.

**Parameters:** placeholder

- Character used when formatting if the value does not
completely fill the mask

- getPlaceholderCharacter

```java
public char getPlaceholderCharacter()
```

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

**Returns:** Character used when formatting if the value does not
completely fill the mask

- setValueContainsLiteralCharacters

```java
public void setValueContainsLiteralCharacters​(boolean containsLiteralChars)
```

If true, the returned value and set value will also contain the literal
characters in mask.

For example, if the mask is

'(###) ###-####'

, the
current value is

'(415) 555-1212'

, and

valueContainsLiteralCharacters

is
true

stringToValue

will return

'(415) 555-1212'

. On the other hand, if

valueContainsLiteralCharacters

is false,

stringToValue

will return

'4155551212'

.

**Parameters:** containsLiteralChars

- Used to indicate if literal characters in
mask should be returned in stringToValue

- getValueContainsLiteralCharacters

```java
public boolean getValueContainsLiteralCharacters()
```

Returns true if

stringToValue

should return literal
characters in the mask.

**Returns:** True if literal characters in mask should be returned in
stringToValue

- stringToValue

```java
public
Object
stringToValue​(
String
value)
throws
ParseException
```

Parses the text, returning the appropriate Object representation of
the String

value

. This strips the literal characters as
necessary and invokes supers

stringToValue

, so that if
you have specified a value class (

setValueClass

) an
instance of it will be created. This will throw a

ParseException

if the value does not match the current
mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

**Overrides:** stringToValue

in class

DefaultFormatter
**Parameters:** value

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion
**See Also:** setValueContainsLiteralCharacters(boolean)

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

based on the mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

**Overrides:** valueToString

in class

DefaultFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion
**See Also:** setValueContainsLiteralCharacters(boolean)

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

---

#### Method Detail

setMask

```java
public void setMask​(
String
mask)
throws
ParseException
```

Sets the mask dictating the legal characters.
This will throw a

ParseException

if

mask

is
not valid.

**Parameters:** mask

- the mask
**Throws:** ParseException

- if mask does not contain valid mask characters

---

#### setMask

public void setMask​(

String

mask)
throws

ParseException

Sets the mask dictating the legal characters.
This will throw a

ParseException

if

mask

is
not valid.

getMask

```java
public
String
getMask()
```

Returns the formatting mask.

**Returns:** Mask dictating legal character values.

---

#### getMask

public

String

getMask()

Returns the formatting mask.

setValidCharacters

```java
public void setValidCharacters​(
String
validCharacters)
```

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the invalid characters.

**Parameters:** validCharacters

- If non-null, specifies legal characters.

---

#### setValidCharacters

public void setValidCharacters​(

String

validCharacters)

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the invalid characters.

getValidCharacters

```java
public
String
getValidCharacters()
```

Returns the valid characters that can be input.

**Returns:** Legal characters

---

#### getValidCharacters

public

String

getValidCharacters()

Returns the valid characters that can be input.

setInvalidCharacters

```java
public void setInvalidCharacters​(
String
invalidCharacters)
```

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the valid characters.

**Parameters:** invalidCharacters

- If non-null, specifies illegal characters.

---

#### setInvalidCharacters

public void setInvalidCharacters​(

String

invalidCharacters)

Allows for further restricting of the characters that can be input.
Only characters specified in the mask, not in the

invalidCharacters

, and in

validCharacters

will be allowed to be input. Passing
in null (the default) implies the valid characters are only bound
by the mask and the valid characters.

getInvalidCharacters

```java
public
String
getInvalidCharacters()
```

Returns the characters that are not valid for input.

**Returns:** illegal characters.

---

#### getInvalidCharacters

public

String

getInvalidCharacters()

Returns the characters that are not valid for input.

setPlaceholder

```java
public void setPlaceholder​(
String
placeholder)
```

Sets the string to use if the value does not completely fill in
the mask. A null value implies the placeholder char should be used.

**Parameters:** placeholder

- String used when formatting if the value does not
completely fill the mask

---

#### setPlaceholder

public void setPlaceholder​(

String

placeholder)

Sets the string to use if the value does not completely fill in
the mask. A null value implies the placeholder char should be used.

getPlaceholder

```java
public
String
getPlaceholder()
```

Returns the String to use if the value does not completely fill
in the mask.

**Returns:** String used when formatting if the value does not
completely fill the mask

---

#### getPlaceholder

public

String

getPlaceholder()

Returns the String to use if the value does not completely fill
in the mask.

setPlaceholderCharacter

```java
public void setPlaceholderCharacter​(char placeholder)
```

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in. The default value is
a space.

This is only applicable if the placeholder string has not been
specified, or does not completely fill in the mask.

**Parameters:** placeholder

- Character used when formatting if the value does not
completely fill the mask

---

#### setPlaceholderCharacter

public void setPlaceholderCharacter​(char placeholder)

Sets the character to use in place of characters that are not present
in the value, ie the user must fill them in. The default value is
a space.

This is only applicable if the placeholder string has not been
specified, or does not completely fill in the mask.

This is only applicable if the placeholder string has not been
specified, or does not completely fill in the mask.

getPlaceholderCharacter

```java
public char getPlaceholderCharacter()
```

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

**Returns:** Character used when formatting if the value does not
completely fill the mask

---

#### getPlaceholderCharacter

public char getPlaceholderCharacter()

Returns the character to use in place of characters that are not present
in the value, ie the user must fill them in.

setValueContainsLiteralCharacters

```java
public void setValueContainsLiteralCharacters​(boolean containsLiteralChars)
```

If true, the returned value and set value will also contain the literal
characters in mask.

For example, if the mask is

'(###) ###-####'

, the
current value is

'(415) 555-1212'

, and

valueContainsLiteralCharacters

is
true

stringToValue

will return

'(415) 555-1212'

. On the other hand, if

valueContainsLiteralCharacters

is false,

stringToValue

will return

'4155551212'

.

**Parameters:** containsLiteralChars

- Used to indicate if literal characters in
mask should be returned in stringToValue

---

#### setValueContainsLiteralCharacters

public void setValueContainsLiteralCharacters​(boolean containsLiteralChars)

If true, the returned value and set value will also contain the literal
characters in mask.

For example, if the mask is

'(###) ###-####'

, the
current value is

'(415) 555-1212'

, and

valueContainsLiteralCharacters

is
true

stringToValue

will return

'(415) 555-1212'

. On the other hand, if

valueContainsLiteralCharacters

is false,

stringToValue

will return

'4155551212'

.

For example, if the mask is

'(###) ###-####'

, the
current value is

'(415) 555-1212'

, and

valueContainsLiteralCharacters

is
true

stringToValue

will return

'(415) 555-1212'

. On the other hand, if

valueContainsLiteralCharacters

is false,

stringToValue

will return

'4155551212'

.

getValueContainsLiteralCharacters

```java
public boolean getValueContainsLiteralCharacters()
```

Returns true if

stringToValue

should return literal
characters in the mask.

**Returns:** True if literal characters in mask should be returned in
stringToValue

---

#### getValueContainsLiteralCharacters

public boolean getValueContainsLiteralCharacters()

Returns true if

stringToValue

should return literal
characters in the mask.

stringToValue

```java
public
Object
stringToValue​(
String
value)
throws
ParseException
```

Parses the text, returning the appropriate Object representation of
the String

value

. This strips the literal characters as
necessary and invokes supers

stringToValue

, so that if
you have specified a value class (

setValueClass

) an
instance of it will be created. This will throw a

ParseException

if the value does not match the current
mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

**Overrides:** stringToValue

in class

DefaultFormatter
**Parameters:** value

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion
**See Also:** setValueContainsLiteralCharacters(boolean)

---

#### stringToValue

public

Object

stringToValue​(

String

value)
throws

ParseException

Parses the text, returning the appropriate Object representation of
the String

value

. This strips the literal characters as
necessary and invokes supers

stringToValue

, so that if
you have specified a value class (

setValueClass

) an
instance of it will be created. This will throw a

ParseException

if the value does not match the current
mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

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

based on the mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

**Overrides:** valueToString

in class

DefaultFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion
**See Also:** setValueContainsLiteralCharacters(boolean)

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

based on the mask. Refer to

setValueContainsLiteralCharacters(boolean)

for details
on how literals are treated.

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

---

