# Class LookAndFeel

**Source:** `java.desktop\javax\swing\LookAndFeel.html`

### Class Description

```java
public abstract class
LookAndFeel

extends
Object
```

LookAndFeel

, as the name implies, encapsulates a look and
feel. Beyond installing a look and feel most developers never need to
interact directly with

LookAndFeel

. In general only developers
creating a custom look and feel need to concern themselves with this class.

Swing is built upon the foundation that each

JComponent

subclass has an implementation of a specific

ComponentUI

subclass. The

ComponentUI

is often referred to as "the ui",
"component ui", or "look and feel delegate". The

ComponentUI

subclass is responsible for providing the look and feel specific
functionality of the component. For example,

JTree

requires
an implementation of the

ComponentUI

subclass

TreeUI

. The implementation of the specific

ComponentUI

subclass is provided by the

LookAndFeel

. Each

JComponent

subclass identifies the

ComponentUI

subclass it requires by way of the

JComponent

method

getUIClassID

.

Each

LookAndFeel

implementation must provide
an implementation of the appropriate

ComponentUI

subclass by
specifying a value for each of Swing's ui class ids in the

UIDefaults

object returned from

getDefaults

. For example,

BasicLookAndFeel

uses

BasicTreeUI

as the concrete
implementation for

TreeUI

. This is accomplished by

BasicLookAndFeel

providing the key-value pair

"TreeUI"-"javax.swing.plaf.basic.BasicTreeUI"

, in the

UIDefaults

returned from

getDefaults

. Refer to

UIDefaults.getUI(JComponent)

for details on how the implementation
of the

ComponentUI

subclass is obtained.

When a

LookAndFeel

is installed the

UIManager

does
not check that an entry exists for all ui class ids. As such,
random exceptions will occur if the current look and feel has not
provided a value for a particular ui class id and an instance of
the

JComponent

subclass is created.

Recommendations for Look and Feels

As noted in

UIManager

each

LookAndFeel

has the opportunity
to provide a set of defaults that are layered in with developer and
system defaults. Some of Swing's components require the look and feel
to provide a specific set of defaults. These are documented in the
classes that require the specific default.

ComponentUIs and defaults

All

ComponentUIs

typically need to set various properties
on the

JComponent

the

ComponentUI

is providing the
look and feel for. This is typically done when the

ComponentUI

is installed on the

JComponent

. Setting a
property should only be done if the developer has not set the
property. For non-primitive values it is recommended that the

ComponentUI

only change the property on the

JComponent

if the current value is

null

or implements

UIResource

. If the current value is

null

or
implements

UIResource

it indicates the property has not
been set by the developer, and the ui is free to change it. For
example,

BasicButtonUI.installDefaults

only changes the
font on the

JButton

if the return value from

button.getFont()

is

null

or implements

UIResource

. On the other hand if

button.getFont()

returned
a

non-null

value that did not implement

UIResource

then

BasicButtonUI.installDefaults

would not change the

JButton

's font.

For primitive values, such as

opaque

, the method

installProperty

should be invoked.

installProperty

only changes
the corresponding property if the value has not been changed by the
developer.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

**Direct Known Subclasses:** BasicLookAndFeel

,

MultiLookAndFeel

---

### Field Details

*No entries found.*

### Constructor Details

#### public LookAndFeel()

*No description found.*

---

### Method Details

#### public static void installColors​(
JComponent
c,

String
defaultBgName,

String
defaultFgName)

Convenience method for setting a component's foreground
and background color properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:**
- c

- component to set the colors on
- defaultBgName

- key for the background
- defaultFgName

- key for the foreground

**Throws:**
- NullPointerException

- as described in

exceptions

**See Also:**
- installColorsAndFont(javax.swing.JComponent, java.lang.String, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

---

#### public static void installColorsAndFont​(
JComponent
c,

String
defaultBgName,

String
defaultFgName,

String
defaultFontName)

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:**
- c

- component set to the colors and font on
- defaultBgName

- key for the background
- defaultFgName

- key for the foreground
- defaultFontName

- key for the font

**Throws:**
- NullPointerException

- as described in

exceptions

**See Also:**
- installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

,

UIManager.getFont(java.lang.Object)

---

#### public static void installBorder​(
JComponent
c,

String
defaultBorderName)

Convenience method for setting a component's border property with
a value from the defaults. The border is only set if the border is

null

or an instance of

UIResource

.

**Parameters:**
- c

- component to set the border on
- defaultBorderName

- key specifying the border

**Throws:**
- NullPointerException

- as described in

exceptions

---

#### public static void uninstallBorder​(
JComponent
c)

Convenience method for uninstalling a border. If the border of
the component is a

UIResource

, it is set to

null

.

**Parameters:**
- c

- component to uninstall the border on

**Throws:**
- NullPointerException

- if

c

is

null

---

#### public static void installProperty​(
JComponent
c,

String
propertyName,

Object
propertyValue)

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer. This method is intended to be used by
ui delegate instances that need to specify a default value for a
property of primitive type (boolean, int, ..), but do not wish
to override a value set by the client. Since primitive property
values cannot be wrapped with the

UIResource

marker, this method
uses private state to determine whether the property has been set
by the client.

**Parameters:**
- c

- target component to set the property on
- propertyName

- name of the property to set
- propertyValue

- value of the property

**Throws:**
- IllegalArgumentException

- if the specified property is not
one which can be set using this method
- ClassCastException

- if the property value has not been set
by the developer and the type does not match the property's type
- NullPointerException

- if

c

is

null

, or the
named property has not been set by the developer and

propertyValue

is

null

**Since:**
- 1.5

---

#### public static
JTextComponent.KeyBinding
[] makeKeyBindings​(
Object
[] keyBindingList)

Convenience method for building an array of

KeyBindings

. While this method is not deprecated, developers
should instead use

ActionMap

and

InputMap

for
supplying key bindings.

This method returns an array of

KeyBindings

, one for each
alternating

key-action

pair in

keyBindingList

.
A

key

can either be a

String

in the format
specified by the

KeyStroke.getKeyStroke

method, or
a

KeyStroke

. The

action

part of the pair is a

String

that corresponds to the name of the

Action

.

The following example illustrates creating a

KeyBinding

array
from six alternating

key-action

pairs:

```java
JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});
```

If

keyBindingList's

length is odd, the last element is
ignored.

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

**Parameters:**
- keyBindingList

- an array of

key-action

pairs

**Returns:**
- an array of

KeyBindings

**Throws:**
- NullPointerException

- if

keyBindingList

is

null
- ClassCastException

- if the

key

part of the pair is
not a

KeyStroke

or

String

, or the

action

part of the pair is not a

String

**See Also:**
- ActionMap

,

InputMap

,

KeyStroke.getKeyStroke(char)

---

#### public static
InputMap
makeInputMap​(
Object
[] keys)

Creates an

InputMapUIResource

from

keys

. This is
a convenience method for creating a new

InputMapUIResource

,
invoking

loadKeyBindings(map, keys)

, and returning the

InputMapUIResource

.

**Parameters:**
- keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

**Returns:**
- newly created and populated

InputMapUIResource

**See Also:**
- loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

**Since:**
- 1.3

---

#### public static
ComponentInputMap
makeComponentInputMap​(
JComponent
c,

Object
[] keys)

Creates a

ComponentInputMapUIResource

from

keys

. This is a convenience method for creating a
new

ComponentInputMapUIResource

, invoking

loadKeyBindings(map, keys)

, and returning the

ComponentInputMapUIResource

.

**Parameters:**
- c

- component to create the

ComponentInputMapUIResource

with
- keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

**Returns:**
- newly created and populated

InputMapUIResource

**Throws:**
- IllegalArgumentException

- if

c

is

null

**See Also:**
- loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

,

ComponentInputMapUIResource

**Since:**
- 1.3

---

#### public static void loadKeyBindings​(
InputMap
retMap,

Object
[] keys)

Populates an

InputMap

with the specified bindings.
The bindings are supplied as a list of alternating

keystroke-action key

pairs. The

keystroke

is either
an instance of

KeyStroke

, or a

String

that identifies the

KeyStroke

for the binding. Refer
to

KeyStroke.getKeyStroke(String)

for the specific
format. The

action key

part of the pair is the key
registered in the

InputMap

for the

KeyStroke

.

The following illustrates loading an

InputMap

with two

key-action

pairs:

```java
LookAndFeel.loadKeyBindings(inputMap, new Object[] {
"control X", "cut",
"control V", "paste"
});
```

Supplying a

null

list of bindings (

keys

) does not
change

retMap

in any way.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

**Parameters:**
- retMap

-

InputMap

to add the

key-action

pairs to
- keys

- bindings to add to

retMap

**Throws:**
- NullPointerException

- if

keys

is

non-null

, not empty, and

retMap

is

null

**See Also:**
- KeyStroke.getKeyStroke(String)

,

InputMap

**Since:**
- 1.3

---

#### public static
Object
makeIcon​(
Class
<?> baseClass,

String
gifFile)

Creates and returns a

UIDefault.LazyValue

that loads an
image. The returned value is an implementation of

UIDefaults.LazyValue

. When

createValue

is invoked on
the returned object, the image is loaded. If the image is

non-null

, it is then wrapped in an

Icon

that implements

UIResource

. The image is loaded using

Class.getResourceAsStream(gifFile)

.

This method does not check the arguments in any way. It is
strongly recommended that

non-null

values are supplied else
exceptions may occur when

createValue

is invoked on the
returned object.

**Parameters:**
- baseClass

-

Class

used to load the resource
- gifFile

- path to the image to load

**Returns:**
- a

UIDefaults.LazyValue

; when resolved the

LazyValue

loads the specified image

**See Also:**
- UIDefaults.LazyValue

,

Icon

,

Class.getResourceAsStream(String)

---

#### public
LayoutStyle
getLayoutStyle()

Returns the

LayoutStyle

for this look
and feel. This never returns

null

.

You generally don't use the

LayoutStyle

from
the look and feel, instead use the

LayoutStyle

method

getInstance

.

**Returns:**
- the

LayoutStyle

for this look and feel

**See Also:**
- LayoutStyle.getInstance()

**Since:**
- 1.6

---

#### public void provideErrorFeedback​(
Component
component)

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus. The default implementation beeps. Subclasses
that wish different behavior should override this and provide
the additional feedback.

**Parameters:**
- component

- the

Component

the error occurred in,
may be

null

indicating the error condition is not directly
associated with a

Component

**Since:**
- 1.4

---

#### public static
Object
getDesktopPropertyValue​(
String
systemPropertyName,

Object
fallbackValue)

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.
If the value of the specified property is

