# Class BasicLookAndFeel

**Source:** `java.desktop\javax\swing\plaf\basic\BasicLookAndFeel.html`

### Class Description

```java
public abstract class
BasicLookAndFeel

extends
LookAndFeel

implements
Serializable
```

A base class to use in creating a look and feel for Swing.

Each of the

ComponentUI

s provided by

BasicLookAndFeel

derives its behavior from the defaults
table. Unless otherwise noted each of the

ComponentUI

implementations in this package document the set of defaults they
use. Unless otherwise noted the defaults are installed at the time

installUI

is invoked, and follow the recommendations
outlined in

LookAndFeel

for installing defaults.

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

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicLookAndFeel()

*No description found.*

---

### Method Details

#### public
UIDefaults
getDefaults()

Returns the look and feel defaults. The returned

UIDefaults

is populated by invoking, in order,

initClassDefaults

,

initSystemColorDefaults

and

initComponentDefaults

.

While this method is public, it should only be invoked by the

UIManager

when the look and feel is set as the current
look and feel and after

initialize

has been invoked.

**Overrides:**
- getDefaults

in class

LookAndFeel

**Returns:**
- the look and feel defaults

**See Also:**
- initClassDefaults(javax.swing.UIDefaults)

,

initSystemColorDefaults(javax.swing.UIDefaults)

,

initComponentDefaults(javax.swing.UIDefaults)

---

#### protected void initClassDefaults​(
UIDefaults
table)

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class. The value for a
particular

uiClassID

is

"javax.swing.plaf.basic.Basic + uiClassID"

. For example, the
value for the

uiClassID

TreeUI

is

"javax.swing.plaf.basic.BasicTreeUI"

.

**Parameters:**
- table

- the

UIDefaults

instance the entries are
added to

**Throws:**
- NullPointerException

- if

table

is

null

**See Also:**
- LookAndFeel

,

getDefaults()

---

#### protected void initSystemColorDefaults​(
UIDefaults
table)

Populates

table

with system colors. This creates an
array of

name-color

pairs and invokes

loadSystemColors

.

The name is a

String

that corresponds to the name of
one of the static

SystemColor

fields in the

SystemColor

class. A name-color pair is created for every
such

SystemColor

field.

The

color

corresponds to a hex

String

as
understood by

Color.decode

. For example, one of the

name-color

pairs is

"desktop"-"#005C5C"

. This corresponds to the

SystemColor

field

desktop

, with a color value of

new Color(0x005C5C)

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

**Parameters:**
- table

- the

UIDefaults

object the values are added to

**Throws:**
- NullPointerException

- if

table

is

null

**See Also:**
- SystemColor

,

getDefaults()

,

loadSystemColors(javax.swing.UIDefaults, java.lang.String[], boolean)

---

#### protected void loadSystemColors​(
UIDefaults
table,

String
[] systemColors,
boolean useNative)

Populates

table

with the

name-color

pairs in

systemColors

. Refer to

initSystemColorDefaults(UIDefaults)

for details on
the format of

systemColors

.

An entry is added to

table

for each of the

name-color

pairs in

systemColors

. The entry key is
the

name

of the

name-color

pair.

The value of the entry corresponds to the

color

of the

name-color

pair. The value of the entry is calculated
in one of two ways. With either approach the value is always a

ColorUIResource

.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

**Parameters:**
- table

- the

UIDefaults

object the values are added to
- systemColors

- array of

name-color

pairs as described
in

initSystemColorDefaults(UIDefaults)
- useNative

- whether the color is obtained from

SystemColor

or

Color.decode

**Throws:**
- NullPointerException

- if

systemColors

is

null

; or

systemColors

is not empty, and

table

is

null

; or one of the
names of the

name-color

pairs is

null

; or

useNative

is

false

and one of the

colors

of the

name-color

pairs is

null
- ArrayIndexOutOfBoundsException

- if

useNative

is

false

and

systemColors.length

is odd

**See Also:**
- initSystemColorDefaults(javax.swing.UIDefaults)

,

SystemColor

,

Color.decode(String)

---

#### protected void initComponentDefaults​(
UIDefaults
table)

Populates

table

with the defaults for the basic look and
feel.

**Parameters:**
- table

- the

UIDefaults

to add the values to

**Throws:**
- NullPointerException

- if

table

is

null

---

#### protected
ActionMap
getAudioActionMap()

Returns an

ActionMap

containing the audio actions
for this look and feel.

The returned

ActionMap

contains

Actions

