# Class JConsolePlugin

**Source:** `jdk.jconsole\com\sun\tools\jconsole\JConsolePlugin.html`

### Class Description

```java
public abstract class
JConsolePlugin

extends
Object
```

A JConsole plugin class. JConsole uses the

service provider

mechanism to search the JConsole plugins.
Users can provide their JConsole plugins in a jar file
containing a file named

```java
META-INF/services/com.sun.tools.jconsole.JConsolePlugin
```

This file contains one line for each plugin, for example,

```java
com.sun.example.JTop
```

which is the fully qualified class name of the class implementing

JConsolePlugin

.

To load the JConsole plugins in JConsole, run:

```java
jconsole -pluginpath <plugin-path>
```

where

<plugin-path>

specifies the paths of JConsole
plugins to look up which can be a directory or a jar file. Multiple
paths are separated by the path separator character of the platform.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

**Since:** 1.6
**See Also:** ServiceLoader

---

### Field Details

*No entries found.*

### Constructor Details

#### protected JConsolePlugin()

Constructor.

---

### Method Details

#### public final void setContext​(
JConsoleContext
context)

Sets the

JConsoleContext

object representing
the connection to an application. This method will be called
only once after the plugin is created and before the

getTabs()

is called. The given

context

can be in any

connection state

when
this method is called.

**Parameters:**
- context

- a

JConsoleContext

object

---

#### public final
JConsoleContext
getContext()

Returns the

JConsoleContext

object representing
the connection to an application. This method may return

null

if it is called before the

context

is initialized.

**Returns:**
- the

JConsoleContext

object representing
the connection to an application.

---

#### public abstract
Map
<
String
,​
JPanel
> getTabs()

Returns the tabs to be added in JConsole window.

The returned map contains one entry for each tab
to be added in the tabbed pane in a JConsole window with
the tab name as the key
and the

JPanel

object as the value.
This method returns an empty map if no tab is added by this plugin.
This method will be called from the

Event Dispatch Thread

once at the new connection time.

**Returns:**
- a map of a tab name and a

JPanel

object
representing the tabs to be added in the JConsole window;
or an empty map.

---

#### public abstract
SwingWorker
<?,​?> newSwingWorker()

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

JConsole schedules the GUI update at an interval specified
for a connection. This method will be called at every
update to obtain a

SwingWorker

for each plugin.

JConsole will invoke the

execute()

method to schedule the returned

SwingWorker

for execution
if:

- the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and
- the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

Otherwise,

SwingWorker

object will not be scheduled to work.

A plugin can schedule its own GUI update and this method
will return

null

.

**Returns:**
- a

SwingWorker

to perform the GUI update; or

null

.

---

#### public void dispose()

Dispose this plugin. This method is called by JConsole to inform
that this plugin will be discarded and that it should free
any resources that it has allocated.
The

JConsoleContext

can be in any

connection state

when
this method is called.

---

#### public final void addContextPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.
This method is a convenient method for this plugin to register
a listener when the

JConsoleContext

object may or
may not be available.

For example, a plugin constructor can
call this method to register a listener to listen to the

connectionState

property changes and the listener will be added to the

JConsoleContext

object when it is available.

**Parameters:**
- listener

- The

PropertyChangeListener

to be added

**Throws:**
- NullPointerException

- if

listener

is

null

.

---

#### public final void removeContextPropertyChangeListener​(
PropertyChangeListener
listener)

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.
If

listener

was never added, no exception is
thrown and no action is taken.

**Parameters:**
- listener

- the

PropertyChangeListener

to be removed

**Throws:**
- NullPointerException

- if

listener

is

null

.

---

### Additional Sections

#### Class JConsolePlugin

java.lang.Object

- com.sun.tools.jconsole.JConsolePlugin

com.sun.tools.jconsole.JConsolePlugin

```java
public abstract class
JConsolePlugin

extends
Object
```

A JConsole plugin class. JConsole uses the

service provider

mechanism to search the JConsole plugins.
Users can provide their JConsole plugins in a jar file
containing a file named

