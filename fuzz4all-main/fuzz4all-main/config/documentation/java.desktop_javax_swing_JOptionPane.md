# Class JOptionPane

**Source:** `java.desktop\javax\swing\JOptionPane.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component which implements standard dialog box controls.")
public class
JOptionPane

extends
JComponent

implements
Accessible
```

JOptionPane

makes it easy to pop up a standard dialog box that
prompts users for a value or informs them of something.
For information about using

JOptionPane

, see

How to Make Dialogs

,
a section in

The Java Tutorial

.

While the

JOptionPane

class may appear complex because of the large number of methods, almost
all uses of this class are one-line calls to one of the static

showXxxDialog

methods shown below:

Common JOptionPane method names and their descriptions

Method Name

Description

showConfirmDialog

Asks a confirming question, like yes/no/cancel.

showInputDialog

Prompt for some input.

showMessageDialog

Tell the user about something that has happened.

showOptionDialog

The Grand Unification of the above three.

Each of these methods also comes in a

showInternalXXX

flavor, which uses an internal frame to hold the dialog box (see

JInternalFrame

).
Multiple convenience methods have also been defined -- overloaded
versions of the basic methods that use different parameter lists.

All dialogs are modal. Each

showXxxDialog

method blocks
the caller until the user's interaction is complete.

Common dialog

icon

message

input value

option buttons

The basic appearance of one of these dialog boxes is generally
similar to the picture above, although the various
look-and-feels are
ultimately responsible for the final result. In particular, the
look-and-feels will adjust the layout to accommodate the option pane's

ComponentOrientation

property.

Parameters:

The parameters to these methods follow consistent patterns:

When the selection is changed,

setValue

is invoked,
which generates a

PropertyChangeEvent

.

If a

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final
Object
UNINITIALIZED_VALUE

Indicates that the user has not yet selected a value.

---

#### public static final int DEFAULT_OPTION

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

**See Also:**
- Constant Field Values

---

#### public static final int YES_NO_OPTION

Type used for

showConfirmDialog

.

**See Also:**
- Constant Field Values

---

#### public static final int YES_NO_CANCEL_OPTION

Type used for

showConfirmDialog

.

**See Also:**
- Constant Field Values

---

#### public static final int OK_CANCEL_OPTION

Type used for

showConfirmDialog

.

**See Also:**
- Constant Field Values

---

#### public static final int YES_OPTION

Return value from class method if YES is chosen.

**See Also:**
- Constant Field Values

---

#### public static final int NO_OPTION

Return value from class method if NO is chosen.

**See Also:**
- Constant Field Values

---

#### public static final int CANCEL_OPTION

Return value from class method if CANCEL is chosen.

**See Also:**
- Constant Field Values

---

#### public static final int OK_OPTION

Return value form class method if OK is chosen.

**See Also:**
- Constant Field Values

---

#### public static final int CLOSED_OPTION

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

**See Also:**
- Constant Field Values

---

#### public static final int ERROR_MESSAGE

Used for error messages.

**See Also:**
- Constant Field Values

---

#### public static final int INFORMATION_MESSAGE

Used for information messages.

**See Also:**
- Constant Field Values

---

#### public static final int WARNING_MESSAGE

Used for warning messages.

**See Also:**
- Constant Field Values

---

#### public static final int QUESTION_MESSAGE

Used for questions.

**See Also:**
- Constant Field Values

---

#### public static final int PLAIN_MESSAGE

No icon is used.

**See Also:**
- Constant Field Values

---

#### public static final
String
ICON_PROPERTY

Bound property name for

icon

.

**See Also:**
- Constant Field Values

---

#### public static final
String
MESSAGE_PROPERTY

Bound property name for

message

.

**See Also:**
- Constant Field Values

---

#### public static final
String
VALUE_PROPERTY

Bound property name for

value

.

**See Also:**
- Constant Field Values

---

#### public static final
String
OPTIONS_PROPERTY

Bound property name for

option

.

**See Also:**
- Constant Field Values

---

#### public static final
String
INITIAL_VALUE_PROPERTY

Bound property name for

initialValue

.

**See Also:**
- Constant Field Values

---

#### public static final
String
MESSAGE_TYPE_PROPERTY

Bound property name for

type

.

**See Also:**
- Constant Field Values

---

#### public static final
String
OPTION_TYPE_PROPERTY

Bound property name for

optionType

.

**See Also:**
- Constant Field Values

---

#### public static final
String
SELECTION_VALUES_PROPERTY

Bound property name for

selectionValues

.

**See Also:**
- Constant Field Values

---

#### public static final
String
INITIAL_SELECTION_VALUE_PROPERTY

Bound property name for

initialSelectionValue

.

**See Also:**
- Constant Field Values

---

#### public static final
String
INPUT_VALUE_PROPERTY

Bound property name for

inputValue

.

**See Also:**
- Constant Field Values

---

#### public static final
String
WANTS_INPUT_PROPERTY

Bound property name for

wantsInput

.

**See Also:**
- Constant Field Values

---

#### protected transient
Icon
icon

Icon used in pane.

---

#### protected transient
Object
message

Message to display.

---

#### protected transient
Object
[] options

Options to display to the user.

---

#### protected transient
Object
initialValue

Value that should be initially selected in

options

.

---

#### protected int messageType

Message type.

---

#### protected int optionType

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

---

#### protected transient
Object
value

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

---

#### protected transient
Object
[] selectionValues

Array of values the user can choose from. Look and feel will
provide the UI component to choose this from.

---

#### protected transient
Object
inputValue

Value the user has input.

---

#### protected transient
Object
initialSelectionValue

Initial value to select in

selectionValues

.

---

#### protected boolean wantsInput

If true, a UI widget will be provided to the user to get input.

---

### Constructor Details

#### public JOptionPane()

Creates a

JOptionPane

with a test message.

---

#### public JOptionPane​(
Object
message)

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

**Parameters:**
- message

- the

Object

to display

---

#### public JOptionPane​(
Object
message,
int messageType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

**Parameters:**
- message

- the

Object

to display
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

---

#### public JOptionPane​(
Object
message,
int messageType,
int optionType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

**Parameters:**
- message

- the

Object

to display
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION

---

#### public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon)

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

**Parameters:**
- message

- the

Object

to display
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
- icon

- the

Icon

image to display

---

#### public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.
None of the options is initially selected.

The options objects should contain either instances of

Component

s, (which are added directly) or

Strings

(which are wrapped in a

JButton

).
If you provide

Component

s, you must ensure that when the

Component

is clicked it messages

setValue

in the created

JOptionPane

.

**Parameters:**
- message

- the

Object

to display
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
- icon

- the

Icon

image to display
- options

- the choices the user can select

---

#### public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options,

Object
initialValue)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

**Parameters:**
- message

- the

Object

to display
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
- icon

- the Icon image to display
- options

- the choices the user can select
- initialValue

- the choice that is initially selected; if

null

, then nothing will be initially selected;
only meaningful if

options

is used

---

### Method Details

#### public static
String
showInputDialog​(
Object
message)
throws
HeadlessException

Shows a question-message dialog requesting input from the user. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:**
- message

- the

Object

to display

**Returns:**
- user's input

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static
String
showInputDialog​(
Object
message,

Object
initialSelectionValue)

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:**
- message

- the

Object

to display
- initialSelectionValue

- the value used to initialize the input
field

**Returns:**
- user's input

**Since:**
- 1.4

---

#### public static
String
showInputDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:**
- parentComponent

- the parent

Component

for the
dialog
- message

- the

Object

to display

**Returns:**
- user's input

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

Object
initialSelectionValue)

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

. The input value will be
initialized to

initialSelectionValue

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:**
- parentComponent

- the parent

Component

for the
dialog
- message

- the

Object

to display
- initialSelectionValue

- the value used to initialize the input
field

**Returns:**
- user's input

**Since:**
- 1.4

---

#### public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:**
- parentComponent

- the parent

Component

for the
dialog
- message

- the

Object

to display
- title

- the

String

to display in the dialog
title bar
- messageType

- the type of message that is to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

**Returns:**
- user's input

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static
Object
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)
throws
HeadlessException

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified. The user will able to choose from

selectionValues

, where

null

implies the
user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:**
- parentComponent

- the parent

Component

for the
dialog
- message

- the

Object

to display
- title

- the

String

to display in the
dialog title bar
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- icon

- the

Icon

image to display
- selectionValues

- an array of

Object

s that
gives the possible selections
- initialSelectionValue

- the value used to initialize the input
field

**Returns:**
- user's input, or

null

meaning the user
canceled the input

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static void showMessageDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException

Brings up an information-message dialog titled "Message".

**Parameters:**
- parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the

Object

to display

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the

Object

to display
- title

- the title string for the dialog
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)
throws
HeadlessException

Brings up a dialog displaying a message, specifying all parameters.

**Parameters:**
- parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
- message

- the

Object

to display
- title

- the title string for the dialog
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static int showConfirmDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

**Parameters:**
- parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
- message

- the

Object

to display

**Returns:**
- an integer indicating the option selected by the user

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)
throws
HeadlessException

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

**Parameters:**
- parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
- message

- the

Object

to display
- title

- the title string for the dialog
- optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION

**Returns:**
- an int indicating the option selected by the user

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)
throws
HeadlessException

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:**
- parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used.
- message

- the

Object

to display
- title

- the title string for the dialog
- optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
- messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

**Returns:**
- an integer indicating the option selected by the user

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)
throws
HeadlessException

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:**
- parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
- message

- the Object to display
- title

- the title string for the dialog
- optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
- messageType

- an int designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- icon

- the icon to display in the dialog

**Returns:**
- an int indicating the option selected by the user

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public static int showOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)
throws
HeadlessException

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are
supplied by the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

, or if the

parentComponent

has no

Frame

, a
default

Frame

is used
- message

- the

Object

to display
- title

- the title string for the dialog
- optionType

- an integer designating the options available on the
dialog:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
- messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- icon

- the icon to display in the dialog
- options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are
rendered using their

toString

methods;
if this parameter is

null

,
the options are determined by the Look and Feel
- initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null

**Returns:**
- an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed
the dialog

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public
JDialog
createDialog​(
Component
parentComponent,

String
title)
throws
HeadlessException

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

title

is the title of the returned dialog.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:**
- parentComponent

- determines the frame in which the dialog
is displayed; if the

parentComponent

has
no

Frame

, a default

Frame

is used
- title

- the title string for the dialog

**Returns:**
- a new

JDialog

containing this instance

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public
JDialog
createDialog​(
String
title)
throws
HeadlessException

Creates and returns a new parentless

JDialog

with the specified title.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:**
- title

- the title string for the dialog

**Returns:**
- a new

JDialog

containing this instance

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.6

---

#### public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message)

Brings up an internal confirmation dialog panel. The dialog
is a information-message dialog titled "Message".

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the object to display

---

#### public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the

Object

to display
- title

- the title string for the dialog
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

---

#### public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)

Brings up an internal dialog panel displaying a message,
specifying all parameters.

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the

Object

to display
- title

- the title string for the dialog
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed

---

#### public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message)

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

**Parameters:**
- parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the

Object

to display

**Returns:**
- an integer indicating the option selected by the user

---

#### public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects
are converted to a

String

using the

toString

method
- title

- the title string for the dialog
- optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION

**Returns:**
- an integer indicating the option selected by the user

---

#### public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:**
- parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
- title

- the title string for the dialog
- optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION
- messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

**Returns:**
- an integer indicating the option selected by the user

---

#### public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the parentComponent has no Frame, a
default

Frame

is used
- message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
- title

- the title string for the dialog
- optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

.
- messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- icon

- the icon to display in the dialog

**Returns:**
- an integer indicating the option selected by the user

---

#### public static int showInternalOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are supplied by the Look and Feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:**
- parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
- message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string. Other objects are
converted to a

String

using the

toString

method
- title

- the title string for the dialog
- optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION
- messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
- icon

- the icon to display in the dialog
- options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are rendered using their

toString

methods; if this parameter is

null

,
the options are determined by the Look and Feel
- initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null

**Returns:**
- an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed the Dialog

---

#### public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message)

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

. The dialog
is displayed in the

Component

's frame,
and is usually positioned below the

Component

.

**Parameters:**
- parentComponent

- the parent

Component

for the dialog
- message

- the

Object

to display

**Returns:**
- user's input

---

#### public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:**
- parentComponent

- the parent

Component

for the dialog
- message

- the

Object

to display
- title

- the

String

to display in the
dialog title bar
- messageType

- the type of message that is to be displayed:
ERROR_MESSAGE, INFORMATION_MESSAGE, WARNING_MESSAGE,
QUESTION_MESSAGE, or PLAIN_MESSAGE

**Returns:**
- user's input

---

#### public static
Object
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified. The user will able to choose from

selectionValues

, where

null

implies the user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:**
- parentComponent

- the parent

Component

for the dialog
- message

- the

Object

to display
- title

- the

String

to display in the dialog
title bar
- messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE
- icon

- the

Icon

image to display
- selectionValues

- an array of

Objects

that
gives the possible selections
- initialSelectionValue

- the value used to initialize the input
field

**Returns:**
- user's input, or

null

meaning the user
canceled the input

---

#### public
JInternalFrame
createInternalFrame​(
Component
parentComponent,

String
title)

Creates and returns an instance of

JInternalFrame

.
The internal frame is created with the specified title,
and wrapping the

JOptionPane

.
The returned

JInternalFrame

is
added to the

JDesktopPane

ancestor of

parentComponent

, or components
parent if one its ancestors isn't a

JDesktopPane

,
or if

parentComponent

doesn't have a parent then a

RuntimeException

is thrown.

**Parameters:**
- parentComponent

- the parent

Component

for
the internal frame
- title

- the

String

to display in the
frame's title bar

**Returns:**
- a

JInternalFrame

containing a

JOptionPane

**Throws:**
- RuntimeException

- if

parentComponent

does
not have a valid parent

---

#### public static
Frame
getFrameForComponent​(
Component
parentComponent)
throws
HeadlessException

Returns the specified component's

Frame

.

**Parameters:**
- parentComponent

- the

Component

to check for a

Frame

**Returns:**
- the

Frame

that contains the component,
or

getRootFrame

if the component is

null

,
or does not have a valid

Frame

parent

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- getRootFrame()

,

GraphicsEnvironment.isHeadless()

---

#### public static
JDesktopPane
getDesktopPaneForComponent​(
Component
parentComponent)

Returns the specified component's desktop pane.

**Parameters:**
- parentComponent

- the

Component

to check for a
desktop

**Returns:**
- the

JDesktopPane

that contains the component,
or

null

if the component is

null

or does not have an ancestor that is a

JInternalFrame

---

#### public static void setRootFrame​(
Frame
newRootFrame)

Sets the frame to use for class methods in which a frame is
not provided.

Note:

It is recommended that rather than using this method you supply a valid parent.

**Parameters:**
- newRootFrame

- the default

Frame

to use

---

#### public static
Frame
getRootFrame()
throws
HeadlessException

Returns the

Frame

to use for the class methods in
which a frame is not provided.

**Returns:**
- the default

Frame

to use

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**See Also:**
- setRootFrame(java.awt.Frame)

,

GraphicsEnvironment.isHeadless()

---

#### @BeanProperty
(
hidden
=true,

description
="The UI object that implements the optionpane\'s LookAndFeel")
public void setUI​(
OptionPaneUI
ui)

Sets the UI object which implements the L&F for this component.

**Parameters:**
- ui

- the

OptionPaneUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### public
OptionPaneUI
getUI()

Returns the UI object which implements the L&F for this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

OptionPaneUI

object

---

#### public void updateUI()

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.updateUI()

---

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "OptionPaneUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
preferred
=true,

description
="The optionpane\'s message object.")
public void setMessage​(
Object
newMessage)

Sets the option pane's message-object.

**Parameters:**
- newMessage

- the

Object

to display

**See Also:**
- getMessage()

---

#### public
Object
getMessage()

Returns the message-object this pane displays.

**Returns:**
- the

Object

that is displayed

**See Also:**
- setMessage(java.lang.Object)

---

#### @BeanProperty
(
preferred
=true,

description
="The option pane\'s type icon.")
public void setIcon​(
Icon
newIcon)

Sets the icon to display. If non-

null

, the look and feel
does not provide an icon.

**Parameters:**
- newIcon

- the

Icon

to display

**See Also:**
- getIcon()

---

#### public
Icon
getIcon()

Returns the icon this pane displays.

**Returns:**
- the

Icon

that is displayed

**See Also:**
- setIcon(javax.swing.Icon)

---