null

,

fallbackValue

is returned.

**Parameters:**
- systemPropertyName

- the name of the system desktop property being queried
- fallbackValue

- the object to be returned as the value if the system value is null

**Returns:**
- the current value of the desktop property

**See Also:**
- Toolkit.getDesktopProperty(java.lang.String)

**Since:**
- 1.4

---

#### public
Icon
getDisabledIcon​(
JComponent
component,

Icon
icon)

Returns an

Icon

with a disabled appearance.
This method is used to generate a disabled

Icon

when
one has not been specified. For example, if you create a

JButton

and only specify an

Icon

via

setIcon

this method will be called to generate the
disabled

Icon

. If

null

is passed as

icon

this method returns

null

.

Some look and feels might not render the disabled

Icon

, in which
case they will ignore this.

**Parameters:**
- component

-

JComponent

that will display the

Icon

,
may be

null
- icon

-

Icon

to generate the disabled icon from

**Returns:**
- disabled

Icon

, or

null

if a suitable

Icon

can not be generated

**Since:**
- 1.5

---

#### public
Icon
getDisabledSelectedIcon​(
JComponent
component,

Icon
icon)

Returns an

Icon

for use by disabled
components that are also selected. This method is used to generate an

Icon

for components that are in both the disabled and
selected states but do not have a specific

Icon

for this
state. For example, if you create a

JButton

and only
specify an

Icon

via

setIcon

this method
will be called to generate the disabled and selected

Icon

. If

null

is passed as

icon

this
methods returns

null

.

Some look and feels might not render the disabled and selected

Icon

, in which case they will ignore this.

**Parameters:**
- component

-

JComponent

that will display the

Icon

,
may be

null
- icon

-

Icon

to generate disabled and selected icon from

**Returns:**
- disabled and selected icon, or

null

if a suitable

Icon

can not be generated.

**Since:**
- 1.5

---

#### public abstract
String
getName()

Return a short string that identifies this look and feel, e.g.
"CDE/Motif". This string should be appropriate for a menu item.
Distinct look and feels should have different names, e.g.
a subclass of MotifLookAndFeel that changes the way a few components
are rendered should be called "CDE/Motif My Way"; something
that would be useful to a user trying to select a L&F from a list
of names.

**Returns:**
- short identifier for the look and feel

---

#### public abstract
String
getID()

Return a string that identifies this look and feel. This string
will be used by applications/services that want to recognize
well known look and feel implementations. Presently
the well known names are "Motif", "Windows", "Mac", "Metal". Note
that a LookAndFeel derived from a well known superclass
that doesn't make any fundamental changes to the look or feel
shouldn't override this method.

**Returns:**
- identifier for the look and feel

---

#### public abstract
String
getDescription()

Return a one line description of this look and feel implementation,
e.g. "The CDE/Motif Look and Feel". This string is intended for
the user, e.g. in the title of a window or in a ToolTip message.

**Returns:**
- short description for the look and feel

---

#### public boolean getSupportsWindowDecorations()

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

The default implementation returns

false

, subclasses that
support

Window

decorations should override this and return

true

.

**Returns:**
- true

if the

RootPaneUI

instances created by
this look and feel support client side decorations

**See Also:**
- JDialog.setDefaultLookAndFeelDecorated(boolean)

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

,

JRootPane.setWindowDecorationStyle(int)

**Since:**
- 1.4

---

#### public abstract boolean isNativeLookAndFeel()

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

. For
example, when the underlying platform is Solaris running CDE
a CDE/Motif look and feel implementation would return

true

.

**Returns:**
- true

if this look and feel represents the underlying
platform look and feel

---

#### public abstract boolean isSupportedLookAndFeel()

Return

true

if the underlying platform supports and or permits
this look and feel. This method returns

false

if the look
and feel depends on special resources or legal agreements that
aren't defined for the current platform.

**Returns:**
- true

if this is a supported look and feel

**See Also:**
- UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public void initialize()

Initializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when a
look and feel is installed as the current look and feel. This
method is invoked before the

UIManager

invokes

getDefaults

. This method is intended to perform any
initialization for the look and feel. Subclasses
should do any one-time setup they need here, rather than
in a static initializer, because look and feel class objects
may be loaded just to discover that

isSupportedLookAndFeel()

returns

false

.

**See Also:**
- uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public void uninitialize()

Uninitializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when
the look and feel is uninstalled. For example,

UIManager.setLookAndFeel

invokes this when the look and
feel is changed.

Subclasses may choose to free up some resources here.

**See Also:**
- initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public
UIDefaults
getDefaults()

Returns the look and feel defaults. While this method is public,
it should only be invoked by the

UIManager

when the
look and feel is set as the current look and feel and after

initialize

has been invoked.

**Returns:**
- the look and feel defaults

**See Also:**
- initialize()

,

uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public
String
toString()

Returns a string that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this object

---

### Additional Sections

#### Class LookAndFeel

java.lang.Object

- javax.swing.LookAndFeel

javax.swing.LookAndFeel

**Direct Known Subclasses:** BasicLookAndFeel

,

MultiLookAndFeel

```java
public abstract class
LookAndFeel

extends
Object
```

LookAndFeel

, as the name implies, encapsulates a look and
feel. Beyond installing a look and feel most developers never need to
interact directly with

LookAndFeel

. In general only developers
creating a custom look and feel need to concern themselves with this class.

Swing is built upon the foundation that each

JComponent

subclass has an implementation of a specific

ComponentUI

subclass. The

ComponentUI

is often referred to as "the ui",
"component ui", or "look and feel delegate". The

ComponentUI

subclass is responsible for providing the look and feel specific
functionality of the component. For example,

JTree

requires
an implementation of the

ComponentUI

subclass

TreeUI

. The implementation of the specific

ComponentUI

subclass is provided by the

LookAndFeel

. Each

JComponent

subclass identifies the

ComponentUI

subclass it requires by way of the

JComponent

method

getUIClassID

.

Each

LookAndFeel

implementation must provide
an implementation of the appropriate

ComponentUI

subclass by
specifying a value for each of Swing's ui class ids in the

UIDefaults

object returned from

getDefaults

. For example,

BasicLookAndFeel

uses

BasicTreeUI

as the concrete
implementation for

TreeUI

. This is accomplished by

BasicLookAndFeel

providing the key-value pair

"TreeUI"-"javax.swing.plaf.basic.BasicTreeUI"

, in the

UIDefaults

returned from

getDefaults

. Refer to

UIDefaults.getUI(JComponent)

for details on how the implementation
of the

ComponentUI

subclass is obtained.

When a

LookAndFeel

is installed the

UIManager

does
not check that an entry exists for all ui class ids. As such,
random exceptions will occur if the current look and feel has not
provided a value for a particular ui class id and an instance of
the

JComponent

subclass is created.

Recommendations for Look and Feels

As noted in

UIManager

each

LookAndFeel

has the opportunity
to provide a set of defaults that are layered in with developer and
system defaults. Some of Swing's components require the look and feel
to provide a specific set of defaults. These are documented in the
classes that require the specific default.

ComponentUIs and defaults

All

ComponentUIs

typically need to set various properties
on the

JComponent

the

ComponentUI

is providing the
look and feel for. This is typically done when the

ComponentUI

is installed on the

JComponent

. Setting a
property should only be done if the developer has not set the
property. For non-primitive values it is recommended that the

ComponentUI

only change the property on the

JComponent

if the current value is

null

or implements

UIResource

. If the current value is

null

or
implements

UIResource

it indicates the property has not
been set by the developer, and the ui is free to change it. For
example,

BasicButtonUI.installDefaults

only changes the
font on the

JButton

if the return value from

button.getFont()

is

null

or implements

UIResource

. On the other hand if

button.getFont()

returned
a

non-null

value that did not implement

UIResource

then

BasicButtonUI.installDefaults

would not change the

JButton

's font.

For primitive values, such as

opaque

, the method

installProperty

should be invoked.

installProperty

only changes
the corresponding property if the value has not been changed by the
developer.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

**Since:** 1.2

public abstract class

LookAndFeel

extends

Object

LookAndFeel

, as the name implies, encapsulates a look and
feel. Beyond installing a look and feel most developers never need to
interact directly with

LookAndFeel

. In general only developers
creating a custom look and feel need to concern themselves with this class.

Swing is built upon the foundation that each

JComponent

subclass has an implementation of a specific

ComponentUI

subclass. The

ComponentUI

is often referred to as "the ui",
"component ui", or "look and feel delegate". The

ComponentUI

subclass is responsible for providing the look and feel specific
functionality of the component. For example,

JTree

requires
an implementation of the

ComponentUI

subclass

TreeUI

. The implementation of the specific

ComponentUI

subclass is provided by the

LookAndFeel

. Each

JComponent

subclass identifies the

ComponentUI

subclass it requires by way of the

JComponent

method

getUIClassID

.

Each

LookAndFeel

implementation must provide
an implementation of the appropriate

ComponentUI

subclass by
specifying a value for each of Swing's ui class ids in the

UIDefaults

object returned from

getDefaults

. For example,

BasicLookAndFeel

uses

BasicTreeUI

as the concrete
implementation for

TreeUI

. This is accomplished by

BasicLookAndFeel

providing the key-value pair

"TreeUI"-"javax.swing.plaf.basic.BasicTreeUI"

, in the

UIDefaults

returned from

getDefaults

. Refer to

UIDefaults.getUI(JComponent)

for details on how the implementation
of the

ComponentUI

subclass is obtained.

When a

LookAndFeel

is installed the

UIManager

does
not check that an entry exists for all ui class ids. As such,
random exceptions will occur if the current look and feel has not
provided a value for a particular ui class id and an instance of
the

JComponent

subclass is created.

Recommendations for Look and Feels

As noted in

UIManager

each

LookAndFeel

has the opportunity
to provide a set of defaults that are layered in with developer and
system defaults. Some of Swing's components require the look and feel
to provide a specific set of defaults. These are documented in the
classes that require the specific default.

ComponentUIs and defaults

All

ComponentUIs

typically need to set various properties
on the

JComponent

the

ComponentUI

is providing the
look and feel for. This is typically done when the

ComponentUI

is installed on the

JComponent

. Setting a
property should only be done if the developer has not set the
property. For non-primitive values it is recommended that the

ComponentUI

only change the property on the

JComponent

if the current value is

null

or implements

UIResource

. If the current value is

null

or
implements

UIResource

it indicates the property has not
been set by the developer, and the ui is free to change it. For
example,

BasicButtonUI.installDefaults

only changes the
font on the

JButton

if the return value from

button.getFont()