```java
META-INF/services/com.sun.tools.jconsole.JConsolePlugin
```

This file contains one line for each plugin, for example,

```java
com.sun.example.JTop
```

which is the fully qualified class name of the class implementing

JConsolePlugin

.

To load the JConsole plugins in JConsole, run:

```java
jconsole -pluginpath <plugin-path>
```

where

<plugin-path>

specifies the paths of JConsole
plugins to look up which can be a directory or a jar file. Multiple
paths are separated by the path separator character of the platform.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

**Since:** 1.6
**See Also:** ServiceLoader

public abstract class

JConsolePlugin

extends

Object

A JConsole plugin class. JConsole uses the

service provider

mechanism to search the JConsole plugins.
Users can provide their JConsole plugins in a jar file
containing a file named

```java
META-INF/services/com.sun.tools.jconsole.JConsolePlugin
```

This file contains one line for each plugin, for example,

```java
com.sun.example.JTop
```

which is the fully qualified class name of the class implementing

JConsolePlugin

.

To load the JConsole plugins in JConsole, run:

```java
jconsole -pluginpath <plugin-path>
```

where

<plugin-path>

specifies the paths of JConsole
plugins to look up which can be a directory or a jar file. Multiple
paths are separated by the path separator character of the platform.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

META-INF/services/com.sun.tools.jconsole.JConsolePlugin

This file contains one line for each plugin, for example,

```java
com.sun.example.JTop
```

which is the fully qualified class name of the class implementing

JConsolePlugin

.

To load the JConsole plugins in JConsole, run:

```java
jconsole -pluginpath <plugin-path>
```

where

<plugin-path>

specifies the paths of JConsole
plugins to look up which can be a directory or a jar file. Multiple
paths are separated by the path separator character of the platform.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

com.sun.example.JTop

which is the fully qualified class name of the class implementing

JConsolePlugin

.

To load the JConsole plugins in JConsole, run:

```java
jconsole -pluginpath <plugin-path>
```

where

<plugin-path>

specifies the paths of JConsole
plugins to look up which can be a directory or a jar file. Multiple
paths are separated by the path separator character of the platform.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

To load the JConsole plugins in JConsole, run:

```java
jconsole -pluginpath <plugin-path>
```

where

<plugin-path>

specifies the paths of JConsole
plugins to look up which can be a directory or a jar file. Multiple
paths are separated by the path separator character of the platform.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

jconsole -pluginpath <plugin-path>

where

<plugin-path>

specifies the paths of JConsole
plugins to look up which can be a directory or a jar file. Multiple
paths are separated by the path separator character of the platform.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

When a new JConsole window is created for a connection,
an instance of each

JConsolePlugin

will be created.
The

JConsoleContext

object is not available at its
construction time.
JConsole will set the

JConsoleContext

object for
a plugin after the plugin object is created. It will then
call its

getTabs

method and add the returned
tabs to the JConsole window.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JConsolePlugin

()

Constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addContextPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.

void

dispose

()

Dispose this plugin.

JConsoleContext

getContext

()

Returns the

JConsoleContext

object representing
the connection to an application.

abstract

Map

<

String

,​

JPanel

>

getTabs

()

Returns the tabs to be added in JConsole window.

abstract

SwingWorker

<?,​?>

newSwingWorker

()

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

void

removeContextPropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.

void

setContext

​(

JConsoleContext

context)

Sets the

JConsoleContext

object representing
the connection to an application.

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

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JConsolePlugin

()

Constructor.

---

#### Constructor Summary

Constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addContextPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.

void

dispose

()

Dispose this plugin.

JConsoleContext

getContext

()

Returns the

JConsoleContext

object representing
the connection to an application.

abstract

Map

<

String

,​

JPanel

>

getTabs

()

Returns the tabs to be added in JConsole window.

abstract

SwingWorker

<?,​?>

newSwingWorker

()

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

void

removeContextPropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.

void

setContext

​(

JConsoleContext

context)

Sets the