#### @BeanProperty
(
preferred
=true,

description
="The option pane\'s value object.")
public void setValue​(
Object
newValue)

Sets the value the user has chosen.

**Parameters:**
- newValue

- the chosen value

**See Also:**
- getValue()

---

#### public
Object
getValue()

Returns the value the user has selected.

UNINITIALIZED_VALUE

implies the user has not yet made a choice,

null

means the
user closed the window with out choosing anything. Otherwise
the returned value will be one of the options defined in this
object.

**Returns:**
- the

Object

chosen by the user,

UNINITIALIZED_VALUE

if the user has not yet made a choice, or

null

if
the user closed the window without making a choice

**See Also:**
- setValue(java.lang.Object)

---

#### @BeanProperty
(
description
="The option pane\'s options objects.")
public void setOptions​(
Object
[] newOptions)

Sets the options this pane displays. If an element in

newOptions

is a

Component

it is added directly to the pane,
otherwise a button is created for the element.

**Parameters:**
- newOptions

- an array of

Objects

that create the
buttons the user can click on, or arbitrary

Components

to add to the pane

**See Also:**
- getOptions()

---

#### public
Object
[] getOptions()

Returns the choices the user can make.

**Returns:**
- the array of

Objects

that give the user's choices

**See Also:**
- setOptions(java.lang.Object[])

---

#### @BeanProperty
(
preferred
=true,

description
="The option pane\'s initial value object.")
public void setInitialValue​(
Object
newInitialValue)

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

**Parameters:**
- newInitialValue

- the

Object

that gets the initial
keyboard focus

**See Also:**
- getInitialValue()

---

#### public
Object
getInitialValue()

Returns the initial value.

**Returns:**
- the

Object

that gets the initial keyboard focus

**See Also:**
- setInitialValue(java.lang.Object)

---

#### @BeanProperty
(
preferred
=true,

description
="The option pane\'s message type.")
public void setMessageType​(int newType)

Sets the option pane's message type.
The message type is used by the Look and Feel to determine the
icon to display (if not supplied) as well as potentially how to
lay out the

parentComponent

.

**Parameters:**
- newType

- an integer specifying the kind of message to display:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE

**Throws:**
- RuntimeException

- if

newType

is not one of the
legal values listed above

**See Also:**
- getMessageType()

---

#### public int getMessageType()

Returns the message type.

**Returns:**
- an integer specifying the message type

**See Also:**
- setMessageType(int)

---

#### @BeanProperty
(
preferred
=true,

description
="The option pane\'s option type.")
public void setOptionType​(int newType)

Sets the options to display.
The option type is used by the Look and Feel to
determine what buttons to show (unless options are supplied).

**Parameters:**
- newType

- an integer specifying the options the L&F is to display:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION

**Throws:**
- RuntimeException

- if

newType

is not one of
the legal values listed above

**See Also:**
- getOptionType()

,

setOptions(java.lang.Object[])

---

#### public int getOptionType()

Returns the type of options that are displayed.

**Returns:**
- an integer specifying the user-selectable options

**See Also:**
- setOptionType(int)

---

#### @BeanProperty
(
description
="The option pane\'s selection values.")
public void setSelectionValues​(
Object
[] newValues)

Sets the input selection values for a pane that provides the user
with a list of items to choose from. (The UI provides a widget
for choosing one of the values.) A

null

value
implies the user can input whatever they wish, usually by means
of a

JTextField

.

Sets

wantsInput

to true. Use

setInitialSelectionValue

to specify the initially-chosen
value. After the pane as been enabled,

inputValue

is
set to the value the user has selected.

**Parameters:**
- newValues

- an array of

Objects

the user to be
displayed
(usually in a list or combo-box) from which
the user can make a selection

**See Also:**
- setWantsInput(boolean)

,

setInitialSelectionValue(java.lang.Object)

,

getSelectionValues()

---

#### public
Object
[] getSelectionValues()

Returns the input selection values.

**Returns:**
- the array of

Objects

the user can select

**See Also:**
- setSelectionValues(java.lang.Object[])

---

#### @BeanProperty
(
description
="The option pane\'s initial selection value object.")
public void setInitialSelectionValue​(
Object
newValue)

Sets the input value that is initially displayed as selected to the user.
Only used if

wantsInput

is true.

**Parameters:**
- newValue

- the initially selected value

**See Also:**
- setSelectionValues(java.lang.Object[])

,

getInitialSelectionValue()

---

#### public
Object
getInitialSelectionValue()

Returns the input value that is displayed as initially selected to the user.

**Returns:**
- the initially selected value

**See Also:**
- setInitialSelectionValue(java.lang.Object)

,

setSelectionValues(java.lang.Object[])

---

#### @BeanProperty
(
preferred
=true,

description
="The option pane\'s input value object.")
public void setInputValue​(
Object
newValue)

Sets the input value that was selected or input by the user.
Only used if

wantsInput

is true. Note that this method
is invoked internally by the option pane (in response to user action)
and should generally not be called by client programs. To set the
input value initially displayed as selected to the user, use

setInitialSelectionValue

.

**Parameters:**
- newValue

- the

Object

used to set the
value that the user specified (usually in a text field)

**See Also:**
- setSelectionValues(java.lang.Object[])

,

setInitialSelectionValue(java.lang.Object)

,

setWantsInput(boolean)

,

getInputValue()

---

#### public
Object
getInputValue()

Returns the value the user has input, if

wantsInput

is true.

**Returns:**
- the

Object

the user specified,
if it was one of the objects, or a

String

if it was a value typed into a
field

**See Also:**
- setSelectionValues(java.lang.Object[])

,

setWantsInput(boolean)

,

setInputValue(java.lang.Object)

---

#### @BeanProperty
(
bound
=false)
public int getMaxCharactersPerLineCount()

Returns the maximum number of characters to place on a line in a
message. Default is to return

Integer.MAX_VALUE

.
The value can be
changed by overriding this method in a subclass.

**Returns:**
- an integer giving the maximum number of characters on a line

---

#### @BeanProperty
(
preferred
=true,

description
="Flag which allows the user to input a value.")
public void setWantsInput​(boolean newValue)

Sets the

wantsInput

property.
If

newValue

is true, an input component
(such as a text field or combo box) whose parent is

parentComponent

is provided to
allow the user to input a value. If

getSelectionValues

returns a non-

null

array, the input value is one of the
objects in that array. Otherwise the input value is whatever
the user inputs.

This is a bound property.

**Parameters:**
- newValue

- if true, an input component whose parent is

parentComponent

is provided to allow the user to input a value.

**See Also:**
- setSelectionValues(java.lang.Object[])

,

setInputValue(java.lang.Object)

---

#### public boolean getWantsInput()

Returns the value of the

wantsInput

property.

**Returns:**
- true if an input component will be provided

**See Also:**
- setWantsInput(boolean)

---

#### public void selectInitialValue()

Requests that the initial value be selected, which will set
focus to the initial value. This method
should be invoked after the window containing the option pane
is made visible.

---

#### protected
String
paramString()

Returns a string representation of this

JOptionPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this

JOptionPane

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this option pane")
public
AccessibleContext
getAccessibleContext()

Returns the

AccessibleContext

associated with this JOptionPane.
For option panes, the

AccessibleContext

takes the form of an

AccessibleJOptionPane

.
A new

AccessibleJOptionPane

instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJOptionPane that serves as the
AccessibleContext of this AccessibleJOptionPane

---

### Additional Sections

#### Class JOptionPane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JOptionPane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JOptionPane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JOptionPane

javax.swing.JComponent

- javax.swing.JOptionPane

javax.swing.JOptionPane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component which implements standard dialog box controls.")
public class
JOptionPane

extends
JComponent