is

null

or implements

UIResource

. On the other hand if

button.getFont()

returned
a

non-null

value that did not implement

UIResource

then

BasicButtonUI.installDefaults

would not change the

JButton

's font.

For primitive values, such as

opaque

, the method

installProperty

should be invoked.

installProperty

only changes
the corresponding property if the value has not been changed by the
developer.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

Swing is built upon the foundation that each

JComponent

subclass has an implementation of a specific

ComponentUI

subclass. The

ComponentUI

is often referred to as "the ui",
"component ui", or "look and feel delegate". The

ComponentUI

subclass is responsible for providing the look and feel specific
functionality of the component. For example,

JTree

requires
an implementation of the

ComponentUI

subclass

TreeUI

. The implementation of the specific

ComponentUI

subclass is provided by the

LookAndFeel

. Each

JComponent

subclass identifies the

ComponentUI

subclass it requires by way of the

JComponent

method

getUIClassID

.

Each

LookAndFeel

implementation must provide
an implementation of the appropriate

ComponentUI

subclass by
specifying a value for each of Swing's ui class ids in the

UIDefaults

object returned from

getDefaults

. For example,

BasicLookAndFeel

uses

BasicTreeUI

as the concrete
implementation for

TreeUI

. This is accomplished by

BasicLookAndFeel

providing the key-value pair

"TreeUI"-"javax.swing.plaf.basic.BasicTreeUI"

, in the

UIDefaults

returned from

getDefaults

. Refer to

UIDefaults.getUI(JComponent)

for details on how the implementation
of the

ComponentUI

subclass is obtained.

When a

LookAndFeel

is installed the

UIManager

does
not check that an entry exists for all ui class ids. As such,
random exceptions will occur if the current look and feel has not
provided a value for a particular ui class id and an instance of
the

JComponent

subclass is created.

Recommendations for Look and Feels

As noted in

UIManager

each

LookAndFeel

has the opportunity
to provide a set of defaults that are layered in with developer and
system defaults. Some of Swing's components require the look and feel
to provide a specific set of defaults. These are documented in the
classes that require the specific default.

ComponentUIs and defaults

All

ComponentUIs

typically need to set various properties
on the

JComponent

the

ComponentUI

is providing the
look and feel for. This is typically done when the

ComponentUI

is installed on the

JComponent

. Setting a
property should only be done if the developer has not set the
property. For non-primitive values it is recommended that the

ComponentUI

only change the property on the

JComponent

if the current value is

null

or implements

UIResource

. If the current value is

null

or
implements

UIResource

it indicates the property has not
been set by the developer, and the ui is free to change it. For
example,

BasicButtonUI.installDefaults

only changes the
font on the

JButton

if the return value from

button.getFont()

is

null

or implements

UIResource

. On the other hand if

button.getFont()

returned
a

non-null

value that did not implement

UIResource

then

BasicButtonUI.installDefaults

would not change the

JButton

's font.

For primitive values, such as

opaque

, the method

installProperty

should be invoked.

installProperty

only changes
the corresponding property if the value has not been changed by the
developer.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

Each

LookAndFeel

implementation must provide
an implementation of the appropriate

ComponentUI

subclass by
specifying a value for each of Swing's ui class ids in the

UIDefaults

object returned from

getDefaults

. For example,

BasicLookAndFeel

uses

BasicTreeUI

as the concrete
implementation for

TreeUI

. This is accomplished by

BasicLookAndFeel

providing the key-value pair

"TreeUI"-"javax.swing.plaf.basic.BasicTreeUI"

, in the

UIDefaults

returned from

getDefaults

. Refer to

UIDefaults.getUI(JComponent)

for details on how the implementation
of the

ComponentUI

subclass is obtained.

When a

LookAndFeel

is installed the

UIManager

does
not check that an entry exists for all ui class ids. As such,
random exceptions will occur if the current look and feel has not
provided a value for a particular ui class id and an instance of
the

JComponent

subclass is created.

Recommendations for Look and Feels

As noted in

UIManager

each

LookAndFeel

has the opportunity
to provide a set of defaults that are layered in with developer and
system defaults. Some of Swing's components require the look and feel
to provide a specific set of defaults. These are documented in the
classes that require the specific default.

ComponentUIs and defaults

All

ComponentUIs

typically need to set various properties
on the

JComponent

the

ComponentUI

is providing the
look and feel for. This is typically done when the

ComponentUI

is installed on the

JComponent

. Setting a
property should only be done if the developer has not set the
property. For non-primitive values it is recommended that the

ComponentUI

only change the property on the

JComponent

if the current value is

null

or implements

UIResource

. If the current value is

null

or
implements

UIResource

it indicates the property has not
been set by the developer, and the ui is free to change it. For
example,

BasicButtonUI.installDefaults

only changes the
font on the

JButton

if the return value from

button.getFont()

is

null

or implements

UIResource

. On the other hand if

button.getFont()

returned
a

non-null

value that did not implement

UIResource

then

BasicButtonUI.installDefaults

would not change the

JButton

's font.

For primitive values, such as

opaque

, the method

installProperty

should be invoked.

installProperty

only changes
the corresponding property if the value has not been changed by the
developer.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

When a

LookAndFeel

is installed the

UIManager

does
not check that an entry exists for all ui class ids. As such,
random exceptions will occur if the current look and feel has not
provided a value for a particular ui class id and an instance of
the

JComponent

subclass is created.

Recommendations for Look and Feels

As noted in

UIManager

each

LookAndFeel

has the opportunity
to provide a set of defaults that are layered in with developer and
system defaults. Some of Swing's components require the look and feel
to provide a specific set of defaults. These are documented in the
classes that require the specific default.

ComponentUIs and defaults

All

ComponentUIs

typically need to set various properties
on the

JComponent

the

ComponentUI

is providing the
look and feel for. This is typically done when the

ComponentUI

is installed on the

JComponent

. Setting a
property should only be done if the developer has not set the
property. For non-primitive values it is recommended that the

ComponentUI

only change the property on the

JComponent

if the current value is

null

or implements

UIResource

. If the current value is

null

or
implements

UIResource

it indicates the property has not
been set by the developer, and the ui is free to change it. For
example,

BasicButtonUI.installDefaults

only changes the
font on the

JButton

if the return value from

button.getFont()

is

null

or implements

UIResource

. On the other hand if

button.getFont()

returned
a

non-null

value that did not implement

UIResource

then

BasicButtonUI.installDefaults

would not change the

JButton

's font.

For primitive values, such as

opaque

, the method

installProperty

should be invoked.

installProperty

only changes
the corresponding property if the value has not been changed by the
developer.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

---

#### ComponentUIs and defaults

For primitive values, such as

opaque

, the method

installProperty

should be invoked.

installProperty

only changes
the corresponding property if the value has not been changed by the
developer.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

ComponentUI

implementations should use the various install methods
provided by this class as they handle the necessary checking and install
the property using the recommended guidelines.

Exceptions

All of the install methods provided by

LookAndFeel

need to
access the defaults if the value of the property being changed is

null

or a

UIResource

. For example, installing the
font does the following:

```java
JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}
```

If the font is

null

or a

UIResource

, the
defaults table is queried with the key

fontKey

. All of

UIDefault's

get methods throw a

NullPointerException

if passed in

null

. As such, unless
otherwise noted each of the various install methods of

LookAndFeel

throw a

NullPointerException

if the current
value is

null

or a

UIResource

and the supplied
defaults key is

null

. In addition, unless otherwise specified
all of the

install

methods throw a

NullPointerException

if
a

null

component is passed in.

---

#### Exceptions