that
embody the ability to render an auditory cue. These auditory
cues map onto user and system activities that may be useful
for an end user to know about (such as a dialog box appearing).

At the appropriate time,
the

ComponentUI

is responsible for obtaining an

Action

out of the

ActionMap

and passing
it to

playSound

.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

**Returns:**
- an ActionMap containing

Actions

responsible for playing auditory cues

**Throws:**
- ClassCastException

- if the value of the
default

"AuditoryCues.actionMap"

is not an

ActionMap

, or the value of the default

"AuditoryCues.cueList"

is not an

Object[]

**See Also:**
- createAudioAction(java.lang.Object)

,

playSound(Action)

**Since:**
- 1.4

---

#### protected
Action
createAudioAction​(
Object
key)

Creates and returns an

Action

used to play a sound.

If

key

is

non-null

, an

Action

is created
using the value from the defaults with key

key

. The value
identifies the sound resource to load when

actionPerformed

is invoked on the

Action

. The
sound resource is loaded into a

byte[]

by way of

getClass().getResourceAsStream()

.

**Parameters:**
- key

- the key identifying the audio action

**Returns:**
- an

Action

used to play the source, or

null

if

key

is

null

**See Also:**
- playSound(Action)

**Since:**
- 1.4

---

#### protected void playSound​(
Action
audioAction)

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.
The

actionPerformed

method is invoked if the value of
the

"AuditoryCues.playList"

default is a

non-null

Object[]

containing a

String

entry
equal to the name of the

audioAction

.

**Parameters:**
- audioAction

- an Action that knows how to render the audio
associated with the system or user activity
that is occurring; a value of

null

, is
ignored

**Throws:**
- ClassCastException

- if

audioAction

is

non-null

and the value of the default

"AuditoryCues.playList"

is not an

Object[]

**Since:**
- 1.4

---

### Additional Sections

#### Class BasicLookAndFeel

java.lang.Object

- javax.swing.LookAndFeel
- - javax.swing.plaf.basic.BasicLookAndFeel

javax.swing.LookAndFeel

- javax.swing.plaf.basic.BasicLookAndFeel

javax.swing.plaf.basic.BasicLookAndFeel

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** MetalLookAndFeel

,

SynthLookAndFeel

```java
public abstract class
BasicLookAndFeel

extends
LookAndFeel

implements
Serializable
```

A base class to use in creating a look and feel for Swing.

Each of the

ComponentUI

s provided by

BasicLookAndFeel

derives its behavior from the defaults
table. Unless otherwise noted each of the

ComponentUI

implementations in this package document the set of defaults they
use. Unless otherwise noted the defaults are installed at the time

installUI

is invoked, and follow the recommendations
outlined in

LookAndFeel

for installing defaults.

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

**See Also:** Serialized Form

public abstract class

BasicLookAndFeel

extends

LookAndFeel

implements

Serializable

A base class to use in creating a look and feel for Swing.

Each of the

ComponentUI

s provided by

BasicLookAndFeel

derives its behavior from the defaults
table. Unless otherwise noted each of the

ComponentUI

implementations in this package document the set of defaults they
use. Unless otherwise noted the defaults are installed at the time

installUI

is invoked, and follow the recommendations
outlined in

LookAndFeel

for installing defaults.

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

Each of the

ComponentUI

s provided by

BasicLookAndFeel

derives its behavior from the defaults
table. Unless otherwise noted each of the

ComponentUI

implementations in this package document the set of defaults they
use. Unless otherwise noted the defaults are installed at the time

installUI

is invoked, and follow the recommendations
outlined in

LookAndFeel

for installing defaults.

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

BasicLookAndFeel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Action

createAudioAction

​(

Object

key)

Creates and returns an

Action

used to play a sound.

protected

ActionMap

getAudioActionMap

()

Returns an

ActionMap

containing the audio actions
for this look and feel.

UIDefaults

getDefaults

()

Returns the look and feel defaults.

protected void

initClassDefaults

​(

UIDefaults

table)

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class.

protected void

initComponentDefaults

​(

UIDefaults

table)

Populates

table

with the defaults for the basic look and
feel.

protected void

initSystemColorDefaults

​(

UIDefaults

table)

Populates

table

with system colors.

protected void

loadSystemColors

​(

UIDefaults

table,

String

[] systemColors,
boolean useNative)

Populates

table

with the

name-color

pairs in

systemColors

.

protected void

playSound

​(

Action

audioAction)

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.

- Methods declared in class javax.swing.

LookAndFeel

getDescription

,