implements
Accessible
```

JOptionPane

makes it easy to pop up a standard dialog box that
prompts users for a value or informs them of something.
For information about using

JOptionPane

, see

How to Make Dialogs

,
a section in

The Java Tutorial

.

While the

JOptionPane

class may appear complex because of the large number of methods, almost
all uses of this class are one-line calls to one of the static

showXxxDialog

methods shown below:

Common JOptionPane method names and their descriptions

Method Name

Description

showConfirmDialog

Asks a confirming question, like yes/no/cancel.

showInputDialog

Prompt for some input.

showMessageDialog

Tell the user about something that has happened.

showOptionDialog

The Grand Unification of the above three.

Each of these methods also comes in a

showInternalXXX

flavor, which uses an internal frame to hold the dialog box (see

JInternalFrame

).
Multiple convenience methods have also been defined -- overloaded
versions of the basic methods that use different parameter lists.

All dialogs are modal. Each

showXxxDialog

method blocks
the caller until the user's interaction is complete.

Common dialog

icon

message

input value

option buttons

The basic appearance of one of these dialog boxes is generally
similar to the picture above, although the various
look-and-feels are
ultimately responsible for the final result. In particular, the
look-and-feels will adjust the layout to accommodate the option pane's

ComponentOrientation

property.

Parameters:

The parameters to these methods follow consistent patterns:

When the selection is changed,

setValue

is invoked,
which generates a

PropertyChangeEvent

.

If a

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**Since:** 1.2
**See Also:** JInternalFrame

,

Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A component which implements standard dialog box controls.")
public class

JOptionPane

extends

JComponent

implements

Accessible

JOptionPane

makes it easy to pop up a standard dialog box that
prompts users for a value or informs them of something.
For information about using

JOptionPane

, see

How to Make Dialogs

,
a section in

The Java Tutorial

.

While the

JOptionPane

class may appear complex because of the large number of methods, almost
all uses of this class are one-line calls to one of the static

showXxxDialog

methods shown below:

Common JOptionPane method names and their descriptions

Method Name

Description

showConfirmDialog

Asks a confirming question, like yes/no/cancel.

showInputDialog

Prompt for some input.

showMessageDialog

Tell the user about something that has happened.

showOptionDialog

The Grand Unification of the above three.

Each of these methods also comes in a

showInternalXXX

flavor, which uses an internal frame to hold the dialog box (see

JInternalFrame

).
Multiple convenience methods have also been defined -- overloaded
versions of the basic methods that use different parameter lists.

All dialogs are modal. Each

showXxxDialog

method blocks
the caller until the user's interaction is complete.

Common dialog

icon

message

input value

option buttons

The basic appearance of one of these dialog boxes is generally
similar to the picture above, although the various
look-and-feels are
ultimately responsible for the final result. In particular, the
look-and-feels will adjust the layout to accommodate the option pane's

ComponentOrientation

property.

Parameters:

The parameters to these methods follow consistent patterns:

When the selection is changed,

setValue

is invoked,
which generates a

PropertyChangeEvent

.

If a

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

While the

JOptionPane

class may appear complex because of the large number of methods, almost
all uses of this class are one-line calls to one of the static

showXxxDialog

methods shown below:

Common JOptionPane method names and their descriptions

Method Name

Description

showConfirmDialog

Asks a confirming question, like yes/no/cancel.

showInputDialog

Prompt for some input.

showMessageDialog

Tell the user about something that has happened.

showOptionDialog

The Grand Unification of the above three.

Each of these methods also comes in a

showInternalXXX

flavor, which uses an internal frame to hold the dialog box (see

JInternalFrame

).
Multiple convenience methods have also been defined -- overloaded
versions of the basic methods that use different parameter lists.

All dialogs are modal. Each

showXxxDialog

method blocks
the caller until the user's interaction is complete.

Common dialog

icon

message

input value

option buttons

The basic appearance of one of these dialog boxes is generally
similar to the picture above, although the various
look-and-feels are
ultimately responsible for the final result. In particular, the
look-and-feels will adjust the layout to accommodate the option pane's

ComponentOrientation

property.

Parameters:

The parameters to these methods follow consistent patterns:

When the selection is changed,

setValue

is invoked,
which generates a

PropertyChangeEvent

.

If a

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

All dialogs are modal. Each

showXxxDialog

method blocks
the caller until the user's interaction is complete.

Common dialog

icon

message

input value

option buttons

The basic appearance of one of these dialog boxes is generally
similar to the picture above, although the various
look-and-feels are
ultimately responsible for the final result. In particular, the
look-and-feels will adjust the layout to accommodate the option pane's

ComponentOrientation

property.

Parameters:

The parameters to these methods follow consistent patterns:

When the selection is changed,

setValue

is invoked,
which generates a

PropertyChangeEvent

.

If a

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

Parameters:

The parameters to these methods follow consistent patterns:

When the selection is changed,

setValue

is invoked,
which generates a

PropertyChangeEvent

.

If a

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

ERROR_MESSAGE

INFORMATION_MESSAGE

WARNING_MESSAGE

QUESTION_MESSAGE

PLAIN_MESSAGE

DEFAULT_OPTION

YES_NO_OPTION

YES_NO_CANCEL_OPTION

OK_CANCEL_OPTION

When the selection is changed,

setValue

is invoked,
which generates a

PropertyChangeEvent

.

If a

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

JOptionPane

has configured to all input

setWantsInput

the bound property

JOptionPane.INPUT_VALUE_PROPERTY

can also be listened
to, to determine when the user has input or selected a value.

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

When one of the

showXxxDialog

methods returns an integer,
the possible values are:

- YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

Examples:

Direct Use:

To create and use an

JOptionPane

directly, the
standard pattern is roughly as follows:

```java
JOptionPane pane = new JOptionPane(
arguments
);
pane.set
.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(
parentComponent, title
);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is
not
an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;
```

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

YES_OPTION

NO_OPTION

CANCEL_OPTION

OK_OPTION

CLOSED_OPTION

JOptionPane.showInternalMessageDialog(frame, "information",
"information", JOptionPane.INFORMATION_MESSAGE);

JOptionPane.showConfirmDialog(null,
"choose one", "choose one", JOptionPane.YES_NO_OPTION);

JOptionPane.showInternalConfirmDialog(frame,
"please choose one", "information",
JOptionPane.YES_NO_CANCEL_OPTION, JOptionPane.INFORMATION_MESSAGE);

Object[] options = { "OK", "CANCEL" };
JOptionPane.showOptionDialog(null, "Click OK to continue", "Warning",
JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE,
null, options, options[0]);

Object[] possibleValues = { "First", "Second", "Third" };

Object selectedValue = JOptionPane.showInputDialog(null,
"Choose one", "Input",
JOptionPane.INFORMATION_MESSAGE, null,
possibleValues, possibleValues[0]);

JOptionPane pane = new JOptionPane(

arguments

);
pane.set

.Xxxx(...); // Configure

JDialog dialog = pane.createDialog(

parentComponent, title

);
dialog.show();
Object selectedValue = pane.getValue();
if(selectedValue == null)
return CLOSED_OPTION;

//If there is

not

an array of option buttons:

if(options == null) {
if(selectedValue instanceof Integer)
return ((Integer)selectedValue).intValue();
return CLOSED_OPTION;
}

//If there is an array of option buttons:

for(int counter = 0, maxCounter = options.length;
counter < maxCounter; counter++) {
if(options[counter].equals(selectedValue))
return counter;
}
return CLOSED_OPTION;

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JOptionPane.AccessibleJOptionPane

This class implements accessibility support for the

JOptionPane

class.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CANCEL_OPTION

Return value from class method if CANCEL is chosen.

static int

CLOSED_OPTION

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

static int

DEFAULT_OPTION

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

static int

ERROR_MESSAGE

Used for error messages.

protected

Icon

icon

Icon used in pane.

static

String

ICON_PROPERTY

Bound property name for

icon

.

static int

INFORMATION_MESSAGE

Used for information messages.

static

String

INITIAL_SELECTION_VALUE_PROPERTY

Bound property name for

initialSelectionValue

.

static

String

INITIAL_VALUE_PROPERTY

Bound property name for

initialValue

.

protected

Object

initialSelectionValue

Initial value to select in

selectionValues

.

protected

Object

initialValue

Value that should be initially selected in

options

.

static

String

INPUT_VALUE_PROPERTY

Bound property name for

inputValue

.

protected

Object

inputValue

Value the user has input.

protected

Object

message

Message to display.

static

String

MESSAGE_PROPERTY

Bound property name for

message

.

static

String

MESSAGE_TYPE_PROPERTY

Bound property name for

type

.

protected int

messageType

Message type.

static int

NO_OPTION

Return value from class method if NO is chosen.

static int

OK_CANCEL_OPTION

Type used for

showConfirmDialog

.

static int

OK_OPTION

Return value form class method if OK is chosen.

static

String

OPTION_TYPE_PROPERTY

Bound property name for

optionType

.

protected

Object

[]

options

Options to display to the user.

static

String

OPTIONS_PROPERTY

Bound property name for

option

.

protected int

optionType

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

static int

PLAIN_MESSAGE

No icon is used.

static int

QUESTION_MESSAGE

Used for questions.

static

String

SELECTION_VALUES_PROPERTY

Bound property name for

selectionValues

.

protected

Object

[]

selectionValues

Array of values the user can choose from.

static

Object

UNINITIALIZED_VALUE

Indicates that the user has not yet selected a value.

protected

Object

value

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

static

String

VALUE_PROPERTY

Bound property name for

value

.

static

String

WANTS_INPUT_PROPERTY

Bound property name for

wantsInput

.

protected boolean

wantsInput

If true, a UI widget will be provided to the user to get input.

static int

WARNING_MESSAGE

Used for warning messages.

static int

YES_NO_CANCEL_OPTION

Type used for

showConfirmDialog

.

static int

YES_NO_OPTION

Type used for

showConfirmDialog

.

static int

YES_OPTION

Return value from class method if YES is chosen.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JOptionPane

()

Creates a

JOptionPane

with a test message.

JOptionPane

​(

Object

message)

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

JOptionPane

​(

Object

message,
int messageType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

JOptionPane

​(

Object

message,
int messageType,
int optionType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

JOptionPane

​(

Object

message,
int messageType,
int optionType,

Icon

icon)

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

JOptionPane

​(

Object

message,
int messageType,
int optionType,

Icon

icon,

Object

[] options)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.

JOptionPane

​(

Object

message,
int messageType,
int optionType,

Icon

icon,

Object

[] options,

Object

initialValue)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JDialog

createDialog

​(

Component

parentComponent,

String

title)

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

JDialog

createDialog

​(

String

title)

Creates and returns a new parentless

JDialog

with the specified title.

JInternalFrame

createInternalFrame

​(

Component

parentComponent,

String

title)

Creates and returns an instance of

JInternalFrame

.

AccessibleContext

getAccessibleContext

()

Returns the

AccessibleContext

associated with this JOptionPane.

static

JDesktopPane

getDesktopPaneForComponent

​(

Component

parentComponent)

Returns the specified component's desktop pane.

static

Frame

getFrameForComponent

​(

Component

parentComponent)

Returns the specified component's

Frame

.

Icon

getIcon

()

Returns the icon this pane displays.

Object

getInitialSelectionValue

()

Returns the input value that is displayed as initially selected to the user.

Object

getInitialValue

()

Returns the initial value.

Object

getInputValue

()

Returns the value the user has input, if

wantsInput

is true.

int

getMaxCharactersPerLineCount

()

Returns the maximum number of characters to place on a line in a
message.

Object

getMessage

()

Returns the message-object this pane displays.

int

getMessageType

()

Returns the message type.

Object

[]

getOptions

()

Returns the choices the user can make.

int

getOptionType

()

Returns the type of options that are displayed.

static

Frame

getRootFrame

()

Returns the

Frame

to use for the class methods in
which a frame is not provided.

Object

[]

getSelectionValues

()

Returns the input selection values.

OptionPaneUI

getUI

()

Returns the UI object which implements the L&F for this component.

String

getUIClassID

()

Returns the name of the UI class that implements the
L&F for this component.

Object

getValue

()

Returns the value the user has selected.

boolean

getWantsInput

()

Returns the value of the

wantsInput

property.

protected

String

paramString

()

Returns a string representation of this

JOptionPane

.

void

selectInitialValue

()

Requests that the initial value be selected, which will set
focus to the initial value.

void

setIcon

​(

Icon

newIcon)

Sets the icon to display.

void

setInitialSelectionValue

​(

Object

newValue)

Sets the input value that is initially displayed as selected to the user.

void

setInitialValue

​(

Object

newInitialValue)

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

void

setInputValue

​(

Object

newValue)

Sets the input value that was selected or input by the user.

void

setMessage

​(

Object

newMessage)

Sets the option pane's message-object.

void

setMessageType

​(int newType)

Sets the option pane's message type.

void

setOptions

​(

Object

[] newOptions)

Sets the options this pane displays.

void

setOptionType

​(int newType)

Sets the options to display.

static void

setRootFrame

​(

Frame

newRootFrame)

Sets the frame to use for class methods in which a frame is
not provided.

void

setSelectionValues

​(

Object

[] newValues)

Sets the input selection values for a pane that provides the user
with a list of items to choose from.

void

setUI

​(

OptionPaneUI

ui)

Sets the UI object which implements the L&F for this component.

void

setValue

​(

Object

newValue)

Sets the value the user has chosen.

void

setWantsInput

​(boolean newValue)

Sets the

wantsInput

property.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message)

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType)

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType)

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon)

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.

static

String

showInputDialog

​(

Component

parentComponent,

Object

message)

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.

static

String

showInputDialog

​(

Component

parentComponent,

Object

message,

Object

initialSelectionValue)

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

.

static

String

showInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

static

Object

showInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon,

Object

[] selectionValues,

Object

initialSelectionValue)

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified.

static

String

showInputDialog

​(

Object

message)

Shows a question-message dialog requesting input from the user.

static

String

showInputDialog

​(

Object

message,

Object

initialSelectionValue)

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message)

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType)

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType)

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon)

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.

static

String

showInternalInputDialog

​(

Component

parentComponent,

Object

message)

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

.

static

String

showInternalInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

static

Object

showInternalInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon,

Object

[] selectionValues,

Object

initialSelectionValue)

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified.

static void

showInternalMessageDialog

​(

Component

parentComponent,

Object

message)

Brings up an internal confirmation dialog panel.

static void

showInternalMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

static void

showInternalMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon)

Brings up an internal dialog panel displaying a message,
specifying all parameters.

static int

showInternalOptionDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon,

Object

[] options,

Object

initialValue)

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

static void

showMessageDialog

​(

Component

parentComponent,

Object

message)

Brings up an information-message dialog titled "Message".

static void

showMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

static void

showMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon)

Brings up a dialog displaying a message, specifying all parameters.

static int

showOptionDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon,

Object

[] options,

Object

initialValue)

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

void

updateUI

()

Notification from the

UIManager

that the L&F has changed.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

- Methods declared in class java.lang.

Object

clone

,

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

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JOptionPane.AccessibleJOptionPane

This class implements accessibility support for the

JOptionPane

class.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

This class implements accessibility support for the

JOptionPane

class.

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

static int

CANCEL_OPTION

Return value from class method if CANCEL is chosen.

static int

CLOSED_OPTION

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

static int

DEFAULT_OPTION

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

static int

ERROR_MESSAGE

Used for error messages.

protected

Icon

icon

Icon used in pane.

static

String

ICON_PROPERTY

Bound property name for

icon

.

static int

INFORMATION_MESSAGE

Used for information messages.

static

String

INITIAL_SELECTION_VALUE_PROPERTY

Bound property name for

initialSelectionValue

.

static

String

INITIAL_VALUE_PROPERTY

Bound property name for

initialValue

.

protected

Object

initialSelectionValue

Initial value to select in

selectionValues

.

protected

Object

initialValue

Value that should be initially selected in

options

.

static

String

INPUT_VALUE_PROPERTY

Bound property name for

inputValue

.

protected

Object

inputValue

Value the user has input.

protected

Object

message

Message to display.

static

String

MESSAGE_PROPERTY

Bound property name for

message

.

static

String

MESSAGE_TYPE_PROPERTY

Bound property name for

type

.

protected int

messageType

Message type.

static int

NO_OPTION

Return value from class method if NO is chosen.

static int

OK_CANCEL_OPTION

Type used for

showConfirmDialog

.

static int

OK_OPTION

Return value form class method if OK is chosen.

static

String

OPTION_TYPE_PROPERTY

Bound property name for

optionType

.

protected

Object

[]

options

Options to display to the user.

static

String

OPTIONS_PROPERTY

Bound property name for

option

.

protected int

optionType

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

static int

PLAIN_MESSAGE

No icon is used.

static int

QUESTION_MESSAGE

Used for questions.

static

String

SELECTION_VALUES_PROPERTY

Bound property name for

selectionValues

.

protected

Object

[]

selectionValues

Array of values the user can choose from.

static

Object

UNINITIALIZED_VALUE

Indicates that the user has not yet selected a value.

protected

Object

value

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

static

String

VALUE_PROPERTY

Bound property name for

value

.

static

String

WANTS_INPUT_PROPERTY

Bound property name for

wantsInput

.

protected boolean

wantsInput

If true, a UI widget will be provided to the user to get input.

static int

WARNING_MESSAGE

Used for warning messages.

static int

YES_NO_CANCEL_OPTION

Type used for

showConfirmDialog

.

static int

YES_NO_OPTION

Type used for

showConfirmDialog

.

static int

YES_OPTION

Return value from class method if YES is chosen.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Return value from class method if CANCEL is chosen.

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

Used for error messages.

Icon used in pane.

Bound property name for

icon

.

Used for information messages.

Bound property name for

initialSelectionValue

.

Bound property name for

initialValue

.

Initial value to select in

selectionValues

.

Value that should be initially selected in

options

.

Bound property name for

inputValue

.

Value the user has input.

Message to display.

Bound property name for

message

.

Bound property name for

type

.

Message type.

Return value from class method if NO is chosen.

Type used for

showConfirmDialog

.

Return value form class method if OK is chosen.

Bound property name for

optionType

.

Options to display to the user.

Bound property name for

option

.

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

No icon is used.

Used for questions.

Bound property name for

selectionValues

.

Array of values the user can choose from.

Indicates that the user has not yet selected a value.

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

Bound property name for

value

.

Bound property name for

wantsInput

.

If true, a UI widget will be provided to the user to get input.

Used for warning messages.

Return value from class method if YES is chosen.

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

JOptionPane

()

Creates a

JOptionPane

with a test message.

JOptionPane

​(

Object

message)

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

JOptionPane

​(

Object

message,
int messageType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

JOptionPane

​(

Object

message,
int messageType,
int optionType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

JOptionPane

​(

Object

message,
int messageType,
int optionType,

Icon

icon)

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

JOptionPane

​(

Object

message,
int messageType,
int optionType,

Icon

icon,

Object

[] options)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.

JOptionPane

​(

Object

message,
int messageType,
int optionType,

Icon

icon,

Object

[] options,

Object

initialValue)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

---

#### Constructor Summary

Creates a

JOptionPane

with a test message.

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JDialog

createDialog

​(

Component

parentComponent,

String

title)

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

JDialog

createDialog

​(

String

title)

Creates and returns a new parentless

JDialog

with the specified title.

JInternalFrame

createInternalFrame

​(

Component

parentComponent,

String

title)

Creates and returns an instance of

JInternalFrame

.

AccessibleContext

getAccessibleContext

()

Returns the

AccessibleContext

associated with this JOptionPane.

static

JDesktopPane

getDesktopPaneForComponent

​(

Component

parentComponent)

Returns the specified component's desktop pane.

static

Frame

getFrameForComponent

​(

Component

parentComponent)

Returns the specified component's

Frame

.

Icon

getIcon

()

Returns the icon this pane displays.

Object

getInitialSelectionValue

()

Returns the input value that is displayed as initially selected to the user.

Object

getInitialValue

()

Returns the initial value.

Object

getInputValue

()

Returns the value the user has input, if

wantsInput

is true.

int

getMaxCharactersPerLineCount

()

Returns the maximum number of characters to place on a line in a
message.

Object

getMessage

()

Returns the message-object this pane displays.

int

getMessageType

()

Returns the message type.

Object

[]

getOptions

()

Returns the choices the user can make.

int

getOptionType

()

Returns the type of options that are displayed.

static

Frame

getRootFrame

()

Returns the

Frame

to use for the class methods in
which a frame is not provided.

Object

[]

getSelectionValues

()

Returns the input selection values.

OptionPaneUI

getUI

()

Returns the UI object which implements the L&F for this component.

String

getUIClassID

()

Returns the name of the UI class that implements the
L&F for this component.

Object

getValue

()

Returns the value the user has selected.

boolean

getWantsInput

()

Returns the value of the

wantsInput

property.

protected

String

paramString

()

Returns a string representation of this

JOptionPane

.

void

selectInitialValue

()

Requests that the initial value be selected, which will set
focus to the initial value.

void

setIcon

​(

Icon

newIcon)

Sets the icon to display.

void

setInitialSelectionValue

​(

Object

newValue)

Sets the input value that is initially displayed as selected to the user.

void

setInitialValue

​(

Object

newInitialValue)

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

void

setInputValue

​(

Object

newValue)

Sets the input value that was selected or input by the user.

void

setMessage

​(

Object

newMessage)

Sets the option pane's message-object.

void

setMessageType

​(int newType)

Sets the option pane's message type.

void

setOptions

​(

Object

[] newOptions)

Sets the options this pane displays.

void

setOptionType

​(int newType)

Sets the options to display.

static void

setRootFrame

​(

Frame

newRootFrame)

Sets the frame to use for class methods in which a frame is
not provided.

void

setSelectionValues

​(

Object

[] newValues)

Sets the input selection values for a pane that provides the user
with a list of items to choose from.

void

setUI

​(

OptionPaneUI

ui)

Sets the UI object which implements the L&F for this component.

void

setValue

​(

Object

newValue)

Sets the value the user has chosen.

void

setWantsInput

​(boolean newValue)

Sets the

wantsInput

property.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message)

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType)

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType)

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.

static int

showConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon)

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.

static

String

showInputDialog

​(

Component

parentComponent,

Object

message)

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.

static

String

showInputDialog

​(

Component

parentComponent,

Object

message,

Object

initialSelectionValue)

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

.

static

String

showInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

static

Object

showInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon,

Object

[] selectionValues,

Object

initialSelectionValue)

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified.

static

String

showInputDialog

​(

Object

message)

Shows a question-message dialog requesting input from the user.

static

String

showInputDialog

​(

Object

message,

Object

initialSelectionValue)

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message)

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType)

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType)

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.

static int

showInternalConfirmDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon)

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.

static

String

showInternalInputDialog

​(

Component

parentComponent,

Object

message)

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

.

static

String

showInternalInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

static

Object

showInternalInputDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon,

Object

[] selectionValues,

Object

initialSelectionValue)

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified.

static void

showInternalMessageDialog

​(

Component

parentComponent,

Object

message)

Brings up an internal confirmation dialog panel.

static void

showInternalMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

static void

showInternalMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon)

Brings up an internal dialog panel displaying a message,
specifying all parameters.

static int

showInternalOptionDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon,

Object

[] options,

Object

initialValue)

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

static void

showMessageDialog

​(

Component

parentComponent,

Object

message)

Brings up an information-message dialog titled "Message".

static void

showMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

static void

showMessageDialog

​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon)

Brings up a dialog displaying a message, specifying all parameters.

static int

showOptionDialog

​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon,

Object

[] options,

Object

initialValue)

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

void

updateUI

()

Notification from the

UIManager

that the L&F has changed.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

- Methods declared in class java.lang.

Object

clone

,

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

wait

,

wait

,

wait

---

#### Method Summary

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

Creates and returns a new parentless

JDialog

with the specified title.

Creates and returns an instance of

JInternalFrame

.

Returns the

AccessibleContext

associated with this JOptionPane.

Returns the specified component's desktop pane.

Returns the specified component's

Frame

.

Returns the icon this pane displays.

Returns the input value that is displayed as initially selected to the user.

Returns the initial value.

Returns the value the user has input, if

wantsInput

is true.

Returns the maximum number of characters to place on a line in a
message.

Returns the message-object this pane displays.

Returns the message type.

Returns the choices the user can make.

Returns the type of options that are displayed.

Returns the

Frame

to use for the class methods in
which a frame is not provided.

Returns the input selection values.

Returns the UI object which implements the L&F for this component.

Returns the name of the UI class that implements the
L&F for this component.

Returns the value the user has selected.

Returns the value of the

wantsInput

property.

Returns a string representation of this

JOptionPane

.

Requests that the initial value be selected, which will set
focus to the initial value.

Sets the icon to display.

Sets the input value that is initially displayed as selected to the user.

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

Sets the input value that was selected or input by the user.

Sets the option pane's message-object.

Sets the option pane's message type.

Sets the options this pane displays.

Sets the options to display.

Sets the frame to use for class methods in which a frame is
not provided.

Sets the input selection values for a pane that provides the user
with a list of items to choose from.

Sets the UI object which implements the L&F for this component.

Sets the value the user has chosen.

Sets the

wantsInput

property.

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

.

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified.

Shows a question-message dialog requesting input from the user.

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

.

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

.

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified.

Brings up an internal confirmation dialog panel.

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

Brings up an internal dialog panel displaying a message,
specifying all parameters.

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

Brings up an information-message dialog titled "Message".

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

Brings up a dialog displaying a message, specifying all parameters.

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

Notification from the

UIManager

that the L&F has changed.

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

Methods declared in class java.lang.

Object

clone

,

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- UNINITIALIZED_VALUE

```java
public static final
Object
UNINITIALIZED_VALUE
```

Indicates that the user has not yet selected a value.

- DEFAULT_OPTION

```java
public static final int DEFAULT_OPTION
```

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

**See Also:** Constant Field Values

- YES_NO_OPTION

```java
public static final int YES_NO_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