JComponent c;
Font font = c.getFont();
if (font == null || (font instanceof UIResource)) {
c.setFont(UIManager.getFont("fontKey"));
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LookAndFeel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

UIDefaults

getDefaults

()

Returns the look and feel defaults.

abstract

String

getDescription

()

Return a one line description of this look and feel implementation,
e.g.

static

Object

getDesktopPropertyValue

​(

String

systemPropertyName,

Object

fallbackValue)

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.

Icon

getDisabledIcon

​(

JComponent

component,

Icon

icon)

Returns an

Icon

with a disabled appearance.

Icon

getDisabledSelectedIcon

​(

JComponent

component,

Icon

icon)

Returns an

Icon

for use by disabled
components that are also selected.

abstract

String

getID

()

Return a string that identifies this look and feel.

LayoutStyle

getLayoutStyle

()

Returns the

LayoutStyle

for this look
and feel.

abstract

String

getName

()

Return a short string that identifies this look and feel, e.g.

boolean

getSupportsWindowDecorations

()

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

void

initialize

()

Initializes the look and feel.

static void

installBorder

​(

JComponent

c,

String

defaultBorderName)

Convenience method for setting a component's border property with
a value from the defaults.

static void

installColors

​(

JComponent

c,

String

defaultBgName,

String

defaultFgName)

Convenience method for setting a component's foreground
and background color properties with values from the
defaults.

static void

installColorsAndFont

​(

JComponent

c,

String

defaultBgName,

String

defaultFgName,

String

defaultFontName)

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults.

static void

installProperty

​(

JComponent

c,

String

propertyName,

Object

propertyValue)

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer.

abstract boolean

isNativeLookAndFeel

()

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

.

abstract boolean

isSupportedLookAndFeel

()

Return

true

if the underlying platform supports and or permits
this look and feel.

static void

loadKeyBindings

​(

InputMap

retMap,

Object

[] keys)

Populates an

InputMap

with the specified bindings.

static

ComponentInputMap

makeComponentInputMap

​(

JComponent

c,

Object

[] keys)

Creates a

ComponentInputMapUIResource

from

keys

.

static

Object

makeIcon

​(

Class

<?> baseClass,

String

gifFile)

Creates and returns a

UIDefault.LazyValue

that loads an
image.

static

InputMap

makeInputMap

​(

Object

[] keys)

Creates an

InputMapUIResource

from

keys

.

static

JTextComponent.KeyBinding

[]

makeKeyBindings

​(

Object

[] keyBindingList)

Convenience method for building an array of

KeyBindings

.

void

provideErrorFeedback

​(

Component

component)

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

uninitialize

()

Uninitializes the look and feel.

static void

uninstallBorder

​(

JComponent

c)

Convenience method for uninstalling a border.

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

Constructor Summary

Constructors

Constructor

Description

LookAndFeel

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

UIDefaults

getDefaults

()

Returns the look and feel defaults.

abstract

String

getDescription

()

Return a one line description of this look and feel implementation,
e.g.

static

Object

getDesktopPropertyValue

​(

String

systemPropertyName,

Object

fallbackValue)

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.

Icon

getDisabledIcon

​(

JComponent

component,

Icon

icon)

Returns an

Icon

with a disabled appearance.

Icon

getDisabledSelectedIcon

​(

JComponent

component,

Icon

icon)

Returns an

Icon

for use by disabled
components that are also selected.

abstract

String

getID

()

Return a string that identifies this look and feel.

LayoutStyle

getLayoutStyle

()

Returns the

LayoutStyle

for this look
and feel.

abstract

String

getName

()

Return a short string that identifies this look and feel, e.g.

boolean

getSupportsWindowDecorations

()

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

void

initialize

()

Initializes the look and feel.

static void

installBorder

​(

JComponent

c,

String

defaultBorderName)

Convenience method for setting a component's border property with
a value from the defaults.

static void

installColors

​(

JComponent

c,

String

defaultBgName,

String

defaultFgName)

Convenience method for setting a component's foreground
and background color properties with values from the
defaults.

static void

installColorsAndFont

​(

JComponent

c,

String

defaultBgName,

String

defaultFgName,

String

defaultFontName)

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults.

static void

installProperty

​(

JComponent

c,

String

propertyName,

Object

propertyValue)

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer.

abstract boolean

isNativeLookAndFeel

()

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

.

abstract boolean

isSupportedLookAndFeel

()

Return

true

if the underlying platform supports and or permits
this look and feel.

static void

loadKeyBindings

​(

InputMap

retMap,

Object

[] keys)

Populates an

InputMap

with the specified bindings.

static

ComponentInputMap

makeComponentInputMap

​(

JComponent

c,

Object

[] keys)

Creates a

ComponentInputMapUIResource

from

keys

.

static

Object

makeIcon

​(

Class

<?> baseClass,

String

gifFile)

Creates and returns a

UIDefault.LazyValue

that loads an
image.

static

InputMap

makeInputMap

​(

Object

[] keys)

Creates an

InputMapUIResource

from

keys

.

static

JTextComponent.KeyBinding

[]

makeKeyBindings

​(

Object

[] keyBindingList)

Convenience method for building an array of

KeyBindings

.

void

provideErrorFeedback

​(

Component

component)

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus.

String

toString

()

Returns a string that displays and identifies this
object's properties.

void

uninitialize

()

Uninitializes the look and feel.

static void

uninstallBorder

​(

JComponent

c)

Convenience method for uninstalling a border.

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

Returns the look and feel defaults.

Return a one line description of this look and feel implementation,
e.g.

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.

Returns an

Icon

with a disabled appearance.

Returns an

Icon

for use by disabled
components that are also selected.

Return a string that identifies this look and feel.

Returns the

LayoutStyle

for this look
and feel.

Return a short string that identifies this look and feel, e.g.

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

Initializes the look and feel.

Convenience method for setting a component's border property with
a value from the defaults.

Convenience method for setting a component's foreground
and background color properties with values from the
defaults.

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults.

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer.

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

.

Return

true

if the underlying platform supports and or permits
this look and feel.

Populates an

InputMap

with the specified bindings.

Creates a

ComponentInputMapUIResource

from

keys

.

Creates and returns a

UIDefault.LazyValue

that loads an
image.

Creates an

InputMapUIResource

from

keys

.

Convenience method for building an array of

KeyBindings

.

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus.

Returns a string that displays and identifies this
object's properties.

Uninitializes the look and feel.

Convenience method for uninstalling a border.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LookAndFeel

```java
public LookAndFeel()
```

============ METHOD DETAIL ==========

- Method Detail

- installColors

```java
public static void installColors​(
JComponent
c,

String
defaultBgName,

String
defaultFgName)
```

Convenience method for setting a component's foreground
and background color properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:** c

- component to set the colors on
**Parameters:** defaultBgName

- key for the background
**Parameters:** defaultFgName

- key for the foreground
**Throws:** NullPointerException

- as described in

exceptions
**See Also:** installColorsAndFont(javax.swing.JComponent, java.lang.String, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

- installColorsAndFont

```java
public static void installColorsAndFont​(
JComponent
c,

String
defaultBgName,

String
defaultFgName,

String
defaultFontName)
```

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:** c

- component set to the colors and font on
**Parameters:** defaultBgName

- key for the background
**Parameters:** defaultFgName

- key for the foreground
**Parameters:** defaultFontName

- key for the font
**Throws:** NullPointerException

- as described in

exceptions
**See Also:** installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

,

UIManager.getFont(java.lang.Object)

- installBorder

```java
public static void installBorder​(
JComponent
c,

String
defaultBorderName)
```

Convenience method for setting a component's border property with
a value from the defaults. The border is only set if the border is

null

or an instance of

UIResource

.

**Parameters:** c

- component to set the border on
**Parameters:** defaultBorderName

- key specifying the border
**Throws:** NullPointerException

- as described in

exceptions

- uninstallBorder

```java
public static void uninstallBorder​(
JComponent
c)
```

Convenience method for uninstalling a border. If the border of
the component is a

UIResource

, it is set to

null

.

**Parameters:** c

- component to uninstall the border on
**Throws:** NullPointerException

- if

c

is

null

- installProperty

```java
public static void installProperty​(
JComponent
c,

String
propertyName,

Object
propertyValue)
```

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer. This method is intended to be used by
ui delegate instances that need to specify a default value for a
property of primitive type (boolean, int, ..), but do not wish
to override a value set by the client. Since primitive property
values cannot be wrapped with the

UIResource

marker, this method
uses private state to determine whether the property has been set
by the client.

**Parameters:** c

- target component to set the property on
**Parameters:** propertyName

- name of the property to set
**Parameters:** propertyValue

- value of the property
**Throws:** IllegalArgumentException

- if the specified property is not
one which can be set using this method
**Throws:** ClassCastException

- if the property value has not been set
by the developer and the type does not match the property's type
**Throws:** NullPointerException

- if

c

is

null

, or the
named property has not been set by the developer and

propertyValue

is

null
**Since:** 1.5

- makeKeyBindings

```java
public static
JTextComponent.KeyBinding
[] makeKeyBindings​(
Object
[] keyBindingList)
```

Convenience method for building an array of

KeyBindings

. While this method is not deprecated, developers
should instead use

ActionMap

and

InputMap

for
supplying key bindings.

This method returns an array of

KeyBindings

, one for each
alternating

key-action

pair in

keyBindingList

.
A

key

can either be a

String

in the format
specified by the

KeyStroke.getKeyStroke

method, or
a

KeyStroke

. The

action

part of the pair is a

String

that corresponds to the name of the

Action

.

The following example illustrates creating a

KeyBinding

array
from six alternating

key-action

pairs:

```java
JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});
```

If

keyBindingList's

length is odd, the last element is
ignored.

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

**Parameters:** keyBindingList

- an array of

key-action

pairs
**Returns:** an array of

KeyBindings
**Throws:** NullPointerException

- if

keyBindingList

is

null
**Throws:** ClassCastException

- if the

key

part of the pair is
not a

KeyStroke

or

String

, or the

action

part of the pair is not a

String
**See Also:** ActionMap

,

InputMap

,

KeyStroke.getKeyStroke(char)

- makeInputMap

```java
public static
InputMap
makeInputMap​(
Object
[] keys)
```

Creates an

InputMapUIResource

from

keys

. This is
a convenience method for creating a new

InputMapUIResource

,
invoking

loadKeyBindings(map, keys)

, and returning the

InputMapUIResource

.

**Parameters:** keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])
**Returns:** newly created and populated

InputMapUIResource
**Since:** 1.3
**See Also:** loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

- makeComponentInputMap

```java
public static
ComponentInputMap
makeComponentInputMap​(
JComponent
c,

Object
[] keys)
```

Creates a

ComponentInputMapUIResource

from

keys

. This is a convenience method for creating a
new

ComponentInputMapUIResource

, invoking

loadKeyBindings(map, keys)

, and returning the

ComponentInputMapUIResource

.

**Parameters:** c

- component to create the

ComponentInputMapUIResource

with
**Parameters:** keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])
**Returns:** newly created and populated

InputMapUIResource
**Throws:** IllegalArgumentException

- if

c

is

null
**Since:** 1.3
**See Also:** loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

,

ComponentInputMapUIResource

- loadKeyBindings

```java
public static void loadKeyBindings​(
InputMap
retMap,

Object
[] keys)
```

Populates an

InputMap

with the specified bindings.
The bindings are supplied as a list of alternating

keystroke-action key

pairs. The

keystroke

is either
an instance of

KeyStroke

, or a

String

that identifies the

KeyStroke

for the binding. Refer
to

KeyStroke.getKeyStroke(String)

for the specific
format. The

action key

part of the pair is the key
registered in the

InputMap

for the

KeyStroke

.

The following illustrates loading an

InputMap

with two

key-action

pairs:

```java
LookAndFeel.loadKeyBindings(inputMap, new Object[] {
"control X", "cut",
"control V", "paste"
});
```

Supplying a

null

list of bindings (

keys

) does not
change

retMap

in any way.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

**Parameters:** retMap

-

InputMap

to add the

key-action

pairs to
**Parameters:** keys

- bindings to add to

retMap
**Throws:** NullPointerException

- if

keys

is

non-null

, not empty, and

retMap

is

null
**Since:** 1.3
**See Also:** KeyStroke.getKeyStroke(String)

,

InputMap

- makeIcon

```java
public static
Object
makeIcon​(
Class
<?> baseClass,

String
gifFile)
```

Creates and returns a

UIDefault.LazyValue

that loads an
image. The returned value is an implementation of

UIDefaults.LazyValue

. When

createValue

is invoked on
the returned object, the image is loaded. If the image is

non-null

, it is then wrapped in an

Icon

that implements

UIResource

. The image is loaded using

Class.getResourceAsStream(gifFile)

.

This method does not check the arguments in any way. It is
strongly recommended that

non-null

values are supplied else
exceptions may occur when

createValue

is invoked on the
returned object.

**Parameters:** baseClass

-

Class

used to load the resource
**Parameters:** gifFile

- path to the image to load
**Returns:** a

UIDefaults.LazyValue

; when resolved the

LazyValue

loads the specified image
**See Also:** UIDefaults.LazyValue

,

Icon

,

Class.getResourceAsStream(String)

- getLayoutStyle

```java
public
LayoutStyle
getLayoutStyle()
```

Returns the

LayoutStyle

for this look
and feel. This never returns

null

.

You generally don't use the

LayoutStyle

from
the look and feel, instead use the

LayoutStyle

method

getInstance

.

**Returns:** the

LayoutStyle