getDesktopPropertyValue

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getID

,

getLayoutStyle

,

getName

,

getSupportsWindowDecorations

,

initialize

,

installBorder

,

installColors

,

installColorsAndFont

,

installProperty

,

isNativeLookAndFeel

,

isSupportedLookAndFeel

,

loadKeyBindings

,

makeComponentInputMap

,

makeIcon

,

makeInputMap

,

makeKeyBindings

,

provideErrorFeedback

,

toString

,

uninitialize

,

uninstallBorder

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

BasicLookAndFeel

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Action

createAudioAction

​(

Object

key)

Creates and returns an

Action

used to play a sound.

protected

ActionMap

getAudioActionMap

()

Returns an

ActionMap

containing the audio actions
for this look and feel.

UIDefaults

getDefaults

()

Returns the look and feel defaults.

protected void

initClassDefaults

​(

UIDefaults

table)

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class.

protected void

initComponentDefaults

​(

UIDefaults

table)

Populates

table

with the defaults for the basic look and
feel.

protected void

initSystemColorDefaults

​(

UIDefaults

table)

Populates

table

with system colors.

protected void

loadSystemColors

​(

UIDefaults

table,

String

[] systemColors,
boolean useNative)

Populates

table

with the

name-color

pairs in

systemColors

.

protected void

playSound

​(

Action

audioAction)

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.

- Methods declared in class javax.swing.

LookAndFeel

getDescription

,

getDesktopPropertyValue

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getID

,

getLayoutStyle

,

getName

,

getSupportsWindowDecorations

,

initialize

,

installBorder

,

installColors

,

installColorsAndFont

,

installProperty

,

isNativeLookAndFeel

,

isSupportedLookAndFeel

,

loadKeyBindings

,

makeComponentInputMap

,

makeIcon

,

makeInputMap

,

makeKeyBindings

,

provideErrorFeedback

,

toString

,

uninitialize

,

uninstallBorder

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

Creates and returns an

Action

used to play a sound.

Returns an

ActionMap

containing the audio actions
for this look and feel.

Returns the look and feel defaults.

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class.

Populates

table

with the defaults for the basic look and
feel.

Populates

table

with system colors.

Populates

table

with the

name-color

pairs in

systemColors

.

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.

Methods declared in class javax.swing.

LookAndFeel

getDescription

,

getDesktopPropertyValue

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getID

,

getLayoutStyle

,

getName

,

getSupportsWindowDecorations

,

initialize

,

installBorder

,

installColors

,

installColorsAndFont

,

installProperty

,

isNativeLookAndFeel

,

isSupportedLookAndFeel

,

loadKeyBindings

,

makeComponentInputMap

,

makeIcon

,

makeInputMap

,

makeKeyBindings

,

provideErrorFeedback

,

toString

,

uninitialize

,

uninstallBorder

---

#### Methods declared in class javax.swing. LookAndFeel

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

- BasicLookAndFeel

```java
public BasicLookAndFeel()
```

============ METHOD DETAIL ==========

- Method Detail

- getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the look and feel defaults. The returned

UIDefaults

is populated by invoking, in order,

initClassDefaults

,

initSystemColorDefaults

and

initComponentDefaults

.

While this method is public, it should only be invoked by the

UIManager

when the look and feel is set as the current
look and feel and after

initialize

has been invoked.

**Overrides:** getDefaults

in class

LookAndFeel
**Returns:** the look and feel defaults
**See Also:** initClassDefaults(javax.swing.UIDefaults)

,

initSystemColorDefaults(javax.swing.UIDefaults)

,

initComponentDefaults(javax.swing.UIDefaults)

- initClassDefaults

```java
protected void initClassDefaults​(
UIDefaults
table)
```

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class. The value for a
particular

uiClassID

is

"javax.swing.plaf.basic.Basic + uiClassID"

. For example, the
value for the

uiClassID

TreeUI

is

"javax.swing.plaf.basic.BasicTreeUI"

.

**Parameters:** table

- the

UIDefaults

instance the entries are
added to
**Throws:** NullPointerException

- if

table

is

null
**See Also:** LookAndFeel

,

getDefaults()

- initSystemColorDefaults

```java
protected void initSystemColorDefaults​(
UIDefaults
table)
```

Populates

table

with system colors. This creates an
array of

name-color

pairs and invokes

loadSystemColors

.

The name is a

String

that corresponds to the name of
one of the static

SystemColor

fields in the

SystemColor

class. A name-color pair is created for every
such

SystemColor

field.

The

color