JConsoleContext

object representing
the connection to an application.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.

Dispose this plugin.

Returns the

JConsoleContext

object representing
the connection to an application.

Returns the tabs to be added in JConsole window.

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.

Sets the

JConsoleContext

object representing
the connection to an application.

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

- JConsolePlugin

```java
protected JConsolePlugin()
```

Constructor.

============ METHOD DETAIL ==========

- Method Detail

- setContext

```java
public final void setContext​(
JConsoleContext
context)
```

Sets the

JConsoleContext

object representing
the connection to an application. This method will be called
only once after the plugin is created and before the

getTabs()

is called. The given

context

can be in any

connection state

when
this method is called.

**Parameters:** context

- a

JConsoleContext

object

- getContext

```java
public final
JConsoleContext
getContext()
```

Returns the

JConsoleContext

object representing
the connection to an application. This method may return

null

if it is called before the

context

is initialized.

**Returns:** the

JConsoleContext

object representing
the connection to an application.

- getTabs

```java
public abstract
Map
<
String
,​
JPanel
> getTabs()
```

Returns the tabs to be added in JConsole window.

The returned map contains one entry for each tab
to be added in the tabbed pane in a JConsole window with
the tab name as the key
and the

JPanel

object as the value.
This method returns an empty map if no tab is added by this plugin.
This method will be called from the

Event Dispatch Thread

once at the new connection time.

**Returns:** a map of a tab name and a

JPanel

object
representing the tabs to be added in the JConsole window;
or an empty map.

- newSwingWorker

```java
public abstract
SwingWorker
<?,​?> newSwingWorker()
```

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

JConsole schedules the GUI update at an interval specified
for a connection. This method will be called at every
update to obtain a

SwingWorker

for each plugin.

JConsole will invoke the

execute()

method to schedule the returned

SwingWorker

for execution
if:

- the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and
- the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

Otherwise,

SwingWorker

object will not be scheduled to work.

A plugin can schedule its own GUI update and this method
will return

null

.

**Returns:** a

SwingWorker

to perform the GUI update; or

null

.

- dispose

```java
public void dispose()
```

Dispose this plugin. This method is called by JConsole to inform
that this plugin will be discarded and that it should free
any resources that it has allocated.
The

JConsoleContext

can be in any

connection state

when
this method is called.

- addContextPropertyChangeListener

```java
public final void addContextPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.
This method is a convenient method for this plugin to register
a listener when the

JConsoleContext

object may or
may not be available.

For example, a plugin constructor can
call this method to register a listener to listen to the

connectionState

property changes and the listener will be added to the

JConsoleContext

object when it is available.

**Parameters:** listener

- The

PropertyChangeListener

to be added
**Throws:** NullPointerException

- if

listener

is

null

.

- removeContextPropertyChangeListener

```java
public final void removeContextPropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.
If

listener

was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- the

PropertyChangeListener

to be removed
**Throws:** NullPointerException

- if

listener

is

null

.

Constructor Detail

- JConsolePlugin

```java
protected JConsolePlugin()
```

Constructor.

---

#### Constructor Detail

JConsolePlugin

```java
protected JConsolePlugin()
```

Constructor.

---

#### JConsolePlugin

protected JConsolePlugin()

Constructor.

Method Detail

- setContext

```java
public final void setContext​(
JConsoleContext
context)
```

Sets the

JConsoleContext

object representing
the connection to an application. This method will be called
only once after the plugin is created and before the

getTabs()

is called. The given

context

can be in any

connection state

when
this method is called.

**Parameters:** context

- a

JConsoleContext

object

- getContext

```java
public final
JConsoleContext
getContext()
```

Returns the

JConsoleContext

object representing
the connection to an application. This method may return

null

if it is called before the

context

is initialized.

**Returns:** the

JConsoleContext

object representing
the connection to an application.

- getTabs

```java
public abstract
Map
<
String
,​
JPanel
> getTabs()
```

Returns the tabs to be added in JConsole window.