for this look and feel
**Since:** 1.6
**See Also:** LayoutStyle.getInstance()

- provideErrorFeedback

```java
public void provideErrorFeedback​(
Component
component)
```

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus. The default implementation beeps. Subclasses
that wish different behavior should override this and provide
the additional feedback.

**Parameters:** component

- the

Component

the error occurred in,
may be

null

indicating the error condition is not directly
associated with a

Component
**Since:** 1.4

- getDesktopPropertyValue

```java
public static
Object
getDesktopPropertyValue​(
String
systemPropertyName,

Object
fallbackValue)
```

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.
If the value of the specified property is

null

,

fallbackValue

is returned.

**Parameters:** systemPropertyName

- the name of the system desktop property being queried
**Parameters:** fallbackValue

- the object to be returned as the value if the system value is null
**Returns:** the current value of the desktop property
**Since:** 1.4
**See Also:** Toolkit.getDesktopProperty(java.lang.String)

- getDisabledIcon

```java
public
Icon
getDisabledIcon​(
JComponent
component,

Icon
icon)
```

Returns an

Icon

with a disabled appearance.
This method is used to generate a disabled

Icon

when
one has not been specified. For example, if you create a

JButton

and only specify an

Icon

via

setIcon

this method will be called to generate the
disabled

Icon

. If

null

is passed as

icon

this method returns

null

.

Some look and feels might not render the disabled

Icon

, in which
case they will ignore this.

**Parameters:** component

-

JComponent

that will display the

Icon

,
may be

null
**Parameters:** icon

-

Icon

to generate the disabled icon from
**Returns:** disabled

Icon

, or

null

if a suitable

Icon

can not be generated
**Since:** 1.5

- getDisabledSelectedIcon

```java
public
Icon
getDisabledSelectedIcon​(
JComponent
component,

Icon
icon)
```

Returns an

Icon

for use by disabled
components that are also selected. This method is used to generate an

Icon

for components that are in both the disabled and
selected states but do not have a specific

Icon

for this
state. For example, if you create a

JButton

and only
specify an

Icon

via

setIcon

this method
will be called to generate the disabled and selected

Icon

. If

null

is passed as

icon

this
methods returns

null

.

Some look and feels might not render the disabled and selected

Icon

, in which case they will ignore this.

**Parameters:** component

-

JComponent

that will display the

Icon

,
may be

null
**Parameters:** icon

-

Icon

to generate disabled and selected icon from
**Returns:** disabled and selected icon, or

null

if a suitable

Icon

can not be generated.
**Since:** 1.5

- getName

```java
public abstract
String
getName()
```

Return a short string that identifies this look and feel, e.g.
"CDE/Motif". This string should be appropriate for a menu item.
Distinct look and feels should have different names, e.g.
a subclass of MotifLookAndFeel that changes the way a few components
are rendered should be called "CDE/Motif My Way"; something
that would be useful to a user trying to select a L&F from a list
of names.

**Returns:** short identifier for the look and feel

- getID

```java
public abstract
String
getID()
```

Return a string that identifies this look and feel. This string
will be used by applications/services that want to recognize
well known look and feel implementations. Presently
the well known names are "Motif", "Windows", "Mac", "Metal". Note
that a LookAndFeel derived from a well known superclass
that doesn't make any fundamental changes to the look or feel
shouldn't override this method.

**Returns:** identifier for the look and feel

- getDescription

```java
public abstract
String
getDescription()
```

Return a one line description of this look and feel implementation,
e.g. "The CDE/Motif Look and Feel". This string is intended for
the user, e.g. in the title of a window or in a ToolTip message.

**Returns:** short description for the look and feel

- getSupportsWindowDecorations

```java
public boolean getSupportsWindowDecorations()
```

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

The default implementation returns

false

, subclasses that
support

Window

decorations should override this and return

true

.

**Returns:** true

if the

RootPaneUI

instances created by
this look and feel support client side decorations
**Since:** 1.4
**See Also:** JDialog.setDefaultLookAndFeelDecorated(boolean)

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

,

JRootPane.setWindowDecorationStyle(int)

- isNativeLookAndFeel

```java
public abstract boolean isNativeLookAndFeel()
```

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

. For
example, when the underlying platform is Solaris running CDE
a CDE/Motif look and feel implementation would return

true

.

**Returns:** true

if this look and feel represents the underlying
platform look and feel

- isSupportedLookAndFeel

```java
public abstract boolean isSupportedLookAndFeel()
```

Return

true

if the underlying platform supports and or permits
this look and feel. This method returns

false

if the look
and feel depends on special resources or legal agreements that
aren't defined for the current platform.

**Returns:** true

if this is a supported look and feel
**See Also:** UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- initialize

```java
public void initialize()
```

Initializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when a
look and feel is installed as the current look and feel. This
method is invoked before the

UIManager

invokes

getDefaults

. This method is intended to perform any
initialization for the look and feel. Subclasses
should do any one-time setup they need here, rather than
in a static initializer, because look and feel class objects
may be loaded just to discover that

isSupportedLookAndFeel()

returns

false

.

**See Also:** uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- uninitialize

```java
public void uninitialize()
```

Uninitializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when
the look and feel is uninstalled. For example,

UIManager.setLookAndFeel

invokes this when the look and
feel is changed.

Subclasses may choose to free up some resources here.

**See Also:** initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the look and feel defaults. While this method is public,
it should only be invoked by the

UIManager

when the
look and feel is set as the current look and feel and after

initialize

has been invoked.

**Returns:** the look and feel defaults
**See Also:** initialize()

,

uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

Constructor Detail

- LookAndFeel

```java
public LookAndFeel()
```

---

#### Constructor Detail

LookAndFeel

```java
public LookAndFeel()
```

---

#### LookAndFeel

public LookAndFeel()

Method Detail

- installColors

```java
public static void installColors​(
JComponent
c,

String
defaultBgName,

String
defaultFgName)
```

Convenience method for setting a component's foreground
and background color properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:** c

- component to set the colors on
**Parameters:** defaultBgName

- key for the background
**Parameters:** defaultFgName

- key for the foreground
**Throws:** NullPointerException

- as described in

exceptions
**See Also:** installColorsAndFont(javax.swing.JComponent, java.lang.String, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

- installColorsAndFont

```java
public static void installColorsAndFont​(
JComponent
c,

String
defaultBgName,

String
defaultFgName,

String
defaultFontName)
```

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:** c

- component set to the colors and font on
**Parameters:** defaultBgName

- key for the background
**Parameters:** defaultFgName

- key for the foreground
**Parameters:** defaultFontName

- key for the font
**Throws:** NullPointerException

- as described in

exceptions
**See Also:** installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

,

UIManager.getFont(java.lang.Object)

- installBorder

```java
public static void installBorder​(
JComponent
c,

String
defaultBorderName)
```

Convenience method for setting a component's border property with
a value from the defaults. The border is only set if the border is

null

or an instance of

UIResource

.

**Parameters:** c

- component to set the border on
**Parameters:** defaultBorderName

- key specifying the border
**Throws:** NullPointerException

- as described in

exceptions

- uninstallBorder

```java
public static void uninstallBorder​(
JComponent
c)
```

Convenience method for uninstalling a border. If the border of
the component is a

UIResource

, it is set to

null

.

**Parameters:** c

- component to uninstall the border on
**Throws:** NullPointerException

- if

c

is

null

- installProperty

```java
public static void installProperty​(
JComponent
c,

String
propertyName,

Object
propertyValue)
```

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer. This method is intended to be used by
ui delegate instances that need to specify a default value for a
property of primitive type (boolean, int, ..), but do not wish
to override a value set by the client. Since primitive property
values cannot be wrapped with the

UIResource

marker, this method
uses private state to determine whether the property has been set
by the client.

**Parameters:** c

- target component to set the property on
**Parameters:** propertyName

- name of the property to set
**Parameters:** propertyValue

- value of the property
**Throws:** IllegalArgumentException

- if the specified property is not
one which can be set using this method
**Throws:** ClassCastException

- if the property value has not been set
by the developer and the type does not match the property's type
**Throws:** NullPointerException

- if

c

is

null

, or the
named property has not been set by the developer and

propertyValue

is

null
**Since:** 1.5

- makeKeyBindings

```java
public static
JTextComponent.KeyBinding
[] makeKeyBindings​(
Object
[] keyBindingList)
```

Convenience method for building an array of

KeyBindings

. While this method is not deprecated, developers
should instead use

ActionMap

and

InputMap

for
supplying key bindings.

This method returns an array of

KeyBindings

, one for each
alternating

key-action

pair in

keyBindingList

.
A

key

can either be a

String

in the format
specified by the

KeyStroke.getKeyStroke

method, or
a

KeyStroke

. The

action

part of the pair is a

String

that corresponds to the name of the

Action

.

The following example illustrates creating a

KeyBinding

array
from six alternating

key-action

pairs:

```java
JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});
```

If

keyBindingList's

length is odd, the last element is
ignored.

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

**Parameters:** keyBindingList

- an array of

key-action

pairs
**Returns:** an array of

KeyBindings
**Throws:** NullPointerException

- if

keyBindingList

is

null
**Throws:** ClassCastException

- if the

key

part of the pair is
not a

KeyStroke

or

String

, or the

action

part of the pair is not a

String
**See Also:** ActionMap

,

InputMap

,

KeyStroke.getKeyStroke(char)

- makeInputMap

```java
public static
InputMap
makeInputMap​(
Object
[] keys)
```

Creates an

InputMapUIResource

from

keys

. This is
a convenience method for creating a new

InputMapUIResource

,
invoking

loadKeyBindings(map, keys)

, and returning the

InputMapUIResource

.

**Parameters:** keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])
**Returns:** newly created and populated

InputMapUIResource
**Since:** 1.3
**See Also:** loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

- makeComponentInputMap

```java
public static
ComponentInputMap
makeComponentInputMap​(
JComponent
c,

Object
[] keys)
```

Creates a

ComponentInputMapUIResource

from

keys

. This is a convenience method for creating a
new

ComponentInputMapUIResource

, invoking

loadKeyBindings(map, keys)

, and returning the

ComponentInputMapUIResource

.

**Parameters:** c

- component to create the

ComponentInputMapUIResource

with
**Parameters:** keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])
**Returns:** newly created and populated

InputMapUIResource
**Throws:** IllegalArgumentException

- if

c

is

null
**Since:** 1.3
**See Also:** loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

,

ComponentInputMapUIResource

- loadKeyBindings

```java
public static void loadKeyBindings​(
InputMap
retMap,

Object
[] keys)
```

Populates an

InputMap

with the specified bindings.
The bindings are supplied as a list of alternating