corresponds to a hex

String

as
understood by

Color.decode

. For example, one of the

name-color

pairs is

"desktop"-"#005C5C"

. This corresponds to the

SystemColor

field

desktop

, with a color value of

new Color(0x005C5C)

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

**Parameters:** table

- the

UIDefaults

object the values are added to
**Throws:** NullPointerException

- if

table

is

null
**See Also:** SystemColor

,

getDefaults()

,

loadSystemColors(javax.swing.UIDefaults, java.lang.String[], boolean)

- loadSystemColors

```java
protected void loadSystemColors​(
UIDefaults
table,

String
[] systemColors,
boolean useNative)
```

Populates

table

with the

name-color

pairs in

systemColors

. Refer to

initSystemColorDefaults(UIDefaults)

for details on
the format of

systemColors

.

An entry is added to

table

for each of the

name-color

pairs in

systemColors

. The entry key is
the

name

of the

name-color

pair.

The value of the entry corresponds to the

color

of the

name-color

pair. The value of the entry is calculated
in one of two ways. With either approach the value is always a

ColorUIResource

.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

**Parameters:** table

- the

UIDefaults

object the values are added to
**Parameters:** systemColors

- array of

name-color

pairs as described
in

initSystemColorDefaults(UIDefaults)
**Parameters:** useNative

- whether the color is obtained from

SystemColor

or

Color.decode
**Throws:** NullPointerException

- if

systemColors

is

null

; or

systemColors

is not empty, and

table

is

null

; or one of the
names of the

name-color

pairs is

null

; or

useNative

is

false

and one of the

colors

of the

name-color

pairs is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

useNative

is

false

and

systemColors.length

is odd
**See Also:** initSystemColorDefaults(javax.swing.UIDefaults)

,

SystemColor

,

Color.decode(String)

- initComponentDefaults

```java
protected void initComponentDefaults​(
UIDefaults
table)
```

Populates

table

with the defaults for the basic look and
feel.

**Parameters:** table

- the

UIDefaults

to add the values to
**Throws:** NullPointerException

- if

table

is

null

- getAudioActionMap

```java
protected
ActionMap
getAudioActionMap()
```

Returns an

ActionMap

containing the audio actions
for this look and feel.

The returned

ActionMap

contains

Actions

that
embody the ability to render an auditory cue. These auditory
cues map onto user and system activities that may be useful
for an end user to know about (such as a dialog box appearing).

At the appropriate time,
the

ComponentUI

is responsible for obtaining an

Action

out of the

ActionMap

and passing
it to

playSound

.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

**Returns:** an ActionMap containing

Actions

responsible for playing auditory cues
**Throws:** ClassCastException

- if the value of the
default

"AuditoryCues.actionMap"

is not an

ActionMap

, or the value of the default

"AuditoryCues.cueList"

is not an

Object[]
**Since:** 1.4
**See Also:** createAudioAction(java.lang.Object)

,

playSound(Action)

- createAudioAction

```java
protected
Action
createAudioAction​(
Object
key)
```

Creates and returns an

Action

used to play a sound.

If

key

is

non-null

, an

Action

is created
using the value from the defaults with key

key

. The value
identifies the sound resource to load when

actionPerformed

is invoked on the

Action

. The
sound resource is loaded into a

byte[]

by way of

getClass().getResourceAsStream()

.

**Parameters:** key

- the key identifying the audio action
**Returns:** an

Action

used to play the source, or

null

if

key

is

null
**Since:** 1.4
**See Also:** playSound(Action)

- playSound

```java
protected void playSound​(
Action
audioAction)
```

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.
The

actionPerformed

method is invoked if the value of
the

"AuditoryCues.playList"

default is a

non-null

Object[]

containing a

String

entry
equal to the name of the

audioAction

.

**Parameters:** audioAction

- an Action that knows how to render the audio
associated with the system or user activity
that is occurring; a value of

null

, is
ignored
**Throws:** ClassCastException

- if

audioAction

is

non-null

and the value of the default

"AuditoryCues.playList"

is not an

Object[]
**Since:** 1.4

Constructor Detail

- BasicLookAndFeel

```java
public BasicLookAndFeel()
```

---

#### Constructor Detail

BasicLookAndFeel

```java
public BasicLookAndFeel()
```

---

#### BasicLookAndFeel

public BasicLookAndFeel()

Method Detail

- getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the look and feel defaults. The returned

UIDefaults

is populated by invoking, in order,

initClassDefaults

,

initSystemColorDefaults

and

initComponentDefaults