The returned map contains one entry for each tab
to be added in the tabbed pane in a JConsole window with
the tab name as the key
and the

JPanel

object as the value.
This method returns an empty map if no tab is added by this plugin.
This method will be called from the

Event Dispatch Thread

once at the new connection time.

**Returns:** a map of a tab name and a

JPanel

object
representing the tabs to be added in the JConsole window;
or an empty map.

- newSwingWorker

```java
public abstract
SwingWorker
<?,​?> newSwingWorker()
```

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

JConsole schedules the GUI update at an interval specified
for a connection. This method will be called at every
update to obtain a

SwingWorker

for each plugin.

JConsole will invoke the

execute()

method to schedule the returned

SwingWorker

for execution
if:

- the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and
- the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

Otherwise,

SwingWorker

object will not be scheduled to work.

A plugin can schedule its own GUI update and this method
will return

null

.

**Returns:** a

SwingWorker

to perform the GUI update; or

null

.

- dispose

```java
public void dispose()
```

Dispose this plugin. This method is called by JConsole to inform
that this plugin will be discarded and that it should free
any resources that it has allocated.
The

JConsoleContext

can be in any

connection state

when
this method is called.

- addContextPropertyChangeListener

```java
public final void addContextPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.
This method is a convenient method for this plugin to register
a listener when the

JConsoleContext

object may or
may not be available.

For example, a plugin constructor can
call this method to register a listener to listen to the

connectionState

property changes and the listener will be added to the

JConsoleContext

object when it is available.

**Parameters:** listener

- The

PropertyChangeListener

to be added
**Throws:** NullPointerException

- if

listener

is

null

.

- removeContextPropertyChangeListener

```java
public final void removeContextPropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.
If

listener

was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- the

PropertyChangeListener

to be removed
**Throws:** NullPointerException

- if

listener

is

null

.

---

#### Method Detail

setContext

```java
public final void setContext​(
JConsoleContext
context)
```

Sets the

JConsoleContext

object representing
the connection to an application. This method will be called
only once after the plugin is created and before the

getTabs()

is called. The given

context

can be in any

connection state

when
this method is called.

**Parameters:** context

- a

JConsoleContext

object

---

#### setContext

public final void setContext​(

JConsoleContext

context)

Sets the

JConsoleContext

object representing
the connection to an application. This method will be called
only once after the plugin is created and before the

getTabs()

is called. The given

context

can be in any

connection state

when
this method is called.

getContext

```java
public final
JConsoleContext
getContext()
```

Returns the

JConsoleContext

object representing
the connection to an application. This method may return

null

if it is called before the

context

is initialized.

**Returns:** the

JConsoleContext

object representing
the connection to an application.

---

#### getContext

public final

JConsoleContext

getContext()

Returns the

JConsoleContext

object representing
the connection to an application. This method may return

null

if it is called before the

context

is initialized.

getTabs

```java
public abstract
Map
<
String
,​
JPanel
> getTabs()
```

Returns the tabs to be added in JConsole window.

The returned map contains one entry for each tab
to be added in the tabbed pane in a JConsole window with
the tab name as the key
and the

JPanel

object as the value.
This method returns an empty map if no tab is added by this plugin.
This method will be called from the

Event Dispatch Thread

once at the new connection time.

**Returns:** a map of a tab name and a

JPanel

object
representing the tabs to be added in the JConsole window;
or an empty map.

---

#### getTabs

public abstract

Map

<

String

,​

JPanel

> getTabs()

Returns the tabs to be added in JConsole window.

The returned map contains one entry for each tab
to be added in the tabbed pane in a JConsole window with
the tab name as the key
and the

JPanel

object as the value.
This method returns an empty map if no tab is added by this plugin.
This method will be called from the

Event Dispatch Thread

once at the new connection time.

The returned map contains one entry for each tab
to be added in the tabbed pane in a JConsole window with
the tab name as the key
and the

JPanel

object as the value.
This method returns an empty map if no tab is added by this plugin.
This method will be called from the

Event Dispatch Thread

once at the new connection time.