- YES_NO_CANCEL_OPTION

```java
public static final int YES_NO_CANCEL_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

- OK_CANCEL_OPTION

```java
public static final int OK_CANCEL_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

- YES_OPTION

```java
public static final int YES_OPTION
```

Return value from class method if YES is chosen.

**See Also:** Constant Field Values

- NO_OPTION

```java
public static final int NO_OPTION
```

Return value from class method if NO is chosen.

**See Also:** Constant Field Values

- CANCEL_OPTION

```java
public static final int CANCEL_OPTION
```

Return value from class method if CANCEL is chosen.

**See Also:** Constant Field Values

- OK_OPTION

```java
public static final int OK_OPTION
```

Return value form class method if OK is chosen.

**See Also:** Constant Field Values

- CLOSED_OPTION

```java
public static final int CLOSED_OPTION
```

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

**See Also:** Constant Field Values

- ERROR_MESSAGE

```java
public static final int ERROR_MESSAGE
```

Used for error messages.

**See Also:** Constant Field Values

- INFORMATION_MESSAGE

```java
public static final int INFORMATION_MESSAGE
```

Used for information messages.

**See Also:** Constant Field Values

- WARNING_MESSAGE

```java
public static final int WARNING_MESSAGE
```

Used for warning messages.

**See Also:** Constant Field Values

- QUESTION_MESSAGE

```java
public static final int QUESTION_MESSAGE
```

Used for questions.

**See Also:** Constant Field Values

- PLAIN_MESSAGE

```java
public static final int PLAIN_MESSAGE
```

No icon is used.

**See Also:** Constant Field Values

- ICON_PROPERTY

```java
public static final
String
ICON_PROPERTY
```

Bound property name for

icon

.

**See Also:** Constant Field Values

- MESSAGE_PROPERTY

```java
public static final
String
MESSAGE_PROPERTY
```

Bound property name for

message

.

**See Also:** Constant Field Values

- VALUE_PROPERTY

```java
public static final
String
VALUE_PROPERTY
```

Bound property name for

value

.

**See Also:** Constant Field Values

- OPTIONS_PROPERTY

```java
public static final
String
OPTIONS_PROPERTY
```

Bound property name for

option

.

**See Also:** Constant Field Values

- INITIAL_VALUE_PROPERTY

```java
public static final
String
INITIAL_VALUE_PROPERTY
```

Bound property name for

initialValue

.

**See Also:** Constant Field Values

- MESSAGE_TYPE_PROPERTY

```java
public static final
String
MESSAGE_TYPE_PROPERTY
```

Bound property name for

type

.

**See Also:** Constant Field Values

- OPTION_TYPE_PROPERTY

```java
public static final
String
OPTION_TYPE_PROPERTY
```

Bound property name for

optionType

.

**See Also:** Constant Field Values

- SELECTION_VALUES_PROPERTY

```java
public static final
String
SELECTION_VALUES_PROPERTY
```

Bound property name for

selectionValues

.

**See Also:** Constant Field Values

- INITIAL_SELECTION_VALUE_PROPERTY

```java
public static final
String
INITIAL_SELECTION_VALUE_PROPERTY
```

Bound property name for

initialSelectionValue

.

**See Also:** Constant Field Values

- INPUT_VALUE_PROPERTY

```java
public static final
String
INPUT_VALUE_PROPERTY
```

Bound property name for

inputValue

.

**See Also:** Constant Field Values

- WANTS_INPUT_PROPERTY

```java
public static final
String
WANTS_INPUT_PROPERTY
```

Bound property name for

wantsInput

.

**See Also:** Constant Field Values

- icon

```java
protected transient
Icon
icon
```

Icon used in pane.

- message

```java
protected transient
Object
message
```

Message to display.

- options

```java
protected transient
Object
[] options
```

Options to display to the user.

- initialValue

```java
protected transient
Object
initialValue
```

Value that should be initially selected in

options

.

- messageType

```java
protected int messageType
```

Message type.

- optionType

```java
protected int optionType
```

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

- value

```java
protected transient
Object
value
```

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

- selectionValues

```java
protected transient
Object
[] selectionValues
```

Array of values the user can choose from. Look and feel will
provide the UI component to choose this from.

- inputValue

```java
protected transient
Object
inputValue
```

Value the user has input.

- initialSelectionValue

```java
protected transient
Object
initialSelectionValue
```

Initial value to select in

selectionValues

.

- wantsInput

```java
protected boolean wantsInput
```

If true, a UI widget will be provided to the user to get input.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JOptionPane

```java
public JOptionPane()
```

Creates a

JOptionPane

with a test message.

- JOptionPane

```java
public JOptionPane​(
Object
message)
```

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

**Parameters:** message

- the

Object

to display

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the

Icon

image to display

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.
None of the options is initially selected.

The options objects should contain either instances of

Component

s, (which are added directly) or

Strings

(which are wrapped in a

JButton

).
If you provide

Component

s, you must ensure that when the

Component

is clicked it messages

setValue

in the created

JOptionPane

.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the

Icon

image to display
**Parameters:** options

- the choices the user can select

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options,

Object
initialValue)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the Icon image to display
**Parameters:** options

- the choices the user can select
**Parameters:** initialValue

- the choice that is initially selected; if

null

, then nothing will be initially selected;
only meaningful if

options

is used

============ METHOD DETAIL ==========

- Method Detail

- showInputDialog

```java
public static
String
showInputDialog​(
Object
message)
throws
HeadlessException
```

Shows a question-message dialog requesting input from the user. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:** message

- the

Object

to display
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showInputDialog

```java
public static
String
showInputDialog​(
Object
message,

Object
initialSelectionValue)
```

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:** message

- the

Object

to display
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input
**Since:** 1.4

- showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

Object
initialSelectionValue)
```

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

. The input value will be
initialized to

initialSelectionValue

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input
**Since:** 1.4

- showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException
```

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the dialog
title bar
**Parameters:** messageType

- the type of message that is to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showInputDialog

```java
public static
Object
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)
throws
HeadlessException
```

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified. The user will able to choose from

selectionValues

, where

null

implies the
user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the
dialog title bar
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the

Icon

image to display
**Parameters:** selectionValues

- an array of

Object

s that
gives the possible selections
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input, or

null

meaning the user
canceled the input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Brings up an information-message dialog titled "Message".

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException
```

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)
throws
HeadlessException
```

Brings up a dialog displaying a message, specifying all parameters.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Returns:** an integer indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)
throws
HeadlessException
```

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Returns:** an int indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)
throws
HeadlessException
```

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used.
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** an integer indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)
throws
HeadlessException
```

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the Object to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an int designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Returns:** an int indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showOptionDialog

```java
public static int showOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)
throws
HeadlessException
```

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are
supplied by the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

, or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available on the
dialog:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Parameters:** options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are
rendered using their

toString

methods;
if this parameter is

null

,
the options are determined by the Look and Feel
**Parameters:** initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null
**Returns:** an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed
the dialog
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- createDialog

```java
public
JDialog
createDialog​(
Component
parentComponent,

String
title)
throws
HeadlessException
```

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

title

is the title of the returned dialog.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:** parentComponent

- determines the frame in which the dialog
is displayed; if the

parentComponent

has
no

Frame

, a default

Frame

is used
**Parameters:** title

- the title string for the dialog
**Returns:** a new

JDialog

containing this instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- createDialog

```java
public
JDialog
createDialog​(
String
title)
throws
HeadlessException
```

Creates and returns a new parentless

JDialog

with the specified title.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:** title

- the title string for the dialog
**Returns:** a new

JDialog

containing this instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

- showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message)
```

Brings up an internal confirmation dialog panel. The dialog
is a information-message dialog titled "Message".

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display

- showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
```

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

- showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)
```

Brings up an internal dialog panel displaying a message,
specifying all parameters.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message)
```

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Returns:** an integer indicating the option selected by the user

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)
```

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects
are converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION
**Returns:** an integer indicating the option selected by the user

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)
```

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** an integer indicating the option selected by the user

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)
```

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the parentComponent has no Frame, a
default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

.
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Returns:** an integer indicating the option selected by the user

- showInternalOptionDialog

```java
public static int showInternalOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)
```

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are supplied by the Look and Feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string. Other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Parameters:** options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are rendered using their

toString

methods; if this parameter is

null

,
the options are determined by the Look and Feel
**Parameters:** initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null
**Returns:** an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed the Dialog

- showInternalInputDialog

```java
public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message)
```

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

. The dialog
is displayed in the

Component

's frame,
and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Returns:** user's input

- showInternalInputDialog

```java
public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
```

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the
dialog title bar
**Parameters:** messageType

- the type of message that is to be displayed:
ERROR_MESSAGE, INFORMATION_MESSAGE, WARNING_MESSAGE,
QUESTION_MESSAGE, or PLAIN_MESSAGE
**Returns:** user's input

- showInternalInputDialog

```java
public static
Object
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)
```

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified. The user will able to choose from

selectionValues

, where

null

implies the user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the dialog
title bar
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE
**Parameters:** icon

- the

Icon

image to display
**Parameters:** selectionValues

- an array of

Objects

that
gives the possible selections
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input, or

null

meaning the user
canceled the input

- createInternalFrame

```java
public
JInternalFrame
createInternalFrame​(
Component
parentComponent,

String
title)
```

Creates and returns an instance of

JInternalFrame

.
The internal frame is created with the specified title,
and wrapping the

JOptionPane

.
The returned

JInternalFrame

is
added to the

JDesktopPane

ancestor of

parentComponent

, or components
parent if one its ancestors isn't a

JDesktopPane

,
or if

parentComponent

doesn't have a parent then a

RuntimeException

is thrown.

**Parameters:** parentComponent

- the parent

Component

for
the internal frame
**Parameters:** title

- the

String

to display in the
frame's title bar
**Returns:** a

JInternalFrame

containing a

JOptionPane
**Throws:** RuntimeException

- if

parentComponent

does
not have a valid parent

- getFrameForComponent

```java
public static
Frame
getFrameForComponent​(
Component
parentComponent)
throws
HeadlessException
```

Returns the specified component's

Frame

.

**Parameters:** parentComponent

- the

Component

to check for a

Frame
**Returns:** the

Frame

that contains the component,
or

getRootFrame

if the component is

null

,
or does not have a valid

Frame

parent
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** getRootFrame()

,

GraphicsEnvironment.isHeadless()

- getDesktopPaneForComponent

```java
public static
JDesktopPane
getDesktopPaneForComponent​(
Component
parentComponent)
```

Returns the specified component's desktop pane.

**Parameters:** parentComponent

- the

Component

to check for a
desktop
**Returns:** the

JDesktopPane

that contains the component,
or

null

if the component is

null

or does not have an ancestor that is a

JInternalFrame

- setRootFrame

```java
public static void setRootFrame​(
Frame
newRootFrame)
```

Sets the frame to use for class methods in which a frame is
not provided.

Note:

It is recommended that rather than using this method you supply a valid parent.

**Parameters:** newRootFrame

- the default

Frame

to use

- getRootFrame

```java
public static
Frame
getRootFrame()
throws
HeadlessException
```

Returns the

Frame

to use for the class methods in
which a frame is not provided.

**Returns:** the default

Frame

to use
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** setRootFrame(java.awt.Frame)

,

GraphicsEnvironment.isHeadless()

- setUI

```java
@BeanProperty
(
hidden
=true,

description
="The UI object that implements the optionpane\'s LookAndFeel")
public void setUI​(
OptionPaneUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the

OptionPaneUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- getUI

```java
public
OptionPaneUI
getUI()
```

Returns the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

OptionPaneUI

object

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "OptionPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setMessage

```java
@BeanProperty
(
preferred
=true,

description
="The optionpane\'s message object.")
public void setMessage​(
Object
newMessage)
```

Sets the option pane's message-object.

**Parameters:** newMessage

- the

Object

to display
**See Also:** getMessage()

- getMessage

```java
public
Object
getMessage()
```

Returns the message-object this pane displays.

**Returns:** the

Object

that is displayed
**See Also:** setMessage(java.lang.Object)

- setIcon

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s type icon.")
public void setIcon​(
Icon
newIcon)
```

Sets the icon to display. If non-

null

, the look and feel
does not provide an icon.

**Parameters:** newIcon

- the

Icon

to display
**See Also:** getIcon()

- getIcon

```java
public
Icon
getIcon()
```

Returns the icon this pane displays.

**Returns:** the

Icon

that is displayed
**See Also:** setIcon(javax.swing.Icon)

- setValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s value object.")
public void setValue​(
Object
newValue)
```

Sets the value the user has chosen.

**Parameters:** newValue

- the chosen value
**See Also:** getValue()

- getValue

```java
public
Object
getValue()
```

Returns the value the user has selected.

UNINITIALIZED_VALUE

implies the user has not yet made a choice,

null

means the
user closed the window with out choosing anything. Otherwise
the returned value will be one of the options defined in this
object.

**Returns:** the

Object

chosen by the user,

UNINITIALIZED_VALUE

if the user has not yet made a choice, or

null

if
the user closed the window without making a choice
**See Also:** setValue(java.lang.Object)

- setOptions

```java
@BeanProperty
(
description
="The option pane\'s options objects.")
public void setOptions​(
Object
[] newOptions)
```

Sets the options this pane displays. If an element in

newOptions

is a

Component

it is added directly to the pane,
otherwise a button is created for the element.

**Parameters:** newOptions

- an array of

Objects

that create the
buttons the user can click on, or arbitrary

Components

to add to the pane
**See Also:** getOptions()

- getOptions

```java
public
Object
[] getOptions()
```

Returns the choices the user can make.

**Returns:** the array of

Objects

that give the user's choices
**See Also:** setOptions(java.lang.Object[])

- setInitialValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s initial value object.")
public void setInitialValue​(
Object
newInitialValue)
```

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

**Parameters:** newInitialValue

- the

Object

that gets the initial
keyboard focus
**See Also:** getInitialValue()

- getInitialValue

```java
public
Object
getInitialValue()
```

Returns the initial value.

**Returns:** the

Object

that gets the initial keyboard focus
**See Also:** setInitialValue(java.lang.Object)

- setMessageType

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s message type.")
public void setMessageType​(int newType)
```

Sets the option pane's message type.
The message type is used by the Look and Feel to determine the
icon to display (if not supplied) as well as potentially how to
lay out the

parentComponent

.

**Parameters:** newType

- an integer specifying the kind of message to display:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE
**Throws:** RuntimeException

- if

newType

is not one of the
legal values listed above
**See Also:** getMessageType()

- getMessageType

```java
public int getMessageType()
```

Returns the message type.

**Returns:** an integer specifying the message type
**See Also:** setMessageType(int)

- setOptionType

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s option type.")
public void setOptionType​(int newType)
```

Sets the options to display.
The option type is used by the Look and Feel to
determine what buttons to show (unless options are supplied).

**Parameters:** newType

- an integer specifying the options the L&F is to display:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Throws:** RuntimeException

- if

newType

is not one of
the legal values listed above
**See Also:** getOptionType()

,

setOptions(java.lang.Object[])

- getOptionType

```java
public int getOptionType()
```

Returns the type of options that are displayed.

**Returns:** an integer specifying the user-selectable options
**See Also:** setOptionType(int)

- setSelectionValues

```java
@BeanProperty
(
description
="The option pane\'s selection values.")
public void setSelectionValues​(
Object
[] newValues)
```

Sets the input selection values for a pane that provides the user
with a list of items to choose from. (The UI provides a widget
for choosing one of the values.) A

null

value
implies the user can input whatever they wish, usually by means
of a

JTextField

.

Sets

wantsInput

to true. Use

setInitialSelectionValue

to specify the initially-chosen
value. After the pane as been enabled,

inputValue

is
set to the value the user has selected.

**Parameters:** newValues

- an array of

Objects

the user to be
displayed
(usually in a list or combo-box) from which
the user can make a selection
**See Also:** setWantsInput(boolean)

,

setInitialSelectionValue(java.lang.Object)

,

getSelectionValues()

- getSelectionValues

```java
public
Object
[] getSelectionValues()
```

Returns the input selection values.