.

While this method is public, it should only be invoked by the

UIManager

when the look and feel is set as the current
look and feel and after

initialize

has been invoked.

**Overrides:** getDefaults

in class

LookAndFeel
**Returns:** the look and feel defaults
**See Also:** initClassDefaults(javax.swing.UIDefaults)

,

initSystemColorDefaults(javax.swing.UIDefaults)

,

initComponentDefaults(javax.swing.UIDefaults)

- initClassDefaults

```java
protected void initClassDefaults​(
UIDefaults
table)
```

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class. The value for a
particular

uiClassID

is

"javax.swing.plaf.basic.Basic + uiClassID"

. For example, the
value for the

uiClassID

TreeUI

is

"javax.swing.plaf.basic.BasicTreeUI"

.

**Parameters:** table

- the

UIDefaults

instance the entries are
added to
**Throws:** NullPointerException

- if

table

is

null
**See Also:** LookAndFeel

,

getDefaults()

- initSystemColorDefaults

```java
protected void initSystemColorDefaults​(
UIDefaults
table)
```

Populates

table

with system colors. This creates an
array of

name-color

pairs and invokes

loadSystemColors

.

The name is a

String

that corresponds to the name of
one of the static

SystemColor

fields in the

SystemColor

class. A name-color pair is created for every
such

SystemColor

field.

The

color

corresponds to a hex

String

as
understood by

Color.decode

. For example, one of the

name-color

pairs is

"desktop"-"#005C5C"

. This corresponds to the

SystemColor

field

desktop

, with a color value of

new Color(0x005C5C)

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

**Parameters:** table

- the

UIDefaults

object the values are added to
**Throws:** NullPointerException

- if

table

is

null
**See Also:** SystemColor

,

getDefaults()

,

loadSystemColors(javax.swing.UIDefaults, java.lang.String[], boolean)

- loadSystemColors

```java
protected void loadSystemColors​(
UIDefaults
table,

String
[] systemColors,
boolean useNative)
```

Populates

table

with the

name-color

pairs in

systemColors

. Refer to

initSystemColorDefaults(UIDefaults)

for details on
the format of

systemColors

.

An entry is added to

table

for each of the

name-color

pairs in

systemColors

. The entry key is
the

name

of the

name-color

pair.

The value of the entry corresponds to the

color

of the

name-color

pair. The value of the entry is calculated
in one of two ways. With either approach the value is always a

ColorUIResource

.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

**Parameters:** table

- the

UIDefaults

object the values are added to
**Parameters:** systemColors

- array of

name-color

pairs as described
in

initSystemColorDefaults(UIDefaults)
**Parameters:** useNative

- whether the color is obtained from

SystemColor

or

Color.decode
**Throws:** NullPointerException

- if

systemColors

is

null

; or

systemColors

is not empty, and

table

is

null

; or one of the
names of the

name-color

pairs is

null

; or

useNative

is

false

and one of the

colors

of the

name-color

pairs is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

useNative

is

false

and

systemColors.length

is odd
**See Also:** initSystemColorDefaults(javax.swing.UIDefaults)

,

SystemColor

,

Color.decode(String)

- initComponentDefaults

```java
protected void initComponentDefaults​(
UIDefaults
table)
```

Populates

table

with the defaults for the basic look and
feel.

**Parameters:** table

- the

UIDefaults

to add the values to
**Throws:** NullPointerException

- if

table

is

null

- getAudioActionMap

```java
protected
ActionMap
getAudioActionMap()
```

Returns an

ActionMap

containing the audio actions
for this look and feel.

The returned

ActionMap

contains

Actions

that
embody the ability to render an auditory cue. These auditory
cues map onto user and system activities that may be useful
for an end user to know about (such as a dialog box appearing).

At the appropriate time,
the

ComponentUI

is responsible for obtaining an

Action

out of the

ActionMap

and passing
it to

playSound

.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

**Returns:** an ActionMap containing

Actions

responsible for playing auditory cues
**Throws:** ClassCastException

- if the value of the
default

"AuditoryCues.actionMap"

is not an

ActionMap

, or the value of the default

"AuditoryCues.cueList"

is not an

Object[]
**Since:** 1.4
**See Also:** createAudioAction(java.lang.Object)

,

playSound(Action)

- createAudioAction

```java
protected
Action
createAudioAction​(
Object
key)
```

Creates and returns an

Action

used to play a sound.

If

key

is

non-null

, an

Action

is created
using the value from the defaults with key

key

. The value
identifies the sound resource to load when