keystroke-action key

pairs. The

keystroke

is either
an instance of

KeyStroke

, or a

String

that identifies the

KeyStroke

for the binding. Refer
to

KeyStroke.getKeyStroke(String)

for the specific
format. The

action key

part of the pair is the key
registered in the

InputMap

for the

KeyStroke

.

The following illustrates loading an

InputMap

with two

key-action

pairs:

```java
LookAndFeel.loadKeyBindings(inputMap, new Object[] {
"control X", "cut",
"control V", "paste"
});
```

Supplying a

null

list of bindings (

keys

) does not
change

retMap

in any way.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

**Parameters:** retMap

-

InputMap

to add the

key-action

pairs to
**Parameters:** keys

- bindings to add to

retMap
**Throws:** NullPointerException

- if

keys

is

non-null

, not empty, and

retMap

is

null
**Since:** 1.3
**See Also:** KeyStroke.getKeyStroke(String)

,

InputMap

- makeIcon

```java
public static
Object
makeIcon​(
Class
<?> baseClass,

String
gifFile)
```

Creates and returns a

UIDefault.LazyValue

that loads an
image. The returned value is an implementation of

UIDefaults.LazyValue

. When

createValue

is invoked on
the returned object, the image is loaded. If the image is

non-null

, it is then wrapped in an

Icon

that implements

UIResource

. The image is loaded using

Class.getResourceAsStream(gifFile)

.

This method does not check the arguments in any way. It is
strongly recommended that

non-null

values are supplied else
exceptions may occur when

createValue

is invoked on the
returned object.

**Parameters:** baseClass

-

Class

used to load the resource
**Parameters:** gifFile

- path to the image to load
**Returns:** a

UIDefaults.LazyValue

; when resolved the

LazyValue

loads the specified image
**See Also:** UIDefaults.LazyValue

,

Icon

,

Class.getResourceAsStream(String)

- getLayoutStyle

```java
public
LayoutStyle
getLayoutStyle()
```

Returns the

LayoutStyle

for this look
and feel. This never returns

null

.

You generally don't use the

LayoutStyle

from
the look and feel, instead use the

LayoutStyle

method

getInstance

.

**Returns:** the

LayoutStyle

for this look and feel
**Since:** 1.6
**See Also:** LayoutStyle.getInstance()

- provideErrorFeedback

```java
public void provideErrorFeedback​(
Component
component)
```

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus. The default implementation beeps. Subclasses
that wish different behavior should override this and provide
the additional feedback.

**Parameters:** component

- the

Component

the error occurred in,
may be

null

indicating the error condition is not directly
associated with a

Component
**Since:** 1.4

- getDesktopPropertyValue

```java
public static
Object
getDesktopPropertyValue​(
String
systemPropertyName,

Object
fallbackValue)
```

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.
If the value of the specified property is

null

,

fallbackValue

is returned.

**Parameters:** systemPropertyName

- the name of the system desktop property being queried
**Parameters:** fallbackValue

- the object to be returned as the value if the system value is null
**Returns:** the current value of the desktop property
**Since:** 1.4
**See Also:** Toolkit.getDesktopProperty(java.lang.String)

- getDisabledIcon

```java
public
Icon
getDisabledIcon​(
JComponent
component,

Icon
icon)
```

Returns an

Icon

with a disabled appearance.
This method is used to generate a disabled

Icon

when
one has not been specified. For example, if you create a

JButton

and only specify an

Icon

via

setIcon

this method will be called to generate the
disabled

Icon

. If

null

is passed as

icon

this method returns

null

.

Some look and feels might not render the disabled

Icon

, in which
case they will ignore this.

**Parameters:** component

-

JComponent

that will display the

Icon

,
may be

null
**Parameters:** icon

-

Icon

to generate the disabled icon from
**Returns:** disabled

Icon

, or

null

if a suitable

Icon

can not be generated
**Since:** 1.5

- getDisabledSelectedIcon

```java
public
Icon
getDisabledSelectedIcon​(
JComponent
component,

Icon
icon)
```

Returns an

Icon

for use by disabled
components that are also selected. This method is used to generate an

Icon

for components that are in both the disabled and
selected states but do not have a specific

Icon

for this
state. For example, if you create a

JButton

and only
specify an

Icon

via

setIcon

this method
will be called to generate the disabled and selected

Icon

. If

null

is passed as

icon

this
methods returns

null

.

Some look and feels might not render the disabled and selected

Icon

, in which case they will ignore this.

**Parameters:** component

-

JComponent

that will display the

Icon

,
may be

null
**Parameters:** icon

-

Icon

to generate disabled and selected icon from
**Returns:** disabled and selected icon, or

null

if a suitable

Icon

can not be generated.
**Since:** 1.5

- getName

```java
public abstract
String
getName()
```

Return a short string that identifies this look and feel, e.g.
"CDE/Motif". This string should be appropriate for a menu item.
Distinct look and feels should have different names, e.g.
a subclass of MotifLookAndFeel that changes the way a few components
are rendered should be called "CDE/Motif My Way"; something
that would be useful to a user trying to select a L&F from a list
of names.

**Returns:** short identifier for the look and feel

- getID

```java
public abstract
String
getID()
```

Return a string that identifies this look and feel. This string
will be used by applications/services that want to recognize
well known look and feel implementations. Presently
the well known names are "Motif", "Windows", "Mac", "Metal". Note
that a LookAndFeel derived from a well known superclass
that doesn't make any fundamental changes to the look or feel
shouldn't override this method.

**Returns:** identifier for the look and feel

- getDescription

```java
public abstract
String
getDescription()
```

Return a one line description of this look and feel implementation,
e.g. "The CDE/Motif Look and Feel". This string is intended for
the user, e.g. in the title of a window or in a ToolTip message.

**Returns:** short description for the look and feel

- getSupportsWindowDecorations

```java
public boolean getSupportsWindowDecorations()
```

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

The default implementation returns

false

, subclasses that
support

Window

decorations should override this and return

true

.

**Returns:** true

if the

RootPaneUI

instances created by
this look and feel support client side decorations
**Since:** 1.4
**See Also:** JDialog.setDefaultLookAndFeelDecorated(boolean)

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

,

JRootPane.setWindowDecorationStyle(int)

- isNativeLookAndFeel

```java
public abstract boolean isNativeLookAndFeel()
```

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

. For
example, when the underlying platform is Solaris running CDE
a CDE/Motif look and feel implementation would return

true

.

**Returns:** true

if this look and feel represents the underlying
platform look and feel

- isSupportedLookAndFeel

```java
public abstract boolean isSupportedLookAndFeel()
```

Return

true

if the underlying platform supports and or permits
this look and feel. This method returns

false

if the look
and feel depends on special resources or legal agreements that
aren't defined for the current platform.

**Returns:** true

if this is a supported look and feel
**See Also:** UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- initialize

```java
public void initialize()
```

Initializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when a
look and feel is installed as the current look and feel. This
method is invoked before the

UIManager

invokes

getDefaults

. This method is intended to perform any
initialization for the look and feel. Subclasses
should do any one-time setup they need here, rather than
in a static initializer, because look and feel class objects
may be loaded just to discover that

isSupportedLookAndFeel()

returns

false

.

**See Also:** uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- uninitialize

```java
public void uninitialize()
```

Uninitializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when
the look and feel is uninstalled. For example,

UIManager.setLookAndFeel

invokes this when the look and
feel is changed.

Subclasses may choose to free up some resources here.

**See Also:** initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the look and feel defaults. While this method is public,
it should only be invoked by the

UIManager

when the
look and feel is set as the current look and feel and after

initialize

has been invoked.

**Returns:** the look and feel defaults
**See Also:** initialize()

,

uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

---

#### Method Detail

installColors

```java
public static void installColors​(
JComponent
c,

String
defaultBgName,

String
defaultFgName)
```

Convenience method for setting a component's foreground
and background color properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:** c

- component to set the colors on
**Parameters:** defaultBgName

- key for the background
**Parameters:** defaultFgName

- key for the foreground
**Throws:** NullPointerException

- as described in