**Returns:** the array of

Objects

the user can select
**See Also:** setSelectionValues(java.lang.Object[])

- setInitialSelectionValue

```java
@BeanProperty
(
description
="The option pane\'s initial selection value object.")
public void setInitialSelectionValue​(
Object
newValue)
```

Sets the input value that is initially displayed as selected to the user.
Only used if

wantsInput

is true.

**Parameters:** newValue

- the initially selected value
**See Also:** setSelectionValues(java.lang.Object[])

,

getInitialSelectionValue()

- getInitialSelectionValue

```java
public
Object
getInitialSelectionValue()
```

Returns the input value that is displayed as initially selected to the user.

**Returns:** the initially selected value
**See Also:** setInitialSelectionValue(java.lang.Object)

,

setSelectionValues(java.lang.Object[])

- setInputValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s input value object.")
public void setInputValue​(
Object
newValue)
```

Sets the input value that was selected or input by the user.
Only used if

wantsInput

is true. Note that this method
is invoked internally by the option pane (in response to user action)
and should generally not be called by client programs. To set the
input value initially displayed as selected to the user, use

setInitialSelectionValue

.

**Parameters:** newValue

- the

Object

used to set the
value that the user specified (usually in a text field)
**See Also:** setSelectionValues(java.lang.Object[])

,

setInitialSelectionValue(java.lang.Object)

,

setWantsInput(boolean)

,

getInputValue()

- getInputValue

```java
public
Object
getInputValue()
```

Returns the value the user has input, if

wantsInput

is true.

**Returns:** the

Object

the user specified,
if it was one of the objects, or a

String

if it was a value typed into a
field
**See Also:** setSelectionValues(java.lang.Object[])

,

setWantsInput(boolean)

,

setInputValue(java.lang.Object)

- getMaxCharactersPerLineCount

```java
@BeanProperty
(
bound
=false)
public int getMaxCharactersPerLineCount()
```

Returns the maximum number of characters to place on a line in a
message. Default is to return

Integer.MAX_VALUE

.
The value can be
changed by overriding this method in a subclass.

**Returns:** an integer giving the maximum number of characters on a line

- setWantsInput

```java
@BeanProperty
(
preferred
=true,

description
="Flag which allows the user to input a value.")
public void setWantsInput​(boolean newValue)
```

Sets the

wantsInput

property.
If

newValue

is true, an input component
(such as a text field or combo box) whose parent is

parentComponent

is provided to
allow the user to input a value. If

getSelectionValues

returns a non-

null

array, the input value is one of the
objects in that array. Otherwise the input value is whatever
the user inputs.

This is a bound property.

**Parameters:** newValue

- if true, an input component whose parent is

parentComponent

is provided to allow the user to input a value.
**See Also:** setSelectionValues(java.lang.Object[])

,

setInputValue(java.lang.Object)

- getWantsInput

```java
public boolean getWantsInput()
```

Returns the value of the

wantsInput

property.

**Returns:** true if an input component will be provided
**See Also:** setWantsInput(boolean)

- selectInitialValue

```java
public void selectInitialValue()
```

Requests that the initial value be selected, which will set
focus to the initial value. This method
should be invoked after the window containing the option pane
is made visible.

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JOptionPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JOptionPane

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this option pane")
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with this JOptionPane.
For option panes, the

AccessibleContext

takes the form of an

AccessibleJOptionPane

.
A new

AccessibleJOptionPane

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJOptionPane that serves as the
AccessibleContext of this AccessibleJOptionPane

Field Detail

- UNINITIALIZED_VALUE

```java
public static final
Object
UNINITIALIZED_VALUE
```

Indicates that the user has not yet selected a value.

- DEFAULT_OPTION

```java
public static final int DEFAULT_OPTION
```

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

**See Also:** Constant Field Values

- YES_NO_OPTION

```java
public static final int YES_NO_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

- YES_NO_CANCEL_OPTION

```java
public static final int YES_NO_CANCEL_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

- OK_CANCEL_OPTION

```java
public static final int OK_CANCEL_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

- YES_OPTION

```java
public static final int YES_OPTION
```

Return value from class method if YES is chosen.

**See Also:** Constant Field Values

- NO_OPTION

```java
public static final int NO_OPTION
```

Return value from class method if NO is chosen.

**See Also:** Constant Field Values

- CANCEL_OPTION

```java
public static final int CANCEL_OPTION
```

Return value from class method if CANCEL is chosen.

**See Also:** Constant Field Values

- OK_OPTION

```java
public static final int OK_OPTION
```

Return value form class method if OK is chosen.

**See Also:** Constant Field Values

- CLOSED_OPTION

```java
public static final int CLOSED_OPTION
```

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

**See Also:** Constant Field Values

- ERROR_MESSAGE

```java
public static final int ERROR_MESSAGE
```

Used for error messages.

**See Also:** Constant Field Values

- INFORMATION_MESSAGE

```java
public static final int INFORMATION_MESSAGE
```

Used for information messages.

**See Also:** Constant Field Values

- WARNING_MESSAGE

```java
public static final int WARNING_MESSAGE
```

Used for warning messages.

**See Also:** Constant Field Values

- QUESTION_MESSAGE

```java
public static final int QUESTION_MESSAGE
```

Used for questions.

**See Also:** Constant Field Values

- PLAIN_MESSAGE

```java
public static final int PLAIN_MESSAGE
```

No icon is used.

**See Also:** Constant Field Values

- ICON_PROPERTY

```java
public static final
String
ICON_PROPERTY
```

Bound property name for

icon

.

**See Also:** Constant Field Values

- MESSAGE_PROPERTY

```java
public static final
String
MESSAGE_PROPERTY
```

Bound property name for

message

.

**See Also:** Constant Field Values

- VALUE_PROPERTY

```java
public static final
String
VALUE_PROPERTY
```

Bound property name for

value

.

**See Also:** Constant Field Values

- OPTIONS_PROPERTY

```java
public static final
String
OPTIONS_PROPERTY
```

Bound property name for

option

.

**See Also:** Constant Field Values

- INITIAL_VALUE_PROPERTY

```java
public static final
String
INITIAL_VALUE_PROPERTY
```

Bound property name for

initialValue

.

**See Also:** Constant Field Values

- MESSAGE_TYPE_PROPERTY

```java
public static final
String
MESSAGE_TYPE_PROPERTY
```

Bound property name for

type

.

**See Also:** Constant Field Values

- OPTION_TYPE_PROPERTY

```java
public static final
String
OPTION_TYPE_PROPERTY
```

Bound property name for

optionType

.

**See Also:** Constant Field Values

- SELECTION_VALUES_PROPERTY

```java
public static final
String
SELECTION_VALUES_PROPERTY
```

Bound property name for

selectionValues

.

**See Also:** Constant Field Values

- INITIAL_SELECTION_VALUE_PROPERTY

```java
public static final
String
INITIAL_SELECTION_VALUE_PROPERTY
```

Bound property name for

initialSelectionValue

.

**See Also:** Constant Field Values

- INPUT_VALUE_PROPERTY

```java
public static final
String
INPUT_VALUE_PROPERTY
```

Bound property name for

inputValue

.

**See Also:** Constant Field Values

- WANTS_INPUT_PROPERTY

```java
public static final
String
WANTS_INPUT_PROPERTY
```

Bound property name for

wantsInput

.

**See Also:** Constant Field Values

- icon

```java
protected transient
Icon
icon
```

Icon used in pane.

- message

```java
protected transient
Object
message
```

Message to display.

- options

```java
protected transient
Object
[] options
```

Options to display to the user.

- initialValue

```java
protected transient
Object
initialValue
```

Value that should be initially selected in

options

.

- messageType

```java
protected int messageType
```

Message type.

- optionType

```java
protected int optionType
```

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

- value

```java
protected transient
Object
value
```

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

- selectionValues

```java
protected transient
Object
[] selectionValues
```

Array of values the user can choose from. Look and feel will
provide the UI component to choose this from.

- inputValue

```java
protected transient
Object
inputValue
```

Value the user has input.

- initialSelectionValue

```java
protected transient
Object
initialSelectionValue
```

Initial value to select in

selectionValues

.

- wantsInput

```java
protected boolean wantsInput
```

If true, a UI widget will be provided to the user to get input.

---

#### Field Detail

UNINITIALIZED_VALUE

```java
public static final
Object
UNINITIALIZED_VALUE
```

Indicates that the user has not yet selected a value.

---

#### UNINITIALIZED_VALUE

public static final

Object

UNINITIALIZED_VALUE

Indicates that the user has not yet selected a value.

DEFAULT_OPTION

```java
public static final int DEFAULT_OPTION
```

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

**See Also:** Constant Field Values

---

#### DEFAULT_OPTION

public static final int DEFAULT_OPTION

Type meaning Look and Feel should not supply any options -- only
use the options from the

JOptionPane

.

YES_NO_OPTION

```java
public static final int YES_NO_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

---

#### YES_NO_OPTION

public static final int YES_NO_OPTION

Type used for

showConfirmDialog

.

YES_NO_CANCEL_OPTION

```java
public static final int YES_NO_CANCEL_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

---

#### YES_NO_CANCEL_OPTION

public static final int YES_NO_CANCEL_OPTION

Type used for

showConfirmDialog

.

OK_CANCEL_OPTION

```java
public static final int OK_CANCEL_OPTION
```

Type used for

showConfirmDialog

.

**See Also:** Constant Field Values

---

#### OK_CANCEL_OPTION

public static final int OK_CANCEL_OPTION

Type used for

showConfirmDialog

.

YES_OPTION

```java
public static final int YES_OPTION
```

Return value from class method if YES is chosen.

**See Also:** Constant Field Values

---

#### YES_OPTION

public static final int YES_OPTION

Return value from class method if YES is chosen.

NO_OPTION

```java
public static final int NO_OPTION
```

Return value from class method if NO is chosen.

**See Also:** Constant Field Values

---

#### NO_OPTION

public static final int NO_OPTION

Return value from class method if NO is chosen.

CANCEL_OPTION

```java
public static final int CANCEL_OPTION
```

Return value from class method if CANCEL is chosen.

**See Also:** Constant Field Values

---

#### CANCEL_OPTION

public static final int CANCEL_OPTION

Return value from class method if CANCEL is chosen.

OK_OPTION

```java
public static final int OK_OPTION
```

Return value form class method if OK is chosen.

**See Also:** Constant Field Values

---

#### OK_OPTION

public static final int OK_OPTION

Return value form class method if OK is chosen.

CLOSED_OPTION

```java
public static final int CLOSED_OPTION
```

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

**See Also:** Constant Field Values

---

#### CLOSED_OPTION

public static final int CLOSED_OPTION

Return value from class method if user closes window without selecting
anything, more than likely this should be treated as either a

CANCEL_OPTION

or

NO_OPTION

.

ERROR_MESSAGE

```java
public static final int ERROR_MESSAGE
```

Used for error messages.

**See Also:** Constant Field Values

---

#### ERROR_MESSAGE

public static final int ERROR_MESSAGE

Used for error messages.

INFORMATION_MESSAGE

```java
public static final int INFORMATION_MESSAGE
```

Used for information messages.

**See Also:** Constant Field Values

---

#### INFORMATION_MESSAGE

public static final int INFORMATION_MESSAGE

Used for information messages.

WARNING_MESSAGE

```java
public static final int WARNING_MESSAGE
```

Used for warning messages.

**See Also:** Constant Field Values

---

#### WARNING_MESSAGE

public static final int WARNING_MESSAGE

Used for warning messages.

QUESTION_MESSAGE

```java
public static final int QUESTION_MESSAGE
```

Used for questions.

**See Also:** Constant Field Values

---

#### QUESTION_MESSAGE

public static final int QUESTION_MESSAGE

Used for questions.

PLAIN_MESSAGE

```java
public static final int PLAIN_MESSAGE
```

No icon is used.

**See Also:** Constant Field Values

---

#### PLAIN_MESSAGE

public static final int PLAIN_MESSAGE

No icon is used.

ICON_PROPERTY

```java
public static final
String
ICON_PROPERTY
```

Bound property name for

icon

.

**See Also:** Constant Field Values

---

#### ICON_PROPERTY

public static final

String

ICON_PROPERTY

Bound property name for

icon

.

MESSAGE_PROPERTY

```java
public static final
String
MESSAGE_PROPERTY
```

Bound property name for

message

.

**See Also:** Constant Field Values

---

#### MESSAGE_PROPERTY

public static final

String

MESSAGE_PROPERTY

Bound property name for

message

.

VALUE_PROPERTY

```java
public static final
String
VALUE_PROPERTY
```

Bound property name for

value

.

**See Also:** Constant Field Values

---

#### VALUE_PROPERTY

public static final

String

VALUE_PROPERTY

Bound property name for

value

.

OPTIONS_PROPERTY

```java
public static final
String
OPTIONS_PROPERTY
```

Bound property name for

option

.

**See Also:** Constant Field Values

---

#### OPTIONS_PROPERTY

public static final

String

OPTIONS_PROPERTY

Bound property name for

option

.

INITIAL_VALUE_PROPERTY

```java
public static final
String
INITIAL_VALUE_PROPERTY
```

Bound property name for

initialValue

.

**See Also:** Constant Field Values

---

#### INITIAL_VALUE_PROPERTY

public static final

String

INITIAL_VALUE_PROPERTY

Bound property name for

initialValue

.

MESSAGE_TYPE_PROPERTY

```java
public static final
String
MESSAGE_TYPE_PROPERTY
```

Bound property name for

type

.

**See Also:** Constant Field Values

---

#### MESSAGE_TYPE_PROPERTY

public static final

String

MESSAGE_TYPE_PROPERTY

Bound property name for

type

.

OPTION_TYPE_PROPERTY

```java
public static final
String
OPTION_TYPE_PROPERTY
```

Bound property name for

optionType

.

**See Also:** Constant Field Values

---

#### OPTION_TYPE_PROPERTY

public static final

String

OPTION_TYPE_PROPERTY

Bound property name for

optionType

.

SELECTION_VALUES_PROPERTY

```java
public static final
String
SELECTION_VALUES_PROPERTY
```

Bound property name for

selectionValues

.

**See Also:** Constant Field Values

---

#### SELECTION_VALUES_PROPERTY

public static final

String

SELECTION_VALUES_PROPERTY

Bound property name for

selectionValues

.

INITIAL_SELECTION_VALUE_PROPERTY

```java
public static final
String
INITIAL_SELECTION_VALUE_PROPERTY
```

Bound property name for

initialSelectionValue

.

**See Also:** Constant Field Values

---

#### INITIAL_SELECTION_VALUE_PROPERTY

public static final

String

INITIAL_SELECTION_VALUE_PROPERTY

Bound property name for

initialSelectionValue

.

INPUT_VALUE_PROPERTY

```java
public static final
String
INPUT_VALUE_PROPERTY
```

Bound property name for

inputValue

.

**See Also:** Constant Field Values

---

#### INPUT_VALUE_PROPERTY

public static final

String

INPUT_VALUE_PROPERTY

Bound property name for

inputValue

.

WANTS_INPUT_PROPERTY

```java
public static final
String
WANTS_INPUT_PROPERTY
```

Bound property name for

wantsInput

.

**See Also:** Constant Field Values

---

#### WANTS_INPUT_PROPERTY

public static final

String

WANTS_INPUT_PROPERTY

Bound property name for

wantsInput

.

icon

```java
protected transient
Icon
icon
```

Icon used in pane.

---

#### icon

protected transient

Icon

icon

Icon used in pane.

message

```java
protected transient
Object
message
```

Message to display.

---

#### message

protected transient

Object

message

Message to display.

options

```java
protected transient
Object
[] options
```

Options to display to the user.

---

#### options

protected transient

Object

[] options

Options to display to the user.

initialValue

```java
protected transient
Object
initialValue
```

Value that should be initially selected in

options

.

---

#### initialValue

protected transient

Object

initialValue

Value that should be initially selected in

options

.

messageType

```java
protected int messageType
```

Message type.

---

#### messageType

protected int messageType

Message type.

optionType

```java
protected int optionType
```

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

---

#### optionType

protected int optionType

Option type, one of

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

.

value

```java
protected transient
Object
value
```

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

---

#### value

protected transient

Object

value

Currently selected value, will be a valid option, or

UNINITIALIZED_VALUE

or

null

.

selectionValues

```java
protected transient
Object
[] selectionValues
```

Array of values the user can choose from. Look and feel will
provide the UI component to choose this from.

---

#### selectionValues

protected transient

Object

[] selectionValues

Array of values the user can choose from. Look and feel will
provide the UI component to choose this from.

inputValue