actionPerformed

is invoked on the

Action

. The
sound resource is loaded into a

byte[]

by way of

getClass().getResourceAsStream()

.

**Parameters:** key

- the key identifying the audio action
**Returns:** an

Action

used to play the source, or

null

if

key

is

null
**Since:** 1.4
**See Also:** playSound(Action)

- playSound

```java
protected void playSound​(
Action
audioAction)
```

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.
The

actionPerformed

method is invoked if the value of
the

"AuditoryCues.playList"

default is a

non-null

Object[]

containing a

String

entry
equal to the name of the

audioAction

.

**Parameters:** audioAction

- an Action that knows how to render the audio
associated with the system or user activity
that is occurring; a value of

null

, is
ignored
**Throws:** ClassCastException

- if

audioAction

is

non-null

and the value of the default

"AuditoryCues.playList"

is not an

Object[]
**Since:** 1.4

---

#### Method Detail

getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the look and feel defaults. The returned

UIDefaults

is populated by invoking, in order,

initClassDefaults

,

initSystemColorDefaults

and

initComponentDefaults

.

While this method is public, it should only be invoked by the

UIManager

when the look and feel is set as the current
look and feel and after

initialize

has been invoked.

**Overrides:** getDefaults

in class

LookAndFeel
**Returns:** the look and feel defaults
**See Also:** initClassDefaults(javax.swing.UIDefaults)

,

initSystemColorDefaults(javax.swing.UIDefaults)

,

initComponentDefaults(javax.swing.UIDefaults)

---

#### getDefaults

public

UIDefaults

getDefaults()

Returns the look and feel defaults. The returned

UIDefaults

is populated by invoking, in order,

initClassDefaults

,

initSystemColorDefaults

and

initComponentDefaults

.

While this method is public, it should only be invoked by the

UIManager

when the look and feel is set as the current
look and feel and after

initialize

has been invoked.

While this method is public, it should only be invoked by the

UIManager

when the look and feel is set as the current
look and feel and after

initialize

has been invoked.

initClassDefaults

```java
protected void initClassDefaults​(
UIDefaults
table)
```

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class. The value for a
particular

uiClassID

is

"javax.swing.plaf.basic.Basic + uiClassID"

. For example, the
value for the

uiClassID

TreeUI

is

"javax.swing.plaf.basic.BasicTreeUI"

.

**Parameters:** table

- the

UIDefaults

instance the entries are
added to
**Throws:** NullPointerException

- if

table

is

null
**See Also:** LookAndFeel

,

getDefaults()

---

#### initClassDefaults

protected void initClassDefaults​(

UIDefaults

table)

Populates

table

with mappings from

uiClassID

to the
fully qualified name of the ui class. The value for a
particular

uiClassID

is

"javax.swing.plaf.basic.Basic + uiClassID"

. For example, the
value for the

uiClassID

TreeUI

is

"javax.swing.plaf.basic.BasicTreeUI"

.

initSystemColorDefaults

```java
protected void initSystemColorDefaults​(
UIDefaults
table)
```

Populates

table

with system colors. This creates an
array of

name-color

pairs and invokes

loadSystemColors

.

The name is a

String

that corresponds to the name of
one of the static

SystemColor

fields in the

SystemColor

class. A name-color pair is created for every
such

SystemColor

field.

The

color

corresponds to a hex

String

as
understood by

Color.decode

. For example, one of the

name-color

pairs is

"desktop"-"#005C5C"

. This corresponds to the

SystemColor

field

desktop

, with a color value of

new Color(0x005C5C)

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

**Parameters:** table

- the

UIDefaults

object the values are added to
**Throws:** NullPointerException

- if

table

is

null
**See Also:** SystemColor

,

getDefaults()

,

loadSystemColors(javax.swing.UIDefaults, java.lang.String[], boolean)

---

#### initSystemColorDefaults

protected void initSystemColorDefaults​(

UIDefaults

table)

Populates

table

with system colors. This creates an
array of

name-color

pairs and invokes

loadSystemColors

.

The name is a

String

that corresponds to the name of
one of the static

SystemColor

fields in the

SystemColor

class. A name-color pair is created for every
such

SystemColor

field.

The

color

corresponds to a hex

String

as
understood by

Color.decode

. For example, one of the

name-color

pairs is

"desktop"-"#005C5C"

. This corresponds to the

SystemColor

field

desktop

, with a color value of

new Color(0x005C5C)

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

The name is a

String

that corresponds to the name of
one of the static

SystemColor

fields in the