exceptions
**See Also:** installColorsAndFont(javax.swing.JComponent, java.lang.String, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

---

#### installColors

public static void installColors​(

JComponent

c,

String

defaultBgName,

String

defaultFgName)

Convenience method for setting a component's foreground
and background color properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

installColorsAndFont

```java
public static void installColorsAndFont​(
JComponent
c,

String
defaultBgName,

String
defaultFgName,

String
defaultFontName)
```

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

**Parameters:** c

- component set to the colors and font on
**Parameters:** defaultBgName

- key for the background
**Parameters:** defaultFgName

- key for the foreground
**Parameters:** defaultFontName

- key for the font
**Throws:** NullPointerException

- as described in

exceptions
**See Also:** installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

,

UIManager.getColor(java.lang.Object)

,

UIManager.getFont(java.lang.Object)

---

#### installColorsAndFont

public static void installColorsAndFont​(

JComponent

c,

String

defaultBgName,

String

defaultFgName,

String

defaultFontName)

Convenience method for setting a component's foreground,
background and font properties with values from the
defaults. The properties are only set if the current
value is either

null

or a

UIResource

.

installBorder

```java
public static void installBorder​(
JComponent
c,

String
defaultBorderName)
```

Convenience method for setting a component's border property with
a value from the defaults. The border is only set if the border is

null

or an instance of

UIResource

.

**Parameters:** c

- component to set the border on
**Parameters:** defaultBorderName

- key specifying the border
**Throws:** NullPointerException

- as described in

exceptions

---

#### installBorder

public static void installBorder​(

JComponent

c,

String

defaultBorderName)

Convenience method for setting a component's border property with
a value from the defaults. The border is only set if the border is

null

or an instance of

UIResource

.

uninstallBorder

```java
public static void uninstallBorder​(
JComponent
c)
```

Convenience method for uninstalling a border. If the border of
the component is a

UIResource

, it is set to

null

.

**Parameters:** c

- component to uninstall the border on
**Throws:** NullPointerException

- if

c

is

null

---

#### uninstallBorder

public static void uninstallBorder​(

JComponent

c)

Convenience method for uninstalling a border. If the border of
the component is a

UIResource

, it is set to

null

.

installProperty

```java
public static void installProperty​(
JComponent
c,

String
propertyName,

Object
propertyValue)
```

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer. This method is intended to be used by
ui delegate instances that need to specify a default value for a
property of primitive type (boolean, int, ..), but do not wish
to override a value set by the client. Since primitive property
values cannot be wrapped with the

UIResource

marker, this method
uses private state to determine whether the property has been set
by the client.

**Parameters:** c

- target component to set the property on
**Parameters:** propertyName

- name of the property to set
**Parameters:** propertyValue

- value of the property
**Throws:** IllegalArgumentException

- if the specified property is not
one which can be set using this method
**Throws:** ClassCastException

- if the property value has not been set
by the developer and the type does not match the property's type
**Throws:** NullPointerException

- if

c

is

null

, or the
named property has not been set by the developer and

propertyValue

is

null
**Since:** 1.5

---

#### installProperty

public static void installProperty​(

JComponent

c,

String

propertyName,

Object

propertyValue)

Convenience method for installing a property with the specified name
and value on a component if that property has not already been set
by the developer. This method is intended to be used by
ui delegate instances that need to specify a default value for a
property of primitive type (boolean, int, ..), but do not wish
to override a value set by the client. Since primitive property
values cannot be wrapped with the

UIResource

marker, this method
uses private state to determine whether the property has been set
by the client.

makeKeyBindings

```java
public static
JTextComponent.KeyBinding
[] makeKeyBindings​(
Object
[] keyBindingList)
```

Convenience method for building an array of

KeyBindings

. While this method is not deprecated, developers
should instead use

ActionMap

and

InputMap

for
supplying key bindings.

This method returns an array of

KeyBindings

, one for each
alternating

key-action

pair in

keyBindingList

.
A

key

can either be a

String

in the format
specified by the

KeyStroke.getKeyStroke

method, or
a

KeyStroke

. The

action

part of the pair is a

String

that corresponds to the name of the

Action

.

The following example illustrates creating a

KeyBinding

array
from six alternating

key-action

pairs:

```java
JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});
```

If

keyBindingList's

length is odd, the last element is
ignored.

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

**Parameters:** keyBindingList

- an array of

key-action

pairs
**Returns:** an array of

KeyBindings
**Throws:** NullPointerException

- if

keyBindingList

is

null
**Throws:** ClassCastException

- if the

key

part of the pair is
not a

KeyStroke

or

String

, or the

action

part of the pair is not a

String
**See Also:** ActionMap

,

InputMap

,

KeyStroke.getKeyStroke(char)

---

#### makeKeyBindings

public static

JTextComponent.KeyBinding

[] makeKeyBindings​(

Object

[] keyBindingList)

Convenience method for building an array of

KeyBindings

. While this method is not deprecated, developers
should instead use

ActionMap

and

InputMap

for
supplying key bindings.

This method returns an array of

KeyBindings

, one for each
alternating

key-action

pair in

keyBindingList

.
A

key

can either be a

String

in the format
specified by the

KeyStroke.getKeyStroke

method, or
a

KeyStroke

. The

action

part of the pair is a

String

that corresponds to the name of the

Action

.

The following example illustrates creating a

KeyBinding

array
from six alternating

key-action

pairs:

```java
JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});
```

If

keyBindingList's

length is odd, the last element is
ignored.

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

This method returns an array of

KeyBindings

, one for each
alternating

key-action

pair in

keyBindingList

.
A

key

can either be a

String

in the format
specified by the

KeyStroke.getKeyStroke

method, or
a

KeyStroke

. The

action

part of the pair is a

String

that corresponds to the name of the

Action

.

The following example illustrates creating a

KeyBinding

array
from six alternating

key-action

pairs:

```java
JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});
```

If

keyBindingList's

length is odd, the last element is
ignored.

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

The following example illustrates creating a

KeyBinding

array
from six alternating

key-action

pairs:

```java
JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});
```

If

keyBindingList's

length is odd, the last element is
ignored.

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

JTextComponent.KeyBinding[] multilineBindings = makeKeyBindings( new Object[] {
"UP", DefaultEditorKit.upAction,
"DOWN", DefaultEditorKit.downAction,
"PAGE_UP", DefaultEditorKit.pageUpAction,
"PAGE_DOWN", DefaultEditorKit.pageDownAction,
"ENTER", DefaultEditorKit.insertBreakAction,
"TAB", DefaultEditorKit.insertTabAction
});

Supplying a

null

value for either the

key

or

action

part of the

key-action

pair results in
creating a

KeyBinding

with the corresponding value

null

. As other parts of Swing's expect

non-null

values
in a

KeyBinding

, you should avoid supplying

null

as
either the

key

or

action

part of the

key-action

pair.

makeInputMap

```java
public static
InputMap
makeInputMap​(
Object
[] keys)
```

Creates an

InputMapUIResource

from

keys

. This is
a convenience method for creating a new

InputMapUIResource

,
invoking

loadKeyBindings(map, keys)

, and returning the

InputMapUIResource

.

**Parameters:** keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])
**Returns:** newly created and populated

InputMapUIResource
**Since:** 1.3
**See Also:** loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

---

#### makeInputMap

public static

InputMap

makeInputMap​(

Object

[] keys)

Creates an

InputMapUIResource

from

keys

. This is
a convenience method for creating a new

InputMapUIResource

,
invoking

loadKeyBindings(map, keys)

, and returning the

InputMapUIResource

.

makeComponentInputMap

```java
public static
ComponentInputMap
makeComponentInputMap​(
JComponent
c,

Object
[] keys)
```

Creates a

ComponentInputMapUIResource

from

keys

. This is a convenience method for creating a
new

ComponentInputMapUIResource

, invoking

loadKeyBindings(map, keys)

, and returning the

ComponentInputMapUIResource

.

**Parameters:** c

- component to create the

ComponentInputMapUIResource

with
**Parameters:** keys

- alternating pairs of

keystroke-action key

pairs as described in

loadKeyBindings(javax.swing.InputMap, java.lang.Object[])
**Returns:** newly created and populated

InputMapUIResource
**Throws:** IllegalArgumentException

- if

c

is

null
**Since:** 1.3
**See Also:** loadKeyBindings(javax.swing.InputMap, java.lang.Object[])

,

ComponentInputMapUIResource

---

#### makeComponentInputMap

public static

ComponentInputMap

makeComponentInputMap​(

JComponent

c,

Object

[] keys)

Creates a

ComponentInputMapUIResource

from

keys

. This is a convenience method for creating a
new

ComponentInputMapUIResource

, invoking

loadKeyBindings(map, keys)

, and returning the

ComponentInputMapUIResource

.

loadKeyBindings

```java
public static void loadKeyBindings​(
InputMap
retMap,

Object
[] keys)
```

Populates an

InputMap

with the specified bindings.
The bindings are supplied as a list of alternating

keystroke-action key

pairs. The

keystroke

is either
an instance of

KeyStroke

, or a

String

that identifies the

KeyStroke

for the binding. Refer
to

KeyStroke.getKeyStroke(String)

for the specific
format. The

action key

part of the pair is the key
registered in the

InputMap

for the

KeyStroke

.

The following illustrates loading an

InputMap

with two

key-action

pairs:

```java
LookAndFeel.loadKeyBindings(inputMap, new Object[] {
"control X", "cut",
"control V", "paste"
});
```

Supplying a

null

list of bindings (

keys

) does not
change

retMap

in any way.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

**Parameters:** retMap

-

InputMap

to add the

key-action

pairs to
**Parameters:** keys

- bindings to add to

retMap
**Throws:** NullPointerException

- if

keys

is

non-null

, not empty, and

retMap

is

null
**Since:** 1.3
**See Also:** KeyStroke.getKeyStroke(String)

,

InputMap

---

#### loadKeyBindings

public static void loadKeyBindings​(

InputMap

retMap,

Object

[] keys)

Populates an

InputMap

with the specified bindings.
The bindings are supplied as a list of alternating

keystroke-action key

pairs. The

keystroke

is either
an instance of

KeyStroke

, or a

String

that identifies the

KeyStroke

for the binding. Refer
to

KeyStroke.getKeyStroke(String)

for the specific
format. The

action key

part of the pair is the key
registered in the

InputMap

for the

KeyStroke

.

The following illustrates loading an

InputMap

with two

key-action

pairs:

```java
LookAndFeel.loadKeyBindings(inputMap, new Object[] {
"control X", "cut",
"control V", "paste"
});
```

Supplying a

null

list of bindings (

keys

) does not
change

retMap

in any way.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

The following illustrates loading an

InputMap

with two

key-action

pairs:

```java
LookAndFeel.loadKeyBindings(inputMap, new Object[] {
"control X", "cut",
"control V", "paste"
});
```

Supplying a

null

list of bindings (

keys

) does not
change

retMap

in any way.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

LookAndFeel.loadKeyBindings(inputMap, new Object[] {
"control X", "cut",
"control V", "paste"
});

Supplying a

null

list of bindings (

keys

) does not
change

retMap

in any way.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

Specifying a

null

action key

results in
removing the

keystroke's

entry from the

InputMap

.
A

null

keystroke

is ignored.

makeIcon

```java
public static
Object
makeIcon​(
Class
<?> baseClass,

String
gifFile)
```

Creates and returns a

UIDefault.LazyValue

that loads an
image. The returned value is an implementation of

UIDefaults.LazyValue

. When

createValue

is invoked on
the returned object, the image is loaded. If the image is

non-null

, it is then wrapped in an

Icon

that implements

UIResource

. The image is loaded using

Class.getResourceAsStream(gifFile)

.

This method does not check the arguments in any way. It is
strongly recommended that

non-null

values are supplied else
exceptions may occur when

createValue

is invoked on the
returned object.

**Parameters:** baseClass

-

Class

used to load the resource
**Parameters:** gifFile

- path to the image to load
**Returns:** a

UIDefaults.LazyValue

; when resolved the

LazyValue

loads the specified image
**See Also:** UIDefaults.LazyValue

,

Icon

,

Class.getResourceAsStream(String)

---

#### makeIcon

public static

Object

makeIcon​(

Class

<?> baseClass,

String

gifFile)

Creates and returns a

UIDefault.LazyValue

that loads an
image. The returned value is an implementation of

UIDefaults.LazyValue

. When

createValue

is invoked on
the returned object, the image is loaded. If the image is

non-null

, it is then wrapped in an

Icon

that implements

UIResource

. The image is loaded using

Class.getResourceAsStream(gifFile)

.

This method does not check the arguments in any way. It is
strongly recommended that

non-null

values are supplied else
exceptions may occur when

createValue

is invoked on the
returned object.

This method does not check the arguments in any way. It is
strongly recommended that

non-null

values are supplied else
exceptions may occur when

createValue

is invoked on the
returned object.

getLayoutStyle

```java
public
LayoutStyle
getLayoutStyle()
```

Returns the

LayoutStyle

for this look
and feel. This never returns

null

.

You generally don't use the

LayoutStyle