```java
protected transient
Object
inputValue
```

Value the user has input.

---

#### inputValue

protected transient

Object

inputValue

Value the user has input.

initialSelectionValue

```java
protected transient
Object
initialSelectionValue
```

Initial value to select in

selectionValues

.

---

#### initialSelectionValue

protected transient

Object

initialSelectionValue

Initial value to select in

selectionValues

.

wantsInput

```java
protected boolean wantsInput
```

If true, a UI widget will be provided to the user to get input.

---

#### wantsInput

protected boolean wantsInput

If true, a UI widget will be provided to the user to get input.

Constructor Detail

- JOptionPane

```java
public JOptionPane()
```

Creates a

JOptionPane

with a test message.

- JOptionPane

```java
public JOptionPane​(
Object
message)
```

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

**Parameters:** message

- the

Object

to display

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the

Icon

image to display

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.
None of the options is initially selected.

The options objects should contain either instances of

Component

s, (which are added directly) or

Strings

(which are wrapped in a

JButton

).
If you provide

Component

s, you must ensure that when the

Component

is clicked it messages

setValue

in the created

JOptionPane

.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the

Icon

image to display
**Parameters:** options

- the choices the user can select

- JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options,

Object
initialValue)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the Icon image to display
**Parameters:** options

- the choices the user can select
**Parameters:** initialValue

- the choice that is initially selected; if

null

, then nothing will be initially selected;
only meaningful if

options

is used

---

#### Constructor Detail

JOptionPane

```java
public JOptionPane()
```

Creates a

JOptionPane

with a test message.

---

#### JOptionPane

public JOptionPane()

Creates a

JOptionPane

with a test message.

JOptionPane

```java
public JOptionPane​(
Object
message)
```

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

**Parameters:** message

- the

Object

to display

---

#### JOptionPane

public JOptionPane​(

Object

message)

Creates a instance of

JOptionPane

to display a
message using the
plain-message message type and the default options delivered by
the UI.

JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

---

#### JOptionPane

public JOptionPane​(

Object

message,
int messageType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and the default options,

JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION

---

#### JOptionPane

public JOptionPane​(

Object

message,
int messageType,
int optionType)

Creates an instance of

JOptionPane

to display a message
with the specified message type and options.

JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the

Icon

image to display

---

#### JOptionPane

public JOptionPane​(

Object

message,
int messageType,
int optionType,

Icon

icon)

Creates an instance of

JOptionPane

to display a message
with the specified message type, options, and icon.

JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.
None of the options is initially selected.

The options objects should contain either instances of

Component

s, (which are added directly) or

Strings

(which are wrapped in a

JButton

).
If you provide

Component

s, you must ensure that when the

Component

is clicked it messages

setValue

in the created

JOptionPane

.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the

Icon

image to display
**Parameters:** options

- the choices the user can select

---

#### JOptionPane

public JOptionPane​(

Object

message,
int messageType,
int optionType,

Icon

icon,

Object

[] options)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options.
None of the options is initially selected.

The options objects should contain either instances of

Component

s, (which are added directly) or

Strings

(which are wrapped in a

JButton

).
If you provide

Component

s, you must ensure that when the

Component

is clicked it messages

setValue

in the created

JOptionPane

.

The options objects should contain either instances of

Component

s, (which are added directly) or

Strings

(which are wrapped in a

JButton

).
If you provide

Component

s, you must ensure that when the

Component

is clicked it messages

setValue

in the created

JOptionPane

.

JOptionPane

```java
public JOptionPane​(
Object
message,
int messageType,
int optionType,

Icon
icon,

Object
[] options,

Object
initialValue)
```

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

**Parameters:** message

- the

Object

to display
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** optionType

- the options to display in the pane:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,

OK_CANCEL_OPTION
**Parameters:** icon

- the Icon image to display
**Parameters:** options

- the choices the user can select
**Parameters:** initialValue

- the choice that is initially selected; if

null

, then nothing will be initially selected;
only meaningful if

options

is used

---

#### JOptionPane

public JOptionPane​(

Object

message,
int messageType,
int optionType,

Icon

icon,

Object

[] options,

Object

initialValue)

Creates an instance of

JOptionPane

to display a message
with the specified message type, icon, and options, with the
initially-selected option specified.

Method Detail

- showInputDialog

```java
public static
String
showInputDialog​(
Object
message)
throws
HeadlessException
```

Shows a question-message dialog requesting input from the user. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:** message

- the

Object

to display
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showInputDialog

```java
public static
String
showInputDialog​(
Object
message,

Object
initialSelectionValue)
```

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:** message

- the

Object

to display
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input
**Since:** 1.4

- showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

Object
initialSelectionValue)
```

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

. The input value will be
initialized to

initialSelectionValue

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input
**Since:** 1.4

- showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException
```

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the dialog
title bar
**Parameters:** messageType

- the type of message that is to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showInputDialog

```java
public static
Object
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)
throws
HeadlessException
```

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified. The user will able to choose from

selectionValues

, where

null

implies the
user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the
dialog title bar
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the

Icon

image to display
**Parameters:** selectionValues

- an array of

Object

s that
gives the possible selections
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input, or

null

meaning the user
canceled the input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Brings up an information-message dialog titled "Message".

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException
```

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)
throws
HeadlessException
```

Brings up a dialog displaying a message, specifying all parameters.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Returns:** an integer indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)
throws
HeadlessException
```

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Returns:** an int indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)
throws
HeadlessException
```

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used.
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** an integer indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)
throws
HeadlessException
```

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the Object to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an int designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Returns:** an int indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- showOptionDialog

```java
public static int showOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)
throws
HeadlessException
```

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are
supplied by the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

, or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available on the
dialog:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Parameters:** options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are
rendered using their

toString

methods;
if this parameter is

null

,
the options are determined by the Look and Feel
**Parameters:** initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null
**Returns:** an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed
the dialog
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- createDialog

```java
public
JDialog
createDialog​(
Component
parentComponent,

String
title)
throws
HeadlessException
```

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

title

is the title of the returned dialog.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:** parentComponent

- determines the frame in which the dialog
is displayed; if the

parentComponent

has
no

Frame

, a default

Frame

is used
**Parameters:** title

- the title string for the dialog
**Returns:** a new

JDialog

containing this instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

- createDialog

```java
public
JDialog
createDialog​(
String
title)
throws
HeadlessException
```

Creates and returns a new parentless

JDialog

with the specified title.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:** title

- the title string for the dialog
**Returns:** a new

JDialog

containing this instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

- showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message)
```

Brings up an internal confirmation dialog panel. The dialog
is a information-message dialog titled "Message".

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display

- showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
```

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

- showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)
```

Brings up an internal dialog panel displaying a message,
specifying all parameters.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message)
```

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Returns:** an integer indicating the option selected by the user

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)
```

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects
are converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION
**Returns:** an integer indicating the option selected by the user

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)
```

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** an integer indicating the option selected by the user

- showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)
```

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the parentComponent has no Frame, a
default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

.
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Returns:** an integer indicating the option selected by the user

- showInternalOptionDialog

```java
public static int showInternalOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)
```

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are supplied by the Look and Feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string. Other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Parameters:** options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are rendered using their

toString

methods; if this parameter is

null

,
the options are determined by the Look and Feel
**Parameters:** initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null
**Returns:** an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed the Dialog

- showInternalInputDialog

```java
public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message)
```

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

. The dialog
is displayed in the

Component

's frame,
and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Returns:** user's input

- showInternalInputDialog

```java
public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
```

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the
dialog title bar
**Parameters:** messageType

- the type of message that is to be displayed:
ERROR_MESSAGE, INFORMATION_MESSAGE, WARNING_MESSAGE,
QUESTION_MESSAGE, or PLAIN_MESSAGE
**Returns:** user's input

- showInternalInputDialog

```java
public static
Object
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)
```

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified. The user will able to choose from

selectionValues

, where

null

implies the user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the dialog
title bar
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE
**Parameters:** icon

- the

Icon

image to display
**Parameters:** selectionValues

- an array of

Objects

that
gives the possible selections
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input, or

null

meaning the user
canceled the input

- createInternalFrame

```java
public
JInternalFrame
createInternalFrame​(
Component
parentComponent,

String
title)
```

Creates and returns an instance of

JInternalFrame

.
The internal frame is created with the specified title,
and wrapping the

JOptionPane

.
The returned

JInternalFrame

is
added to the

JDesktopPane

ancestor of

parentComponent

, or components
parent if one its ancestors isn't a

JDesktopPane

,
or if

parentComponent

doesn't have a parent then a

RuntimeException

is thrown.

**Parameters:** parentComponent

- the parent

Component

for
the internal frame
**Parameters:** title

- the

String

to display in the
frame's title bar
**Returns:** a

JInternalFrame

containing a

JOptionPane
**Throws:** RuntimeException

- if

parentComponent

does
not have a valid parent

- getFrameForComponent

```java
public static
Frame
getFrameForComponent​(
Component
parentComponent)
throws
HeadlessException
```

Returns the specified component's

Frame

.

**Parameters:** parentComponent

- the

Component

to check for a

Frame
**Returns:** the

Frame

that contains the component,
or

getRootFrame

if the component is

null

,
or does not have a valid

Frame

parent
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** getRootFrame()

,

GraphicsEnvironment.isHeadless()

- getDesktopPaneForComponent

```java
public static
JDesktopPane
getDesktopPaneForComponent​(
Component
parentComponent)
```

Returns the specified component's desktop pane.

**Parameters:** parentComponent

- the

Component

to check for a
desktop
**Returns:** the

JDesktopPane

that contains the component,
or

null

if the component is

null

or does not have an ancestor that is a

JInternalFrame

- setRootFrame

```java
public static void setRootFrame​(
Frame
newRootFrame)
```

Sets the frame to use for class methods in which a frame is
not provided.

Note:

It is recommended that rather than using this method you supply a valid parent.

**Parameters:** newRootFrame

- the default

Frame

to use

- getRootFrame

```java
public static
Frame
getRootFrame()
throws
HeadlessException
```

Returns the

Frame

to use for the class methods in
which a frame is not provided.

**Returns:** the default

Frame

to use
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** setRootFrame(java.awt.Frame)

,

GraphicsEnvironment.isHeadless()

- setUI

```java
@BeanProperty
(
hidden
=true,

description
="The UI object that implements the optionpane\'s LookAndFeel")
public void setUI​(
OptionPaneUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the

OptionPaneUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- getUI

```java
public
OptionPaneUI
getUI()
```

Returns the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

OptionPaneUI

object

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "OptionPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setMessage

```java
@BeanProperty
(
preferred
=true,

description
="The optionpane\'s message object.")
public void setMessage​(
Object
newMessage)
```

Sets the option pane's message-object.

**Parameters:** newMessage

- the

Object

to display
**See Also:** getMessage()

- getMessage

```java
public
Object
getMessage()
```

Returns the message-object this pane displays.

**Returns:** the

Object

that is displayed
**See Also:** setMessage(java.lang.Object)

- setIcon

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s type icon.")
public void setIcon​(
Icon
newIcon)
```

Sets the icon to display. If non-

null

, the look and feel
does not provide an icon.

**Parameters:** newIcon

- the

Icon

to display
**See Also:** getIcon()

- getIcon

```java
public
Icon
getIcon()
```

Returns the icon this pane displays.

**Returns:** the

Icon

that is displayed
**See Also:** setIcon(javax.swing.Icon)

- setValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s value object.")
public void setValue​(
Object
newValue)
```

Sets the value the user has chosen.

**Parameters:** newValue

- the chosen value
**See Also:** getValue()

- getValue

```java
public
Object
getValue()
```

Returns the value the user has selected.

UNINITIALIZED_VALUE

implies the user has not yet made a choice,

null

means the
user closed the window with out choosing anything. Otherwise
the returned value will be one of the options defined in this
object.

**Returns:** the

Object

chosen by the user,

UNINITIALIZED_VALUE

if the user has not yet made a choice, or

null

if
the user closed the window without making a choice
**See Also:** setValue(java.lang.Object)

- setOptions

```java
@BeanProperty
(
description
="The option pane\'s options objects.")
public void setOptions​(
Object
[] newOptions)
```

Sets the options this pane displays. If an element in

newOptions

is a

Component

it is added directly to the pane,
otherwise a button is created for the element.

**Parameters:** newOptions

- an array of

Objects

that create the
buttons the user can click on, or arbitrary

Components

to add to the pane
**See Also:** getOptions()

- getOptions

```java
public
Object
[] getOptions()
```

Returns the choices the user can make.

**Returns:** the array of

Objects

that give the user's choices
**See Also:** setOptions(java.lang.Object[])

- setInitialValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s initial value object.")
public void setInitialValue​(
Object
newInitialValue)
```

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

**Parameters:** newInitialValue

- the

Object

that gets the initial
keyboard focus
**See Also:** getInitialValue()

- getInitialValue

```java
public
Object
getInitialValue()
```

Returns the initial value.

**Returns:** the

Object

that gets the initial keyboard focus
**See Also:** setInitialValue(java.lang.Object)

- setMessageType

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s message type.")
public void setMessageType​(int newType)
```

Sets the option pane's message type.
The message type is used by the Look and Feel to determine the
icon to display (if not supplied) as well as potentially how to
lay out the

parentComponent

.

**Parameters:** newType

- an integer specifying the kind of message to display:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE
**Throws:** RuntimeException

- if

newType

is not one of the
legal values listed above
**See Also:** getMessageType()

- getMessageType

```java
public int getMessageType()
```

Returns the message type.

**Returns:** an integer specifying the message type
**See Also:** setMessageType(int)

- setOptionType

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s option type.")
public void setOptionType​(int newType)
```

Sets the options to display.
The option type is used by the Look and Feel to
determine what buttons to show (unless options are supplied).

**Parameters:** newType

- an integer specifying the options the L&F is to display:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Throws:** RuntimeException

- if

newType

is not one of
the legal values listed above
**See Also:** getOptionType()

,

setOptions(java.lang.Object[])

- getOptionType

```java
public int getOptionType()
```

Returns the type of options that are displayed.

**Returns:** an integer specifying the user-selectable options
**See Also:** setOptionType(int)

- setSelectionValues

```java
@BeanProperty
(
description
="The option pane\'s selection values.")
public void setSelectionValues​(
Object
[] newValues)
```

Sets the input selection values for a pane that provides the user
with a list of items to choose from. (The UI provides a widget
for choosing one of the values.) A

null

value
implies the user can input whatever they wish, usually by means
of a

JTextField

.

Sets

wantsInput

to true. Use

setInitialSelectionValue

to specify the initially-chosen
value. After the pane as been enabled,

inputValue

is
set to the value the user has selected.

**Parameters:** newValues

- an array of

Objects

the user to be
displayed
(usually in a list or combo-box) from which
the user can make a selection
**See Also:** setWantsInput(boolean)

,

setInitialSelectionValue(java.lang.Object)

,

getSelectionValues()

- getSelectionValues

```java
public
Object
[] getSelectionValues()
```

Returns the input selection values.

**Returns:** the array of

Objects

the user can select
**See Also:** setSelectionValues(java.lang.Object[])

- setInitialSelectionValue

```java
@BeanProperty
(
description
="The option pane\'s initial selection value object.")
public void setInitialSelectionValue​(
Object
newValue)
```

Sets the input value that is initially displayed as selected to the user.
Only used if

wantsInput

is true.

**Parameters:** newValue

- the initially selected value
**See Also:** setSelectionValues(java.lang.Object[])

,

getInitialSelectionValue()

- getInitialSelectionValue

```java
public
Object
getInitialSelectionValue()
```

Returns the input value that is displayed as initially selected to the user.

**Returns:** the initially selected value
**See Also:** setInitialSelectionValue(java.lang.Object)

,

setSelectionValues(java.lang.Object[])

- setInputValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s input value object.")
public void setInputValue​(
Object
newValue)
```

Sets the input value that was selected or input by the user.
Only used if

wantsInput

is true. Note that this method
is invoked internally by the option pane (in response to user action)
and should generally not be called by client programs. To set the
input value initially displayed as selected to the user, use

setInitialSelectionValue

.

**Parameters:** newValue

- the

Object

used to set the
value that the user specified (usually in a text field)
**See Also:** setSelectionValues(java.lang.Object[])

,

setInitialSelectionValue(java.lang.Object)

,

setWantsInput(boolean)

,

getInputValue()

- getInputValue

```java
public
Object
getInputValue()
```

Returns the value the user has input, if

wantsInput

is true.

**Returns:** the

Object

the user specified,
if it was one of the objects, or a

String

if it was a value typed into a
field
**See Also:** setSelectionValues(java.lang.Object[])

,

setWantsInput(boolean)

,

setInputValue(java.lang.Object)

- getMaxCharactersPerLineCount

```java
@BeanProperty
(
bound
=false)
public int getMaxCharactersPerLineCount()
```

Returns the maximum number of characters to place on a line in a
message. Default is to return

Integer.MAX_VALUE

.
The value can be
changed by overriding this method in a subclass.

**Returns:** an integer giving the maximum number of characters on a line

- setWantsInput

```java
@BeanProperty
(
preferred
=true,

description
="Flag which allows the user to input a value.")
public void setWantsInput​(boolean newValue)
```

Sets the

wantsInput

property.
If

newValue

is true, an input component
(such as a text field or combo box) whose parent is

parentComponent

is provided to
allow the user to input a value. If

getSelectionValues

returns a non-

null

array, the input value is one of the
objects in that array. Otherwise the input value is whatever
the user inputs.

This is a bound property.

**Parameters:** newValue

- if true, an input component whose parent is

parentComponent

is provided to allow the user to input a value.
**See Also:** setSelectionValues(java.lang.Object[])

,

setInputValue(java.lang.Object)

- getWantsInput

```java
public boolean getWantsInput()
```

Returns the value of the

wantsInput

property.

**Returns:** true if an input component will be provided
**See Also:** setWantsInput(boolean)

- selectInitialValue

```java
public void selectInitialValue()
```

Requests that the initial value be selected, which will set
focus to the initial value. This method
should be invoked after the window containing the option pane
is made visible.

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JOptionPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JOptionPane

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this option pane")
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with this JOptionPane.
For option panes, the

AccessibleContext

takes the form of an

AccessibleJOptionPane

.
A new

AccessibleJOptionPane

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJOptionPane that serves as the
AccessibleContext of this AccessibleJOptionPane

---

#### Method Detail

showInputDialog

```java
public static
String
showInputDialog​(
Object
message)
throws
HeadlessException
```

Shows a question-message dialog requesting input from the user. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:** message

- the

Object

to display
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showInputDialog

public static

String

showInputDialog​(

Object

message)
throws

HeadlessException

Shows a question-message dialog requesting input from the user. The
dialog uses the default frame, which usually means it is centered on
the screen.

showInputDialog

```java
public static
String
showInputDialog​(
Object
message,

Object
initialSelectionValue)
```

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

. The
dialog uses the default frame, which usually means it is centered on
the screen.

**Parameters:** message

- the

Object

to display
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input
**Since:** 1.4

---

#### showInputDialog

public static

String

showInputDialog​(

Object

message,

Object

initialSelectionValue)

Shows a question-message dialog requesting input from the user, with
the input value initialized to

initialSelectionValue

. The
dialog uses the default frame, which usually means it is centered on
the screen.

showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showInputDialog

public static

String

showInputDialog​(

Component

parentComponent,

Object

message)
throws

HeadlessException

Shows a question-message dialog requesting input from the user
parented to

parentComponent

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

Object
initialSelectionValue)
```

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

. The input value will be
initialized to

initialSelectionValue

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input
**Since:** 1.4

---

#### showInputDialog

public static

String

showInputDialog​(

Component

parentComponent,

Object

message,

Object

initialSelectionValue)

Shows a question-message dialog requesting input from the user and
parented to

parentComponent

. The input value will be
initialized to

initialSelectionValue

.
The dialog is displayed on top of the

Component

's
frame, and is usually positioned below the

Component

.

showInputDialog

```java
public static
String
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException
```

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the dialog
title bar
**Parameters:** messageType

- the type of message that is to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** user's input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showInputDialog

public static

String

showInputDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType)
throws

HeadlessException

Shows a dialog requesting input from the user parented to

parentComponent

with the dialog having the title

title

and message type

messageType

.

showInputDialog

```java
public static
Object
showInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)
throws
HeadlessException
```

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified. The user will able to choose from

selectionValues

, where

null

implies the
user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:** parentComponent

- the parent

Component

for the
dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the
dialog title bar
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the

Icon

image to display
**Parameters:** selectionValues

- an array of

Object

s that
gives the possible selections
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input, or

null

meaning the user
canceled the input
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showInputDialog

public static

Object

showInputDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon,

Object

[] selectionValues,

Object

initialSelectionValue)
throws

HeadlessException

Prompts the user for input in a blocking dialog where the
initial selection, possible selections, and all other options can
be specified. The user will able to choose from

selectionValues

, where

null

implies the
user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Brings up an information-message dialog titled "Message".

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showMessageDialog

public static void showMessageDialog​(

Component

parentComponent,

Object

message)
throws

HeadlessException

Brings up an information-message dialog titled "Message".

showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
throws
HeadlessException
```

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showMessageDialog

public static void showMessageDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType)
throws

HeadlessException

Brings up a dialog that displays a message using a default
icon determined by the

messageType

parameter.

showMessageDialog

```java
public static void showMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)
throws
HeadlessException
```

Brings up a dialog displaying a message, specifying all parameters.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showMessageDialog

public static void showMessageDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon)
throws

HeadlessException

Brings up a dialog displaying a message, specifying all parameters.

showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message)
throws
HeadlessException
```

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Returns:** an integer indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showConfirmDialog

public static int showConfirmDialog​(

Component

parentComponent,

Object

message)
throws

HeadlessException

Brings up a dialog with the options

Yes

,

No

and

Cancel

; with the
title,

Select an Option

.

showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)
throws
HeadlessException
```

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Returns:** an int indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showConfirmDialog

public static int showConfirmDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType)
throws

HeadlessException

Brings up a dialog where the number of choices is determined
by the

optionType

parameter.

showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)
throws
HeadlessException
```

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used.
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** an integer indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showConfirmDialog

public static int showConfirmDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType)
throws

HeadlessException

Brings up a dialog where the number of choices is determined
by the

optionType

parameter, where the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

showConfirmDialog

```java
public static int showConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)
throws
HeadlessException
```

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the
dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the Object to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an int designating the options available on the dialog:

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an int designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Returns:** an int indicating the option selected by the user
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showConfirmDialog

public static int showConfirmDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon)
throws

HeadlessException

Brings up a dialog with a specified icon, where the number of
choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

showOptionDialog

```java
public static int showOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)
throws
HeadlessException
```

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are
supplied by the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

, or if the

parentComponent

has no

Frame

, a
default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available on the
dialog:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Parameters:** options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are
rendered using their

toString

methods;
if this parameter is

null

,
the options are determined by the Look and Feel
**Parameters:** initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null
**Returns:** an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed
the dialog
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### showOptionDialog

public static int showOptionDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon,

Object

[] options,

Object

initialValue)
throws

HeadlessException

Brings up a dialog with a specified icon, where the initial
choice is determined by the

initialValue

parameter and
the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are
supplied by the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

If

optionType

is

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are
supplied by the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

createDialog

```java
public
JDialog
createDialog​(
Component
parentComponent,

String
title)
throws
HeadlessException
```

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

title

is the title of the returned dialog.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:** parentComponent

- determines the frame in which the dialog
is displayed; if the

parentComponent

has
no

Frame

, a default

Frame

is used
**Parameters:** title

- the title string for the dialog
**Returns:** a new

JDialog

containing this instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** GraphicsEnvironment.isHeadless()

---

#### createDialog

public

JDialog

createDialog​(

Component

parentComponent,

String

title)
throws

HeadlessException

Creates and returns a new

JDialog

wrapping

this

centered on the

parentComponent

in the

parentComponent

's frame.

title

is the title of the returned dialog.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

createDialog

```java
public
JDialog
createDialog​(
String
title)
throws
HeadlessException
```

Creates and returns a new parentless

JDialog

with the specified title.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

**Parameters:** title

- the title string for the dialog
**Returns:** a new

JDialog

containing this instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.6
**See Also:** GraphicsEnvironment.isHeadless()

---

#### createDialog

public

JDialog

createDialog​(

String

title)
throws

HeadlessException

Creates and returns a new parentless

JDialog

with the specified title.
The returned

JDialog

will not be resizable by the
user, however programs can invoke

setResizable

on
the

JDialog

instance to change this property.
The returned

JDialog

will be set up such that
once it is closed, or the user clicks on one of the buttons,
the optionpane's value property will be set accordingly and
the dialog will be closed. Each time the dialog is made visible,
it will reset the option pane's value property to

JOptionPane.UNINITIALIZED_VALUE

to ensure the
user's subsequent action closes the dialog properly.

showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message)
```

Brings up an internal confirmation dialog panel. The dialog
is a information-message dialog titled "Message".

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display

---

#### showInternalMessageDialog

public static void showInternalMessageDialog​(

Component

parentComponent,

Object

message)

Brings up an internal confirmation dialog panel. The dialog
is a information-message dialog titled "Message".

showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
```

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE

---

#### showInternalMessageDialog

public static void showInternalMessageDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Brings up an internal dialog panel that displays a message
using a default icon determined by the

messageType

parameter.

showInternalMessageDialog

```java
public static void showInternalMessageDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon)
```

Brings up an internal dialog panel displaying a message,
specifying all parameters.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the title string for the dialog
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- an icon to display in the dialog that helps the user
identify the kind of message that is being displayed

---

#### showInternalMessageDialog

public static void showInternalMessageDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon)

Brings up an internal dialog panel displaying a message,
specifying all parameters.

showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message)
```

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the

Object

to display
**Returns:** an integer indicating the option selected by the user

---

#### showInternalConfirmDialog

public static int showInternalConfirmDialog​(

Component

parentComponent,

Object

message)

Brings up an internal dialog panel with the options

Yes

,

No

and

Cancel

; with the title,

Select an Option

.

showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType)
```

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects
are converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION
**Returns:** an integer indicating the option selected by the user

---

#### showInternalConfirmDialog

public static int showInternalConfirmDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType)

Brings up a internal dialog panel where the number of choices
is determined by the

optionType

parameter.

showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType)
```

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

**Parameters:** parentComponent

- determines the

Frame

in
which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options
available on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Returns:** an integer indicating the option selected by the user

---

#### showInternalConfirmDialog

public static int showInternalConfirmDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType)

Brings up an internal dialog panel where the number of choices
is determined by the

optionType

parameter, where
the

messageType

parameter determines the icon to display.
The

messageType

parameter is primarily used to supply
a default icon from the Look and Feel.

showInternalConfirmDialog

```java
public static int showInternalConfirmDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon)
```

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the parentComponent has no Frame, a
default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string; other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

.
**Parameters:** messageType

- an integer designating the kind of message this is,
primarily used to determine the icon from the pluggable
Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Returns:** an integer indicating the option selected by the user

---

#### showInternalConfirmDialog

public static int showInternalConfirmDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon)

Brings up an internal dialog panel with a specified icon, where
the number of choices is determined by the

optionType

parameter.
The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

showInternalOptionDialog

```java
public static int showInternalOptionDialog​(
Component
parentComponent,

Object
message,

String
title,
int optionType,
int messageType,

Icon
icon,

Object
[] options,

Object
initialValue)
```

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are supplied by the Look and Feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

**Parameters:** parentComponent

- determines the

Frame

in which the dialog is displayed; if

null

,
or if the

parentComponent

has no

Frame

, a default

Frame

is used
**Parameters:** message

- the object to display in the dialog; a

Component

object is rendered as a

Component

; a

String

object is rendered as a string. Other objects are
converted to a

String

using the

toString

method
**Parameters:** title

- the title string for the dialog
**Parameters:** optionType

- an integer designating the options available
on the dialog:

YES_NO_OPTION

,
or

YES_NO_CANCEL_OPTION
**Parameters:** messageType

- an integer designating the kind of message this is;
primarily used to determine the icon from the
pluggable Look and Feel:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

,
or

PLAIN_MESSAGE
**Parameters:** icon

- the icon to display in the dialog
**Parameters:** options

- an array of objects indicating the possible choices
the user can make; if the objects are components, they
are rendered properly; non-

String

objects are rendered using their

toString

methods; if this parameter is

null

,
the options are determined by the Look and Feel
**Parameters:** initialValue

- the object that represents the default selection
for the dialog; only meaningful if

options

is used; can be

null
**Returns:** an integer indicating the option chosen by the user,
or

CLOSED_OPTION

if the user closed the Dialog

---

#### showInternalOptionDialog

public static int showInternalOptionDialog​(

Component

parentComponent,

Object

message,

String

title,
int optionType,
int messageType,

Icon

icon,

Object

[] options,

Object

initialValue)

Brings up an internal dialog panel with a specified icon, where
the initial choice is determined by the

initialValue

parameter and the number of choices is determined by the

optionType

parameter.

If

optionType

is

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are supplied by the Look and Feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

If

optionType

is

YES_NO_OPTION

, or

YES_NO_CANCEL_OPTION

and the

options

parameter is

null

,
then the options are supplied by the Look and Feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

The

messageType

parameter is primarily used to supply
a default icon from the look and feel.

showInternalInputDialog

```java
public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message)
```

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

. The dialog
is displayed in the

Component

's frame,
and is usually positioned below the

Component

.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Returns:** user's input

---

#### showInternalInputDialog

public static

String

showInternalInputDialog​(

Component

parentComponent,

Object

message)

Shows an internal question-message dialog requesting input from
the user parented to

parentComponent

. The dialog
is displayed in the

Component

's frame,
and is usually positioned below the

Component

.

showInternalInputDialog

```java
public static
String
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType)
```

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the
dialog title bar
**Parameters:** messageType

- the type of message that is to be displayed:
ERROR_MESSAGE, INFORMATION_MESSAGE, WARNING_MESSAGE,
QUESTION_MESSAGE, or PLAIN_MESSAGE
**Returns:** user's input

---

#### showInternalInputDialog

public static

String

showInternalInputDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType)

Shows an internal dialog requesting input from the user parented
to

parentComponent

with the dialog having the title

title

and message type

messageType

.

showInternalInputDialog

```java
public static
Object
showInternalInputDialog​(
Component
parentComponent,

Object
message,

String
title,
int messageType,

Icon
icon,

Object
[] selectionValues,

Object
initialSelectionValue)
```

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified. The user will able to choose from

selectionValues

, where

null

implies the user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

**Parameters:** parentComponent

- the parent

Component

for the dialog
**Parameters:** message

- the

Object

to display
**Parameters:** title

- the

String

to display in the dialog
title bar
**Parameters:** messageType

- the type of message to be displayed:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE
**Parameters:** icon

- the

Icon

image to display
**Parameters:** selectionValues

- an array of

Objects

that
gives the possible selections
**Parameters:** initialSelectionValue

- the value used to initialize the input
field
**Returns:** user's input, or

null

meaning the user
canceled the input

---

#### showInternalInputDialog

public static

Object

showInternalInputDialog​(

Component

parentComponent,

Object

message,

String

title,
int messageType,

Icon

icon,

Object

[] selectionValues,

Object

initialSelectionValue)

Prompts the user for input in a blocking internal dialog where
the initial selection, possible selections, and all other
options can be specified. The user will able to choose from

selectionValues

, where

null

implies the user can input
whatever they wish, usually by means of a

JTextField

.

initialSelectionValue

is the initial value to prompt
the user with. It is up to the UI to decide how best to represent
the

selectionValues

, but usually a

JComboBox

,

JList

, or

JTextField

will be used.

createInternalFrame

```java
public
JInternalFrame
createInternalFrame​(
Component
parentComponent,

String
title)
```

Creates and returns an instance of

JInternalFrame

.
The internal frame is created with the specified title,
and wrapping the

JOptionPane

.
The returned

JInternalFrame

is
added to the

JDesktopPane

ancestor of

parentComponent

, or components
parent if one its ancestors isn't a

JDesktopPane

,
or if

parentComponent

doesn't have a parent then a

RuntimeException

is thrown.

**Parameters:** parentComponent

- the parent

Component

for
the internal frame
**Parameters:** title

- the

String

to display in the
frame's title bar
**Returns:** a

JInternalFrame

containing a

JOptionPane
**Throws:** RuntimeException

- if

parentComponent

does
not have a valid parent

---

#### createInternalFrame

public

JInternalFrame

createInternalFrame​(

Component

parentComponent,

String

title)

Creates and returns an instance of

JInternalFrame

.
The internal frame is created with the specified title,
and wrapping the

JOptionPane

.
The returned

JInternalFrame

is
added to the

JDesktopPane

ancestor of

parentComponent

, or components
parent if one its ancestors isn't a

JDesktopPane

,
or if

parentComponent

doesn't have a parent then a

RuntimeException

is thrown.

getFrameForComponent

```java
public static
Frame
getFrameForComponent​(
Component
parentComponent)
throws
HeadlessException
```

Returns the specified component's

Frame

.

**Parameters:** parentComponent

- the

Component

to check for a

Frame
**Returns:** the

Frame

that contains the component,
or

getRootFrame

if the component is

null

,
or does not have a valid

Frame

parent
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** getRootFrame()

,

GraphicsEnvironment.isHeadless()

---

#### getFrameForComponent

public static

Frame

getFrameForComponent​(

Component

parentComponent)
throws

HeadlessException

Returns the specified component's

Frame

.

getDesktopPaneForComponent

```java
public static
JDesktopPane
getDesktopPaneForComponent​(
Component
parentComponent)
```

Returns the specified component's desktop pane.

**Parameters:** parentComponent

- the

Component

to check for a
desktop
**Returns:** the

JDesktopPane

that contains the component,
or

null

if the component is

null

or does not have an ancestor that is a

JInternalFrame

---

#### getDesktopPaneForComponent

public static

JDesktopPane

getDesktopPaneForComponent​(

Component

parentComponent)

Returns the specified component's desktop pane.

setRootFrame

```java
public static void setRootFrame​(
Frame
newRootFrame)
```

Sets the frame to use for class methods in which a frame is
not provided.

Note:

It is recommended that rather than using this method you supply a valid parent.

**Parameters:** newRootFrame

- the default

Frame

to use

---

#### setRootFrame

public static void setRootFrame​(

Frame

newRootFrame)

Sets the frame to use for class methods in which a frame is
not provided.

Note:

It is recommended that rather than using this method you supply a valid parent.

Note:

It is recommended that rather than using this method you supply a valid parent.

getRootFrame

```java
public static
Frame
getRootFrame()
throws
HeadlessException
```

Returns the

Frame

to use for the class methods in
which a frame is not provided.

**Returns:** the default

Frame

to use
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**See Also:** setRootFrame(java.awt.Frame)

,

GraphicsEnvironment.isHeadless()

---

#### getRootFrame

public static

Frame

getRootFrame()
throws

HeadlessException

Returns the

Frame

to use for the class methods in
which a frame is not provided.

setUI

```java
@BeanProperty
(
hidden
=true,

description
="The UI object that implements the optionpane\'s LookAndFeel")
public void setUI​(
OptionPaneUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the

OptionPaneUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

@BeanProperty

(

hidden

=true,

description

="The UI object that implements the optionpane\'s LookAndFeel")
public void setUI​(

OptionPaneUI

ui)

Sets the UI object which implements the L&F for this component.

getUI

```java
public
OptionPaneUI
getUI()
```

Returns the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

OptionPaneUI

object

---

#### getUI

public

OptionPaneUI

getUI()

Returns the UI object which implements the L&F for this component.

updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "OptionPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false)
public

String

getUIClassID()

Returns the name of the UI class that implements the
L&F for this component.

setMessage

```java
@BeanProperty
(
preferred
=true,

description
="The optionpane\'s message object.")
public void setMessage​(
Object
newMessage)
```

Sets the option pane's message-object.

**Parameters:** newMessage

- the

Object

to display
**See Also:** getMessage()

---

#### setMessage

@BeanProperty

(

preferred

=true,

description

="The optionpane\'s message object.")
public void setMessage​(

Object

newMessage)

Sets the option pane's message-object.

getMessage

```java
public
Object
getMessage()
```

Returns the message-object this pane displays.

**Returns:** the

Object

that is displayed
**See Also:** setMessage(java.lang.Object)

---

#### getMessage

public

Object

getMessage()

Returns the message-object this pane displays.

setIcon

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s type icon.")
public void setIcon​(
Icon
newIcon)
```

Sets the icon to display. If non-

null

, the look and feel
does not provide an icon.

**Parameters:** newIcon

- the

Icon

to display
**See Also:** getIcon()

---

#### setIcon

@BeanProperty

(

preferred

=true,

description

="The option pane\'s type icon.")
public void setIcon​(

Icon

newIcon)

Sets the icon to display. If non-

null

, the look and feel
does not provide an icon.

getIcon

```java
public
Icon
getIcon()
```

Returns the icon this pane displays.

**Returns:** the

Icon

that is displayed
**See Also:** setIcon(javax.swing.Icon)

---

#### getIcon

public

Icon

getIcon()

Returns the icon this pane displays.

setValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s value object.")
public void setValue​(
Object
newValue)
```

Sets the value the user has chosen.

**Parameters:** newValue

- the chosen value
**See Also:** getValue()

---

#### setValue

@BeanProperty

(

preferred

=true,

description

="The option pane\'s value object.")
public void setValue​(

Object

newValue)

Sets the value the user has chosen.

getValue

```java
public
Object
getValue()
```

Returns the value the user has selected.

UNINITIALIZED_VALUE

implies the user has not yet made a choice,

null

means the
user closed the window with out choosing anything. Otherwise
the returned value will be one of the options defined in this
object.

**Returns:** the

Object

chosen by the user,

UNINITIALIZED_VALUE

if the user has not yet made a choice, or

null

if
the user closed the window without making a choice
**See Also:** setValue(java.lang.Object)

---

#### getValue

public

Object

getValue()

Returns the value the user has selected.

UNINITIALIZED_VALUE

implies the user has not yet made a choice,

null

means the
user closed the window with out choosing anything. Otherwise
the returned value will be one of the options defined in this
object.

setOptions

```java
@BeanProperty
(
description
="The option pane\'s options objects.")
public void setOptions​(
Object
[] newOptions)
```

Sets the options this pane displays. If an element in

newOptions

is a

Component

it is added directly to the pane,
otherwise a button is created for the element.

**Parameters:** newOptions

- an array of

Objects

that create the
buttons the user can click on, or arbitrary

Components

to add to the pane
**See Also:** getOptions()

---

#### setOptions

@BeanProperty

(

description

="The option pane\'s options objects.")
public void setOptions​(

Object

[] newOptions)

Sets the options this pane displays. If an element in

newOptions

is a

Component

it is added directly to the pane,
otherwise a button is created for the element.

getOptions

```java
public
Object
[] getOptions()
```

Returns the choices the user can make.

**Returns:** the array of

Objects

that give the user's choices
**See Also:** setOptions(java.lang.Object[])

---

#### getOptions

public

Object

[] getOptions()

Returns the choices the user can make.

setInitialValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s initial value object.")
public void setInitialValue​(
Object
newInitialValue)
```

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

**Parameters:** newInitialValue

- the

Object

that gets the initial
keyboard focus
**See Also:** getInitialValue()

---

#### setInitialValue

@BeanProperty

(

preferred

=true,

description

="The option pane\'s initial value object.")
public void setInitialValue​(

Object

newInitialValue)

Sets the initial value that is to be enabled -- the

Component

that has the focus when the pane is initially displayed.

getInitialValue

```java
public
Object
getInitialValue()
```

Returns the initial value.

**Returns:** the

Object

that gets the initial keyboard focus
**See Also:** setInitialValue(java.lang.Object)

---

#### getInitialValue

public

Object

getInitialValue()

Returns the initial value.

setMessageType

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s message type.")
public void setMessageType​(int newType)
```

Sets the option pane's message type.
The message type is used by the Look and Feel to determine the
icon to display (if not supplied) as well as potentially how to
lay out the

parentComponent

.

**Parameters:** newType

- an integer specifying the kind of message to display:

ERROR_MESSAGE

,

INFORMATION_MESSAGE

,

WARNING_MESSAGE

,

QUESTION_MESSAGE

, or

PLAIN_MESSAGE
**Throws:** RuntimeException

- if

newType

is not one of the
legal values listed above
**See Also:** getMessageType()

---

#### setMessageType

@BeanProperty

(

preferred

=true,

description

="The option pane\'s message type.")
public void setMessageType​(int newType)

Sets the option pane's message type.
The message type is used by the Look and Feel to determine the
icon to display (if not supplied) as well as potentially how to
lay out the

parentComponent

.

getMessageType

```java
public int getMessageType()
```

Returns the message type.

**Returns:** an integer specifying the message type
**See Also:** setMessageType(int)

---

#### getMessageType

public int getMessageType()

Returns the message type.

setOptionType

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s option type.")
public void setOptionType​(int newType)
```

Sets the options to display.
The option type is used by the Look and Feel to
determine what buttons to show (unless options are supplied).

**Parameters:** newType

- an integer specifying the options the L&F is to display:

DEFAULT_OPTION

,

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

,
or

OK_CANCEL_OPTION
**Throws:** RuntimeException

- if

newType

is not one of
the legal values listed above
**See Also:** getOptionType()

,

setOptions(java.lang.Object[])

---

#### setOptionType

@BeanProperty

(

preferred

=true,

description

="The option pane\'s option type.")
public void setOptionType​(int newType)

Sets the options to display.
The option type is used by the Look and Feel to
determine what buttons to show (unless options are supplied).

getOptionType

```java
public int getOptionType()
```

Returns the type of options that are displayed.

**Returns:** an integer specifying the user-selectable options
**See Also:** setOptionType(int)

---

#### getOptionType

public int getOptionType()

Returns the type of options that are displayed.

setSelectionValues

```java
@BeanProperty
(
description
="The option pane\'s selection values.")
public void setSelectionValues​(
Object
[] newValues)
```

Sets the input selection values for a pane that provides the user
with a list of items to choose from. (The UI provides a widget
for choosing one of the values.) A

null

value
implies the user can input whatever they wish, usually by means
of a

JTextField

.

Sets

wantsInput

to true. Use

setInitialSelectionValue

to specify the initially-chosen
value. After the pane as been enabled,

inputValue

is
set to the value the user has selected.

**Parameters:** newValues

- an array of

Objects

the user to be
displayed
(usually in a list or combo-box) from which
the user can make a selection
**See Also:** setWantsInput(boolean)

,

setInitialSelectionValue(java.lang.Object)

,

getSelectionValues()

---

#### setSelectionValues

@BeanProperty

(

description

="The option pane\'s selection values.")
public void setSelectionValues​(

Object

[] newValues)

Sets the input selection values for a pane that provides the user
with a list of items to choose from. (The UI provides a widget
for choosing one of the values.) A

null

value
implies the user can input whatever they wish, usually by means
of a

JTextField

.

Sets

wantsInput

to true. Use

setInitialSelectionValue

to specify the initially-chosen
value. After the pane as been enabled,

inputValue

is
set to the value the user has selected.

Sets

wantsInput

to true. Use

setInitialSelectionValue

to specify the initially-chosen
value. After the pane as been enabled,

inputValue

is
set to the value the user has selected.

getSelectionValues

```java
public
Object
[] getSelectionValues()
```

Returns the input selection values.

**Returns:** the array of

Objects

the user can select
**See Also:** setSelectionValues(java.lang.Object[])

---

#### getSelectionValues

public

Object

[] getSelectionValues()

Returns the input selection values.

setInitialSelectionValue

```java
@BeanProperty
(
description
="The option pane\'s initial selection value object.")
public void setInitialSelectionValue​(
Object
newValue)
```

Sets the input value that is initially displayed as selected to the user.
Only used if

wantsInput

is true.

**Parameters:** newValue

- the initially selected value
**See Also:** setSelectionValues(java.lang.Object[])

,

getInitialSelectionValue()

---

#### setInitialSelectionValue

@BeanProperty

(

description

="The option pane\'s initial selection value object.")
public void setInitialSelectionValue​(

Object

newValue)

Sets the input value that is initially displayed as selected to the user.
Only used if

wantsInput

is true.

getInitialSelectionValue

```java
public
Object
getInitialSelectionValue()
```

Returns the input value that is displayed as initially selected to the user.

**Returns:** the initially selected value
**See Also:** setInitialSelectionValue(java.lang.Object)

,

setSelectionValues(java.lang.Object[])

---

#### getInitialSelectionValue

public

Object

getInitialSelectionValue()

Returns the input value that is displayed as initially selected to the user.

setInputValue

```java
@BeanProperty
(
preferred
=true,

description
="The option pane\'s input value object.")
public void setInputValue​(
Object
newValue)
```

Sets the input value that was selected or input by the user.
Only used if

wantsInput

is true. Note that this method
is invoked internally by the option pane (in response to user action)
and should generally not be called by client programs. To set the
input value initially displayed as selected to the user, use

setInitialSelectionValue

.

**Parameters:** newValue

- the

Object

used to set the
value that the user specified (usually in a text field)
**See Also:** setSelectionValues(java.lang.Object[])

,

setInitialSelectionValue(java.lang.Object)

,

setWantsInput(boolean)

,

getInputValue()

---

#### setInputValue

@BeanProperty

(

preferred

=true,

description

="The option pane\'s input value object.")
public void setInputValue​(

Object

newValue)

Sets the input value that was selected or input by the user.
Only used if

wantsInput

is true. Note that this method
is invoked internally by the option pane (in response to user action)
and should generally not be called by client programs. To set the
input value initially displayed as selected to the user, use

setInitialSelectionValue

.

getInputValue

```java
public
Object
getInputValue()
```

Returns the value the user has input, if

wantsInput

is true.

**Returns:** the

Object

the user specified,
if it was one of the objects, or a

String

if it was a value typed into a
field
**See Also:** setSelectionValues(java.lang.Object[])

,

setWantsInput(boolean)

,

setInputValue(java.lang.Object)

---

#### getInputValue

public

Object

getInputValue()

Returns the value the user has input, if

wantsInput

is true.

getMaxCharactersPerLineCount

```java
@BeanProperty
(
bound
=false)
public int getMaxCharactersPerLineCount()
```

Returns the maximum number of characters to place on a line in a
message. Default is to return

Integer.MAX_VALUE

.
The value can be
changed by overriding this method in a subclass.

**Returns:** an integer giving the maximum number of characters on a line

---

#### getMaxCharactersPerLineCount

@BeanProperty

(

bound

=false)
public int getMaxCharactersPerLineCount()

Returns the maximum number of characters to place on a line in a
message. Default is to return

Integer.MAX_VALUE

.
The value can be
changed by overriding this method in a subclass.

setWantsInput

```java
@BeanProperty
(
preferred
=true,

description
="Flag which allows the user to input a value.")
public void setWantsInput​(boolean newValue)
```

Sets the

wantsInput

property.
If

newValue

is true, an input component
(such as a text field or combo box) whose parent is

parentComponent

is provided to
allow the user to input a value. If

getSelectionValues

returns a non-

null

array, the input value is one of the
objects in that array. Otherwise the input value is whatever
the user inputs.

This is a bound property.

**Parameters:** newValue

- if true, an input component whose parent is

parentComponent

is provided to allow the user to input a value.
**See Also:** setSelectionValues(java.lang.Object[])

,

setInputValue(java.lang.Object)

---

#### setWantsInput

@BeanProperty

(

preferred

=true,

description

="Flag which allows the user to input a value.")
public void setWantsInput​(boolean newValue)

Sets the

wantsInput

property.
If

newValue

is true, an input component
(such as a text field or combo box) whose parent is

parentComponent

is provided to
allow the user to input a value. If

getSelectionValues

returns a non-

null

array, the input value is one of the
objects in that array. Otherwise the input value is whatever
the user inputs.

This is a bound property.

This is a bound property.

getWantsInput

```java
public boolean getWantsInput()
```

Returns the value of the

wantsInput

property.

**Returns:** true if an input component will be provided
**See Also:** setWantsInput(boolean)

---

#### getWantsInput

public boolean getWantsInput()

Returns the value of the

wantsInput

property.

selectInitialValue

```java
public void selectInitialValue()
```

Requests that the initial value be selected, which will set
focus to the initial value. This method
should be invoked after the window containing the option pane
is made visible.

---

#### selectInitialValue

public void selectInitialValue()

Requests that the initial value be selected, which will set
focus to the initial value. This method
should be invoked after the window containing the option pane
is made visible.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JOptionPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JOptionPane

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JOptionPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this option pane")
public
AccessibleContext
getAccessibleContext()
```

Returns the

AccessibleContext

associated with this JOptionPane.
For option panes, the

AccessibleContext

takes the form of an

AccessibleJOptionPane

.
A new

AccessibleJOptionPane

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJOptionPane that serves as the
AccessibleContext of this AccessibleJOptionPane

---

#### getAccessibleContext

@BeanProperty

(

bound

=false,

expert

=true,

description

="The AccessibleContext associated with this option pane")
public

AccessibleContext

getAccessibleContext()

Returns the

AccessibleContext

associated with this JOptionPane.
For option panes, the

AccessibleContext

takes the form of an

AccessibleJOptionPane

.
A new

AccessibleJOptionPane

instance is created if necessary.

---