SystemColor

class. A name-color pair is created for every
such

SystemColor

field.

The

color

corresponds to a hex

String

as
understood by

Color.decode

. For example, one of the

name-color

pairs is

"desktop"-"#005C5C"

. This corresponds to the

SystemColor

field

desktop

, with a color value of

new Color(0x005C5C)

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

The

color

corresponds to a hex

String

as
understood by

Color.decode

. For example, one of the

name-color

pairs is

"desktop"-"#005C5C"

. This corresponds to the

SystemColor

field

desktop

, with a color value of

new Color(0x005C5C)

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

The following shows two of the

name-color

pairs:

```java
String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());
```

As previously stated, this invokes

loadSystemColors

with the supplied

table

and

name-color

pair
array. The last argument to

loadSystemColors

indicates
whether the value of the field in

SystemColor

should be
used. This method passes the value of

isNativeLookAndFeel()

as the last argument to

loadSystemColors

.

String[] nameColorPairs = new String[] {
"desktop", "#005C5C",
"activeCaption", "#000080" };
loadSystemColors(table, nameColorPairs, isNativeLookAndFeel());

loadSystemColors

```java
protected void loadSystemColors​(
UIDefaults
table,

String
[] systemColors,
boolean useNative)
```

Populates

table

with the

name-color

pairs in

systemColors

. Refer to

initSystemColorDefaults(UIDefaults)

for details on
the format of

systemColors

.

An entry is added to

table

for each of the

name-color

pairs in

systemColors

. The entry key is
the

name

of the

name-color

pair.

The value of the entry corresponds to the

color

of the

name-color

pair. The value of the entry is calculated
in one of two ways. With either approach the value is always a

ColorUIResource

.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

**Parameters:** table

- the

UIDefaults

object the values are added to
**Parameters:** systemColors

- array of

name-color

pairs as described
in

initSystemColorDefaults(UIDefaults)
**Parameters:** useNative

- whether the color is obtained from

SystemColor

or

Color.decode
**Throws:** NullPointerException

- if

systemColors

is

null

; or

systemColors

is not empty, and

table

is

null

; or one of the
names of the

name-color

pairs is

null

; or

useNative

is

false

and one of the

colors

of the

name-color

pairs is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

useNative

is

false

and

systemColors.length

is odd
**See Also:** initSystemColorDefaults(javax.swing.UIDefaults)

,

SystemColor

,

Color.decode(String)

---

#### loadSystemColors

protected void loadSystemColors​(

UIDefaults

table,

String

[] systemColors,
boolean useNative)

Populates

table

with the

name-color

pairs in

systemColors

. Refer to

initSystemColorDefaults(UIDefaults)

for details on
the format of

systemColors

.

An entry is added to

table

for each of the

name-color

pairs in

systemColors

. The entry key is
the

name

of the

name-color

pair.

The value of the entry corresponds to the

color

of the

name-color

pair. The value of the entry is calculated
in one of two ways. With either approach the value is always a

ColorUIResource

.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

An entry is added to

table

for each of the

name-color

pairs in

systemColors

. The entry key is
the

name

of the

name-color

pair.

The value of the entry corresponds to the

color

of the

name-color

pair. The value of the entry is calculated
in one of two ways. With either approach the value is always a

ColorUIResource

.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

The value of the entry corresponds to the

color

of the

name-color

pair. The value of the entry is calculated
in one of two ways. With either approach the value is always a

ColorUIResource

.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

If

useNative

is

false

, the

color

is
created by using

Color.decode

to convert the

String

into a

Color

. If

decode

can not convert
the

String

into a

Color

(

NumberFormatException

is thrown) then a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

If

useNative

is

true

, the

color

is the
value of the field in

SystemColor

with the same name as
the

name

of the

name-color

pair. If the field
is not valid, a

ColorUIResource

of black is used.

initComponentDefaults

```java
protected void initComponentDefaults​(
UIDefaults
table)
```

Populates

table

with the defaults for the basic look and
feel.

**Parameters:** table

- the

UIDefaults

to add the values to
**Throws:** NullPointerException

- if

table

is

null

---

#### initComponentDefaults

protected void initComponentDefaults​(

UIDefaults

table)

Populates

table

with the defaults for the basic look and
feel.

getAudioActionMap

```java
protected
ActionMap
getAudioActionMap()
```

Returns an

ActionMap

containing the audio actions
for this look and feel.

The returned

ActionMap

contains

Actions

that
embody the ability to render an auditory cue. These auditory
cues map onto user and system activities that may be useful
for an end user to know about (such as a dialog box appearing).