from
the look and feel, instead use the

LayoutStyle

method

getInstance

.

**Returns:** the

LayoutStyle

for this look and feel
**Since:** 1.6
**See Also:** LayoutStyle.getInstance()

---

#### getLayoutStyle

public

LayoutStyle

getLayoutStyle()

Returns the

LayoutStyle

for this look
and feel. This never returns

null

.

You generally don't use the

LayoutStyle

from
the look and feel, instead use the

LayoutStyle

method

getInstance

.

You generally don't use the

LayoutStyle

from
the look and feel, instead use the

LayoutStyle

method

getInstance

.

provideErrorFeedback

```java
public void provideErrorFeedback​(
Component
component)
```

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus. The default implementation beeps. Subclasses
that wish different behavior should override this and provide
the additional feedback.

**Parameters:** component

- the

Component

the error occurred in,
may be

null

indicating the error condition is not directly
associated with a

Component
**Since:** 1.4

---

#### provideErrorFeedback

public void provideErrorFeedback​(

Component

component)

Invoked when the user attempts an invalid operation,
such as pasting into an uneditable

JTextField

that has focus. The default implementation beeps. Subclasses
that wish different behavior should override this and provide
the additional feedback.

getDesktopPropertyValue

```java
public static
Object
getDesktopPropertyValue​(
String
systemPropertyName,

Object
fallbackValue)
```

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.
If the value of the specified property is

null

,

fallbackValue

is returned.

**Parameters:** systemPropertyName

- the name of the system desktop property being queried
**Parameters:** fallbackValue

- the object to be returned as the value if the system value is null
**Returns:** the current value of the desktop property
**Since:** 1.4
**See Also:** Toolkit.getDesktopProperty(java.lang.String)

---

#### getDesktopPropertyValue

public static

Object

getDesktopPropertyValue​(

String

systemPropertyName,

Object

fallbackValue)

Returns the value of the specified system desktop property by
invoking

Toolkit.getDefaultToolkit().getDesktopProperty()

.
If the value of the specified property is

null

,

fallbackValue

is returned.

getDisabledIcon

```java
public
Icon
getDisabledIcon​(
JComponent
component,

Icon
icon)
```

Returns an

Icon

with a disabled appearance.
This method is used to generate a disabled

Icon

when
one has not been specified. For example, if you create a

JButton

and only specify an

Icon

via

setIcon

this method will be called to generate the
disabled

Icon

. If

null

is passed as

icon

this method returns

null

.

Some look and feels might not render the disabled

Icon

, in which
case they will ignore this.

**Parameters:** component

-

JComponent

that will display the

Icon

,
may be

null
**Parameters:** icon

-

Icon

to generate the disabled icon from
**Returns:** disabled

Icon

, or

null

if a suitable

Icon

can not be generated
**Since:** 1.5

---

#### getDisabledIcon

public

Icon

getDisabledIcon​(

JComponent

component,

Icon

icon)

Returns an

Icon

with a disabled appearance.
This method is used to generate a disabled

Icon

when
one has not been specified. For example, if you create a

JButton

and only specify an

Icon

via

setIcon

this method will be called to generate the
disabled

Icon

. If

null

is passed as

icon

this method returns

null

.

Some look and feels might not render the disabled

Icon

, in which
case they will ignore this.

Some look and feels might not render the disabled

Icon

, in which
case they will ignore this.

getDisabledSelectedIcon

```java
public
Icon
getDisabledSelectedIcon​(
JComponent
component,

Icon
icon)
```

Returns an

Icon

for use by disabled
components that are also selected. This method is used to generate an

Icon

for components that are in both the disabled and
selected states but do not have a specific

Icon

for this
state. For example, if you create a

JButton

and only
specify an

Icon

via

setIcon

this method
will be called to generate the disabled and selected

Icon

. If

null

is passed as

icon

this
methods returns

null

.

Some look and feels might not render the disabled and selected

Icon

, in which case they will ignore this.

**Parameters:** component

-

JComponent

that will display the

Icon

,
may be

null
**Parameters:** icon

-

Icon

to generate disabled and selected icon from
**Returns:** disabled and selected icon, or

null

if a suitable

Icon

can not be generated.
**Since:** 1.5

---

#### getDisabledSelectedIcon

public

Icon

getDisabledSelectedIcon​(

JComponent

component,

Icon

icon)

Returns an

Icon

for use by disabled
components that are also selected. This method is used to generate an

Icon

for components that are in both the disabled and
selected states but do not have a specific

Icon

for this
state. For example, if you create a

JButton

and only
specify an

Icon

via

setIcon

this method
will be called to generate the disabled and selected

Icon

. If

null

is passed as

icon

this
methods returns

null

.

Some look and feels might not render the disabled and selected

Icon

, in which case they will ignore this.

Some look and feels might not render the disabled and selected

Icon

, in which case they will ignore this.

getName

```java
public abstract
String
getName()
```

Return a short string that identifies this look and feel, e.g.
"CDE/Motif". This string should be appropriate for a menu item.
Distinct look and feels should have different names, e.g.
a subclass of MotifLookAndFeel that changes the way a few components
are rendered should be called "CDE/Motif My Way"; something
that would be useful to a user trying to select a L&F from a list
of names.

**Returns:** short identifier for the look and feel

---

#### getName

public abstract

String

getName()

Return a short string that identifies this look and feel, e.g.
"CDE/Motif". This string should be appropriate for a menu item.
Distinct look and feels should have different names, e.g.
a subclass of MotifLookAndFeel that changes the way a few components
are rendered should be called "CDE/Motif My Way"; something
that would be useful to a user trying to select a L&F from a list
of names.

getID

```java
public abstract
String
getID()
```

Return a string that identifies this look and feel. This string
will be used by applications/services that want to recognize
well known look and feel implementations. Presently
the well known names are "Motif", "Windows", "Mac", "Metal". Note
that a LookAndFeel derived from a well known superclass
that doesn't make any fundamental changes to the look or feel
shouldn't override this method.

**Returns:** identifier for the look and feel

---

#### getID

public abstract

String

getID()

Return a string that identifies this look and feel. This string
will be used by applications/services that want to recognize
well known look and feel implementations. Presently
the well known names are "Motif", "Windows", "Mac", "Metal". Note
that a LookAndFeel derived from a well known superclass
that doesn't make any fundamental changes to the look or feel
shouldn't override this method.

getDescription

```java
public abstract
String
getDescription()
```

Return a one line description of this look and feel implementation,
e.g. "The CDE/Motif Look and Feel". This string is intended for
the user, e.g. in the title of a window or in a ToolTip message.

**Returns:** short description for the look and feel

---

#### getDescription

public abstract

String

getDescription()

Return a one line description of this look and feel implementation,
e.g. "The CDE/Motif Look and Feel". This string is intended for
the user, e.g. in the title of a window or in a ToolTip message.

getSupportsWindowDecorations

```java
public boolean getSupportsWindowDecorations()
```

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

The default implementation returns

false

, subclasses that
support

Window

decorations should override this and return

true

.

**Returns:** true

if the

RootPaneUI

instances created by
this look and feel support client side decorations
**Since:** 1.4
**See Also:** JDialog.setDefaultLookAndFeelDecorated(boolean)

,

JFrame.setDefaultLookAndFeelDecorated(boolean)

,

JRootPane.setWindowDecorationStyle(int)

---

#### getSupportsWindowDecorations

public boolean getSupportsWindowDecorations()

Returns

true

if the

LookAndFeel

returned

RootPaneUI

instances support providing

Window

decorations in a

JRootPane

.

The default implementation returns

false

, subclasses that
support

Window

decorations should override this and return

true

.

The default implementation returns

false

, subclasses that
support

Window

decorations should override this and return

true

.

isNativeLookAndFeel

```java
public abstract boolean isNativeLookAndFeel()
```

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

. For
example, when the underlying platform is Solaris running CDE
a CDE/Motif look and feel implementation would return

true

.

**Returns:** true

if this look and feel represents the underlying
platform look and feel

---

#### isNativeLookAndFeel

public abstract boolean isNativeLookAndFeel()

If the underlying platform has a "native" look and feel, and
this is an implementation of it, return

true

. For
example, when the underlying platform is Solaris running CDE
a CDE/Motif look and feel implementation would return

true

.

isSupportedLookAndFeel

```java
public abstract boolean isSupportedLookAndFeel()
```

Return

true

if the underlying platform supports and or permits
this look and feel. This method returns

false

if the look
and feel depends on special resources or legal agreements that
aren't defined for the current platform.

**Returns:** true

if this is a supported look and feel
**See Also:** UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### isSupportedLookAndFeel

public abstract boolean isSupportedLookAndFeel()

Return

true

if the underlying platform supports and or permits
this look and feel. This method returns

false

if the look
and feel depends on special resources or legal agreements that
aren't defined for the current platform.

initialize

```java
public void initialize()
```

Initializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when a
look and feel is installed as the current look and feel. This
method is invoked before the

UIManager

invokes

getDefaults

. This method is intended to perform any
initialization for the look and feel. Subclasses
should do any one-time setup they need here, rather than
in a static initializer, because look and feel class objects
may be loaded just to discover that

isSupportedLookAndFeel()

returns

false

.

**See Also:** uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### initialize

public void initialize()

Initializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when a
look and feel is installed as the current look and feel. This
method is invoked before the

UIManager

invokes

getDefaults

. This method is intended to perform any
initialization for the look and feel. Subclasses
should do any one-time setup they need here, rather than
in a static initializer, because look and feel class objects
may be loaded just to discover that

isSupportedLookAndFeel()

returns

false

.

uninitialize

```java
public void uninitialize()
```

Uninitializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when
the look and feel is uninstalled. For example,

UIManager.setLookAndFeel

invokes this when the look and
feel is changed.

Subclasses may choose to free up some resources here.

**See Also:** initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### uninitialize

public void uninitialize()

Uninitializes the look and feel. While this method is public,
it should only be invoked by the

UIManager

when
the look and feel is uninstalled. For example,

UIManager.setLookAndFeel

invokes this when the look and
feel is changed.

Subclasses may choose to free up some resources here.

Subclasses may choose to free up some resources here.

getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the look and feel defaults. While this method is public,
it should only be invoked by the

UIManager

when the
look and feel is set as the current look and feel and after

initialize

has been invoked.

**Returns:** the look and feel defaults
**See Also:** initialize()

,

uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### getDefaults

public

UIDefaults

getDefaults()

Returns the look and feel defaults. While this method is public,
it should only be invoked by the

UIManager

when the
look and feel is set as the current look and feel and after

initialize

has been invoked.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

---

