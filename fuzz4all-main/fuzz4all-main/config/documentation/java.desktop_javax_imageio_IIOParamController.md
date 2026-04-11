# Interface IIOParamController

**Source:** `java.desktop\javax\imageio\IIOParamController.html`

### Class Description

```java
public interface
IIOParamController
```

An interface to be implemented by objects that can determine the
settings of an

IIOParam

object, either by putting up a
GUI to obtain values from a user, or by other means. This
interface merely specifies a generic

activate

method
that invokes the controller, without regard for how the controller
obtains values (

i.e.

, whether the controller puts up a GUI
or merely computes a set of values is irrelevant to this
interface).

Within the

activate

method, a controller obtains
initial values by querying the

IIOParam

object's

get

methods, modifies values by whatever means, then
invokes the

IIOParam

object's

set

methods
to modify the appropriate settings. Normally, these

set

methods will be invoked all at once at a final
commit in order that a cancel operation not disturb existing
values. In general, applications may expect that when the

activate

method returns

true

, the

IIOParam

object is ready for use in a read or write
operation.

Vendors may choose to provide GUIs for the

IIOParam

subclasses they define for a particular
plug-in. These can be set up as default controllers in the
corresponding

IIOParam

subclasses.

Applications may override any default GUIs and provide their
own controllers embedded in their own framework. All that is
required is that the

activate

method behave modally
(not returning until either cancelled or committed), though it need
not put up an explicitly modal dialog. Such a non-modal GUI
component would be coded roughly as follows:

```java
class MyGUI extends SomeComponent implements IIOParamController {

public MyGUI() {
// ...
setEnabled(false);
}

public boolean activate(IIOParam param) {
// disable other components if desired
setEnabled(true);
// go to sleep until either cancelled or committed
boolean ret = false;
if (!cancelled) {
// set values on param
ret = true;
}
setEnabled(false);
// enable any components disabled above
return ret;
}
```

Alternatively, an algorithmic process such as a database lookup
or the parsing of a command line could be used as a controller, in
which case the

activate

method would simply look up or
compute the settings, call the

IIOParam.setXXX

methods, and return

true

.

**See Also:** IIOParam.setController(javax.imageio.IIOParamController)

,

IIOParam.getController()

,

IIOParam.getDefaultController()

,

IIOParam.hasController()

,

IIOParam.activateController()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean activate​(
IIOParam
param)

Activates the controller. If

true

is returned,
all settings in the

IIOParam

object should be
ready for use in a read or write operation. If

false

is returned, no settings in the

IIOParam

object will be disturbed (

i.e.

,
the user canceled the operation).

**Parameters:**
- param

- the

IIOParam

object to be modified.

**Returns:**
- true

if the

IIOParam

has been
modified,

false

otherwise.

**Throws:**
- IllegalArgumentException

- if

param

is

null

or is not an instance of the correct class.

---

### Additional Sections

#### Interface IIOParamController

```java
public interface
IIOParamController
```

An interface to be implemented by objects that can determine the
settings of an

IIOParam

object, either by putting up a
GUI to obtain values from a user, or by other means. This
interface merely specifies a generic

activate

method
that invokes the controller, without regard for how the controller
obtains values (

i.e.

, whether the controller puts up a GUI
or merely computes a set of values is irrelevant to this
interface).

Within the

activate

method, a controller obtains
initial values by querying the

IIOParam

object's

get

methods, modifies values by whatever means, then
invokes the

IIOParam

object's

set

methods
to modify the appropriate settings. Normally, these

set

methods will be invoked all at once at a final
commit in order that a cancel operation not disturb existing
values. In general, applications may expect that when the

activate

method returns

true

, the

IIOParam

object is ready for use in a read or write
operation.

Vendors may choose to provide GUIs for the

IIOParam

subclasses they define for a particular
plug-in. These can be set up as default controllers in the
corresponding

IIOParam

subclasses.

Applications may override any default GUIs and provide their
own controllers embedded in their own framework. All that is
required is that the

activate

method behave modally
(not returning until either cancelled or committed), though it need
not put up an explicitly modal dialog. Such a non-modal GUI
component would be coded roughly as follows:

```java
class MyGUI extends SomeComponent implements IIOParamController {

public MyGUI() {
// ...
setEnabled(false);
}

public boolean activate(IIOParam param) {
// disable other components if desired
setEnabled(true);
// go to sleep until either cancelled or committed
boolean ret = false;
if (!cancelled) {
// set values on param
ret = true;
}
setEnabled(false);
// enable any components disabled above
return ret;
}
```

Alternatively, an algorithmic process such as a database lookup
or the parsing of a command line could be used as a controller, in
which case the

activate

method would simply look up or
compute the settings, call the

IIOParam.setXXX

methods, and return

true

.

**See Also:** IIOParam.setController(javax.imageio.IIOParamController)

,

IIOParam.getController()

,

IIOParam.getDefaultController()

,

IIOParam.hasController()

,

IIOParam.activateController()

public interface

IIOParamController

An interface to be implemented by objects that can determine the
settings of an

IIOParam

object, either by putting up a
GUI to obtain values from a user, or by other means. This
interface merely specifies a generic

activate

method
that invokes the controller, without regard for how the controller
obtains values (

i.e.

, whether the controller puts up a GUI
or merely computes a set of values is irrelevant to this
interface).

Within the

activate

method, a controller obtains
initial values by querying the

IIOParam

object's

get

methods, modifies values by whatever means, then
invokes the

IIOParam

object's

set

methods
to modify the appropriate settings. Normally, these

set

methods will be invoked all at once at a final
commit in order that a cancel operation not disturb existing
values. In general, applications may expect that when the

activate

method returns

true

, the

IIOParam

object is ready for use in a read or write
operation.

Vendors may choose to provide GUIs for the

IIOParam

subclasses they define for a particular
plug-in. These can be set up as default controllers in the
corresponding

IIOParam

subclasses.

Applications may override any default GUIs and provide their
own controllers embedded in their own framework. All that is
required is that the

activate

method behave modally
(not returning until either cancelled or committed), though it need
not put up an explicitly modal dialog. Such a non-modal GUI
component would be coded roughly as follows:

```java
class MyGUI extends SomeComponent implements IIOParamController {

public MyGUI() {
// ...
setEnabled(false);
}

public boolean activate(IIOParam param) {
// disable other components if desired
setEnabled(true);
// go to sleep until either cancelled or committed
boolean ret = false;
if (!cancelled) {
// set values on param
ret = true;
}
setEnabled(false);
// enable any components disabled above
return ret;
}
```

Alternatively, an algorithmic process such as a database lookup
or the parsing of a command line could be used as a controller, in
which case the

activate

method would simply look up or
compute the settings, call the

IIOParam.setXXX

methods, and return

true

.

Within the

activate

method, a controller obtains
initial values by querying the

IIOParam

object's

get

methods, modifies values by whatever means, then
invokes the

IIOParam

object's

set

methods
to modify the appropriate settings. Normally, these

set

methods will be invoked all at once at a final
commit in order that a cancel operation not disturb existing
values. In general, applications may expect that when the

activate

method returns

true

, the

IIOParam

object is ready for use in a read or write
operation.

Vendors may choose to provide GUIs for the

IIOParam

subclasses they define for a particular
plug-in. These can be set up as default controllers in the
corresponding

IIOParam

subclasses.

Applications may override any default GUIs and provide their
own controllers embedded in their own framework. All that is
required is that the

activate

method behave modally
(not returning until either cancelled or committed), though it need
not put up an explicitly modal dialog. Such a non-modal GUI
component would be coded roughly as follows:

```java
class MyGUI extends SomeComponent implements IIOParamController {

public MyGUI() {
// ...
setEnabled(false);
}

public boolean activate(IIOParam param) {
// disable other components if desired
setEnabled(true);
// go to sleep until either cancelled or committed
boolean ret = false;
if (!cancelled) {
// set values on param
ret = true;
}
setEnabled(false);
// enable any components disabled above
return ret;
}
```

Alternatively, an algorithmic process such as a database lookup
or the parsing of a command line could be used as a controller, in
which case the

activate

method would simply look up or
compute the settings, call the

IIOParam.setXXX

methods, and return

true

.

Vendors may choose to provide GUIs for the

IIOParam

subclasses they define for a particular
plug-in. These can be set up as default controllers in the
corresponding

IIOParam

subclasses.

Applications may override any default GUIs and provide their
own controllers embedded in their own framework. All that is
required is that the

activate

method behave modally
(not returning until either cancelled or committed), though it need
not put up an explicitly modal dialog. Such a non-modal GUI
component would be coded roughly as follows:

```java
class MyGUI extends SomeComponent implements IIOParamController {

public MyGUI() {
// ...
setEnabled(false);
}

public boolean activate(IIOParam param) {
// disable other components if desired
setEnabled(true);
// go to sleep until either cancelled or committed
boolean ret = false;
if (!cancelled) {
// set values on param
ret = true;
}
setEnabled(false);
// enable any components disabled above
return ret;
}
```

Alternatively, an algorithmic process such as a database lookup
or the parsing of a command line could be used as a controller, in
which case the

activate

method would simply look up or
compute the settings, call the

IIOParam.setXXX

methods, and return

true

.

Applications may override any default GUIs and provide their
own controllers embedded in their own framework. All that is
required is that the

activate

method behave modally
(not returning until either cancelled or committed), though it need
not put up an explicitly modal dialog. Such a non-modal GUI
component would be coded roughly as follows:

```java
class MyGUI extends SomeComponent implements IIOParamController {

public MyGUI() {
// ...
setEnabled(false);
}

public boolean activate(IIOParam param) {
// disable other components if desired
setEnabled(true);
// go to sleep until either cancelled or committed
boolean ret = false;
if (!cancelled) {
// set values on param
ret = true;
}
setEnabled(false);
// enable any components disabled above
return ret;
}
```

Alternatively, an algorithmic process such as a database lookup
or the parsing of a command line could be used as a controller, in
which case the

activate

method would simply look up or
compute the settings, call the

IIOParam.setXXX

methods, and return

true

.

class MyGUI extends SomeComponent implements IIOParamController {

public MyGUI() {
// ...
setEnabled(false);
}

public boolean activate(IIOParam param) {
// disable other components if desired
setEnabled(true);
// go to sleep until either cancelled or committed
boolean ret = false;
if (!cancelled) {
// set values on param
ret = true;
}
setEnabled(false);
// enable any components disabled above
return ret;
}

Alternatively, an algorithmic process such as a database lookup
or the parsing of a command line could be used as a controller, in
which case the

activate

method would simply look up or
compute the settings, call the

IIOParam.setXXX

methods, and return

true

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

activate

​(

IIOParam

param)

Activates the controller.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

activate

​(

IIOParam

param)

Activates the controller.

---

#### Method Summary

Activates the controller.

============ METHOD DETAIL ==========

- Method Detail

- activate

```java
boolean activate​(
IIOParam
param)
```

Activates the controller. If

true

is returned,
all settings in the

IIOParam

object should be
ready for use in a read or write operation. If

false

is returned, no settings in the

IIOParam

object will be disturbed (

i.e.

,
the user canceled the operation).

**Parameters:** param

- the

IIOParam

object to be modified.
**Returns:** true

if the

IIOParam

has been
modified,

false

otherwise.
**Throws:** IllegalArgumentException

- if

param

is

null

or is not an instance of the correct class.

Method Detail

- activate

```java
boolean activate​(
IIOParam
param)
```

Activates the controller. If

true

is returned,
all settings in the

IIOParam

object should be
ready for use in a read or write operation. If

false

is returned, no settings in the

IIOParam

object will be disturbed (

i.e.

,
the user canceled the operation).

**Parameters:** param

- the

IIOParam

object to be modified.
**Returns:** true

if the

IIOParam

has been
modified,

false

otherwise.
**Throws:** IllegalArgumentException

- if

param

is

null

or is not an instance of the correct class.

---

#### Method Detail

activate

```java
boolean activate​(
IIOParam
param)
```

Activates the controller. If

true

is returned,
all settings in the

IIOParam

object should be
ready for use in a read or write operation. If

false

is returned, no settings in the

IIOParam

object will be disturbed (

i.e.

,
the user canceled the operation).

**Parameters:** param

- the

IIOParam

object to be modified.
**Returns:** true

if the

IIOParam

has been
modified,

false

otherwise.
**Throws:** IllegalArgumentException

- if

param

is

null

or is not an instance of the correct class.

---

#### activate

boolean activate​(

IIOParam

param)

Activates the controller. If

true

is returned,
all settings in the

IIOParam

object should be
ready for use in a read or write operation. If

false

is returned, no settings in the

IIOParam

object will be disturbed (

i.e.

,
the user canceled the operation).

---