newSwingWorker

```java
public abstract
SwingWorker
<?,​?> newSwingWorker()
```

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

JConsole schedules the GUI update at an interval specified
for a connection. This method will be called at every
update to obtain a

SwingWorker

for each plugin.

JConsole will invoke the

execute()

method to schedule the returned

SwingWorker

for execution
if:

- the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and
- the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

Otherwise,

SwingWorker

object will not be scheduled to work.

A plugin can schedule its own GUI update and this method
will return

null

.

**Returns:** a

SwingWorker

to perform the GUI update; or

null

.

---

#### newSwingWorker

public abstract

SwingWorker

<?,​?> newSwingWorker()

Returns a

SwingWorker

to perform
the GUI update for this plugin at the same interval
as JConsole updates the GUI.

JConsole schedules the GUI update at an interval specified
for a connection. This method will be called at every
update to obtain a

SwingWorker

for each plugin.

JConsole will invoke the

execute()

method to schedule the returned

SwingWorker

for execution
if:

- the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and
- the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

Otherwise,

SwingWorker

object will not be scheduled to work.

A plugin can schedule its own GUI update and this method
will return

null

.

JConsole schedules the GUI update at an interval specified
for a connection. This method will be called at every
update to obtain a

SwingWorker

for each plugin.

JConsole will invoke the

execute()

method to schedule the returned

SwingWorker

for execution
if:

- the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and
- the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

Otherwise,

SwingWorker

object will not be scheduled to work.

A plugin can schedule its own GUI update and this method
will return

null

.

JConsole will invoke the

execute()

method to schedule the returned

SwingWorker

for execution
if:

- the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and
- the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

Otherwise,

SwingWorker

object will not be scheduled to work.

A plugin can schedule its own GUI update and this method
will return

null

.

the

SwingWorker

object has not been executed
(i.e. the

SwingWorker.getState()

method
returns

PENDING

state); and

the

SwingWorker

object returned in the previous
update has completed the task if it was not

null

(i.e. the

SwingWorker.isDone

method
returns

true

).

A plugin can schedule its own GUI update and this method
will return

null

.

dispose

```java
public void dispose()
```

Dispose this plugin. This method is called by JConsole to inform
that this plugin will be discarded and that it should free
any resources that it has allocated.
The

JConsoleContext

can be in any

connection state

when
this method is called.

---

#### dispose

public void dispose()

Dispose this plugin. This method is called by JConsole to inform
that this plugin will be discarded and that it should free
any resources that it has allocated.
The

JConsoleContext

can be in any

connection state

when
this method is called.

addContextPropertyChangeListener

```java
public final void addContextPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.
This method is a convenient method for this plugin to register
a listener when the

JConsoleContext

object may or
may not be available.

For example, a plugin constructor can
call this method to register a listener to listen to the

connectionState

property changes and the listener will be added to the

JConsoleContext

object when it is available.

**Parameters:** listener

- The

PropertyChangeListener

to be added
**Throws:** NullPointerException

- if

listener

is

null

.

---

#### addContextPropertyChangeListener

public final void addContextPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the

JConsoleContext

object for this plugin.
This method is a convenient method for this plugin to register
a listener when the

JConsoleContext

object may or
may not be available.

For example, a plugin constructor can
call this method to register a listener to listen to the

connectionState

property changes and the listener will be added to the

JConsoleContext

object when it is available.

For example, a plugin constructor can
call this method to register a listener to listen to the

connectionState

property changes and the listener will be added to the

JConsoleContext

object when it is available.

removeContextPropertyChangeListener

```java
public final void removeContextPropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.
If

listener

was never added, no exception is
thrown and no action is taken.

**Parameters:** listener

- the

PropertyChangeListener

to be removed
**Throws:** NullPointerException

- if

listener

is

null

.

---

#### removeContextPropertyChangeListener

public final void removeContextPropertyChangeListener​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list of the

JConsoleContext

object for this plugin.
If

listener

was never added, no exception is
thrown and no action is taken.

---