At the appropriate time,
the

ComponentUI

is responsible for obtaining an

Action

out of the

ActionMap

and passing
it to

playSound

.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

**Returns:** an ActionMap containing

Actions

responsible for playing auditory cues
**Throws:** ClassCastException

- if the value of the
default

"AuditoryCues.actionMap"

is not an

ActionMap

, or the value of the default

"AuditoryCues.cueList"

is not an

Object[]
**Since:** 1.4
**See Also:** createAudioAction(java.lang.Object)

,

playSound(Action)

---

#### getAudioActionMap

protected

ActionMap

getAudioActionMap()

Returns an

ActionMap

containing the audio actions
for this look and feel.

The returned

ActionMap

contains

Actions

that
embody the ability to render an auditory cue. These auditory
cues map onto user and system activities that may be useful
for an end user to know about (such as a dialog box appearing).

At the appropriate time,
the

ComponentUI

is responsible for obtaining an

Action

out of the

ActionMap

and passing
it to

playSound

.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

The returned

ActionMap

contains

Actions

that
embody the ability to render an auditory cue. These auditory
cues map onto user and system activities that may be useful
for an end user to know about (such as a dialog box appearing).

At the appropriate time,
the

ComponentUI

is responsible for obtaining an

Action

out of the

ActionMap

and passing
it to

playSound

.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

At the appropriate time,
the

ComponentUI

is responsible for obtaining an

Action

out of the

ActionMap

and passing
it to

playSound

.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

This method first looks up the

ActionMap

from the
defaults using the key

"AuditoryCues.actionMap"

.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

If the value is

non-null

, it is returned. If the value
of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

non-null

, an

ActionMapUIResource

is created and
populated. Population is done by iterating over each of the
elements of the

"AuditoryCues.cueList"

array, and
invoking

createAudioAction()

to create an

Action

for each element. The resulting

Action

is
placed in the

ActionMapUIResource

, using the array
element as the key. For example, if the

"AuditoryCues.cueList"

array contains a single-element,

"audioKey"

, the

ActionMapUIResource

is created, then
populated by way of

actionMap.put(cueList[0],
createAudioAction(cueList[0]))

.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

If the value of the default

"AuditoryCues.actionMap"

is

null

and the value of the default

"AuditoryCues.cueList"

is

null

, an empty

ActionMapUIResource

is created.

createAudioAction

```java
protected
Action
createAudioAction​(
Object
key)
```

Creates and returns an

Action

used to play a sound.

If

key

is

non-null

, an

Action

is created
using the value from the defaults with key

key

. The value
identifies the sound resource to load when

actionPerformed

is invoked on the

Action

. The
sound resource is loaded into a

byte[]

by way of

getClass().getResourceAsStream()

.

**Parameters:** key

- the key identifying the audio action
**Returns:** an

Action

used to play the source, or

null

if

key

is

null
**Since:** 1.4
**See Also:** playSound(Action)

---

#### createAudioAction

protected

Action

createAudioAction​(

Object

key)

Creates and returns an

Action

used to play a sound.

If

key

is

non-null

, an

Action

is created
using the value from the defaults with key

key

. The value
identifies the sound resource to load when

actionPerformed

is invoked on the

Action

. The
sound resource is loaded into a

byte[]

by way of

getClass().getResourceAsStream()

.

If

key

is

non-null

, an

Action

is created
using the value from the defaults with key

key

. The value
identifies the sound resource to load when

actionPerformed

is invoked on the

Action

. The
sound resource is loaded into a

byte[]

by way of

getClass().getResourceAsStream()

.

playSound

```java
protected void playSound​(
Action
audioAction)
```

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.
The

actionPerformed

method is invoked if the value of
the

"AuditoryCues.playList"

default is a

non-null

Object[]

containing a

String

entry
equal to the name of the

audioAction

.

**Parameters:** audioAction

- an Action that knows how to render the audio
associated with the system or user activity
that is occurring; a value of

null

, is
ignored
**Throws:** ClassCastException

- if

audioAction

is

non-null

and the value of the default

"AuditoryCues.playList"

is not an

Object[]
**Since:** 1.4

---

#### playSound

protected void playSound​(

Action

audioAction)

If necessary, invokes

actionPerformed

on

audioAction

to play a sound.
The

actionPerformed

method is invoked if the value of
the

"AuditoryCues.playList"

default is a

non-null

Object[]

containing a

String

entry
equal to the name of the

audioAction

.

---

