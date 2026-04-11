# Interface Keymap

**Source:** `java.desktop\javax\swing\text\Keymap.html`

### Class Description

```java
public interface
Keymap
```

A collection of bindings of KeyStrokes to actions. The
bindings are basically name-value pairs that potentially
resolve in a hierarchy.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Fetches the name of the set of key-bindings.

**Returns:**
- the name

---

#### Action
getDefaultAction()

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it. Typically this
would be some action that inserts text so that
the keymap doesn't require an action for each
possible key.

**Returns:**
- the default action

---

#### void setDefaultAction​(
Action
a)

Set the default action to fire if a key is typed.

**Parameters:**
- a

- the action

---

#### Action
getAction​(
KeyStroke
key)

Fetches the action appropriate for the given symbolic
event sequence. This is used by JTextController to
determine how to interpret key sequences. If the
binding is not resolved locally, an attempt is made
to resolve through the parent keymap, if one is set.

**Parameters:**
- key

- the key sequence

**Returns:**
- the action associated with the key
sequence if one is defined, otherwise

null

---

#### KeyStroke
[] getBoundKeyStrokes()

Fetches all of the keystrokes in this map that
are bound to some action.

**Returns:**
- the list of keystrokes

---

#### Action
[] getBoundActions()

Fetches all of the actions defined in this keymap.

**Returns:**
- the list of actions

---

#### KeyStroke
[] getKeyStrokesForAction​(
Action
a)

Fetches the keystrokes that will result in
the given action.

**Parameters:**
- a

- the action

**Returns:**
- the list of keystrokes

---

#### boolean isLocallyDefined​(
KeyStroke
key)

Determines if the given key sequence is locally defined.

**Parameters:**
- key

- the key sequence

**Returns:**
- true if the key sequence is locally defined else false

---

#### void addActionForKeyStroke​(
KeyStroke
key,

Action
a)

Adds a binding to the keymap.

**Parameters:**
- key

- the key sequence
- a

- the action

---

#### void removeKeyStrokeBinding​(
KeyStroke
keys)

Removes a binding from the keymap.

**Parameters:**
- keys

- the key sequence

---

#### void removeBindings()

Removes all bindings from the keymap.

---

#### Keymap
getResolveParent()

Fetches the parent keymap used to resolve key-bindings.

**Returns:**
- the keymap

---

#### void setResolveParent​(
Keymap
parent)

Sets the parent keymap, which will be used to
resolve key-bindings.
The behavior is unspecified if a

Keymap

has itself
as one of its resolve parents.

**Parameters:**
- parent

- the parent keymap

---

### Additional Sections

#### Interface Keymap

```java
public interface
Keymap
```

A collection of bindings of KeyStrokes to actions. The
bindings are basically name-value pairs that potentially
resolve in a hierarchy.

public interface

Keymap

A collection of bindings of KeyStrokes to actions. The
bindings are basically name-value pairs that potentially
resolve in a hierarchy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addActionForKeyStroke

​(

KeyStroke

key,

Action

a)

Adds a binding to the keymap.

Action

getAction

​(

KeyStroke

key)

Fetches the action appropriate for the given symbolic
event sequence.

Action

[]

getBoundActions

()

Fetches all of the actions defined in this keymap.

KeyStroke

[]

getBoundKeyStrokes

()

Fetches all of the keystrokes in this map that
are bound to some action.

Action

getDefaultAction

()

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it.

KeyStroke

[]

getKeyStrokesForAction

​(

Action

a)

Fetches the keystrokes that will result in
the given action.

String

getName

()

Fetches the name of the set of key-bindings.

Keymap

getResolveParent

()

Fetches the parent keymap used to resolve key-bindings.

boolean

isLocallyDefined

​(

KeyStroke

key)

Determines if the given key sequence is locally defined.

void

removeBindings

()

Removes all bindings from the keymap.

void

removeKeyStrokeBinding

​(

KeyStroke

keys)

Removes a binding from the keymap.

void

setDefaultAction

​(

Action

a)

Set the default action to fire if a key is typed.

void

setResolveParent

​(

Keymap

parent)

Sets the parent keymap, which will be used to
resolve key-bindings.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addActionForKeyStroke

​(

KeyStroke

key,

Action

a)

Adds a binding to the keymap.

Action

getAction

​(

KeyStroke

key)

Fetches the action appropriate for the given symbolic
event sequence.

Action

[]

getBoundActions

()

Fetches all of the actions defined in this keymap.

KeyStroke

[]

getBoundKeyStrokes

()

Fetches all of the keystrokes in this map that
are bound to some action.

Action

getDefaultAction

()

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it.

KeyStroke

[]

getKeyStrokesForAction

​(

Action

a)

Fetches the keystrokes that will result in
the given action.

String

getName

()

Fetches the name of the set of key-bindings.

Keymap

getResolveParent

()

Fetches the parent keymap used to resolve key-bindings.

boolean

isLocallyDefined

​(

KeyStroke

key)

Determines if the given key sequence is locally defined.

void

removeBindings

()

Removes all bindings from the keymap.

void

removeKeyStrokeBinding

​(

KeyStroke

keys)

Removes a binding from the keymap.

void

setDefaultAction

​(

Action

a)

Set the default action to fire if a key is typed.

void

setResolveParent

​(

Keymap

parent)

Sets the parent keymap, which will be used to
resolve key-bindings.

---

#### Method Summary

Adds a binding to the keymap.

Fetches the action appropriate for the given symbolic
event sequence.

Fetches all of the actions defined in this keymap.

Fetches all of the keystrokes in this map that
are bound to some action.

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it.

Fetches the keystrokes that will result in
the given action.

Fetches the name of the set of key-bindings.

Fetches the parent keymap used to resolve key-bindings.

Determines if the given key sequence is locally defined.

Removes all bindings from the keymap.

Removes a binding from the keymap.

Set the default action to fire if a key is typed.

Sets the parent keymap, which will be used to
resolve key-bindings.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Fetches the name of the set of key-bindings.

**Returns:** the name

- getDefaultAction

```java
Action
getDefaultAction()
```

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it. Typically this
would be some action that inserts text so that
the keymap doesn't require an action for each
possible key.

**Returns:** the default action

- setDefaultAction

```java
void setDefaultAction​(
Action
a)
```

Set the default action to fire if a key is typed.

**Parameters:** a

- the action

- getAction

```java
Action
getAction​(
KeyStroke
key)
```

Fetches the action appropriate for the given symbolic
event sequence. This is used by JTextController to
determine how to interpret key sequences. If the
binding is not resolved locally, an attempt is made
to resolve through the parent keymap, if one is set.

**Parameters:** key

- the key sequence
**Returns:** the action associated with the key
sequence if one is defined, otherwise

null

- getBoundKeyStrokes

```java
KeyStroke
[] getBoundKeyStrokes()
```

Fetches all of the keystrokes in this map that
are bound to some action.

**Returns:** the list of keystrokes

- getBoundActions

```java
Action
[] getBoundActions()
```

Fetches all of the actions defined in this keymap.

**Returns:** the list of actions

- getKeyStrokesForAction

```java
KeyStroke
[] getKeyStrokesForAction​(
Action
a)
```

Fetches the keystrokes that will result in
the given action.

**Parameters:** a

- the action
**Returns:** the list of keystrokes

- isLocallyDefined

```java
boolean isLocallyDefined​(
KeyStroke
key)
```

Determines if the given key sequence is locally defined.

**Parameters:** key

- the key sequence
**Returns:** true if the key sequence is locally defined else false

- addActionForKeyStroke

```java
void addActionForKeyStroke​(
KeyStroke
key,

Action
a)
```

Adds a binding to the keymap.

**Parameters:** key

- the key sequence
**Parameters:** a

- the action

- removeKeyStrokeBinding

```java
void removeKeyStrokeBinding​(
KeyStroke
keys)
```

Removes a binding from the keymap.

**Parameters:** keys

- the key sequence

- removeBindings

```java
void removeBindings()
```

Removes all bindings from the keymap.

- getResolveParent

```java
Keymap
getResolveParent()
```

Fetches the parent keymap used to resolve key-bindings.

**Returns:** the keymap

- setResolveParent

```java
void setResolveParent​(
Keymap
parent)
```

Sets the parent keymap, which will be used to
resolve key-bindings.
The behavior is unspecified if a

Keymap

has itself
as one of its resolve parents.

**Parameters:** parent

- the parent keymap

Method Detail

- getName

```java
String
getName()
```

Fetches the name of the set of key-bindings.

**Returns:** the name

- getDefaultAction

```java
Action
getDefaultAction()
```

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it. Typically this
would be some action that inserts text so that
the keymap doesn't require an action for each
possible key.

**Returns:** the default action

- setDefaultAction

```java
void setDefaultAction​(
Action
a)
```

Set the default action to fire if a key is typed.

**Parameters:** a

- the action

- getAction

```java
Action
getAction​(
KeyStroke
key)
```

Fetches the action appropriate for the given symbolic
event sequence. This is used by JTextController to
determine how to interpret key sequences. If the
binding is not resolved locally, an attempt is made
to resolve through the parent keymap, if one is set.

**Parameters:** key

- the key sequence
**Returns:** the action associated with the key
sequence if one is defined, otherwise

null

- getBoundKeyStrokes

```java
KeyStroke
[] getBoundKeyStrokes()
```

Fetches all of the keystrokes in this map that
are bound to some action.

**Returns:** the list of keystrokes

- getBoundActions

```java
Action
[] getBoundActions()
```

Fetches all of the actions defined in this keymap.

**Returns:** the list of actions

- getKeyStrokesForAction

```java
KeyStroke
[] getKeyStrokesForAction​(
Action
a)
```

Fetches the keystrokes that will result in
the given action.

**Parameters:** a

- the action
**Returns:** the list of keystrokes

- isLocallyDefined

```java
boolean isLocallyDefined​(
KeyStroke
key)
```

Determines if the given key sequence is locally defined.

**Parameters:** key

- the key sequence
**Returns:** true if the key sequence is locally defined else false

- addActionForKeyStroke

```java
void addActionForKeyStroke​(
KeyStroke
key,

Action
a)
```

Adds a binding to the keymap.

**Parameters:** key

- the key sequence
**Parameters:** a

- the action

- removeKeyStrokeBinding

```java
void removeKeyStrokeBinding​(
KeyStroke
keys)
```

Removes a binding from the keymap.

**Parameters:** keys

- the key sequence

- removeBindings

```java
void removeBindings()
```

Removes all bindings from the keymap.

- getResolveParent

```java
Keymap
getResolveParent()
```

Fetches the parent keymap used to resolve key-bindings.

**Returns:** the keymap

- setResolveParent

```java
void setResolveParent​(
Keymap
parent)
```

Sets the parent keymap, which will be used to
resolve key-bindings.
The behavior is unspecified if a

Keymap

has itself
as one of its resolve parents.

**Parameters:** parent

- the parent keymap

---

#### Method Detail

getName

```java
String
getName()
```

Fetches the name of the set of key-bindings.

**Returns:** the name

---

#### getName

String

getName()

Fetches the name of the set of key-bindings.

getDefaultAction

```java
Action
getDefaultAction()
```

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it. Typically this
would be some action that inserts text so that
the keymap doesn't require an action for each
possible key.

**Returns:** the default action

---

#### getDefaultAction

Action

getDefaultAction()

Fetches the default action to fire if a
key is typed (i.e. a KEY_TYPED KeyEvent is received)
and there is no binding for it. Typically this
would be some action that inserts text so that
the keymap doesn't require an action for each
possible key.

setDefaultAction

```java
void setDefaultAction​(
Action
a)
```

Set the default action to fire if a key is typed.

**Parameters:** a

- the action

---

#### setDefaultAction

void setDefaultAction​(

Action

a)

Set the default action to fire if a key is typed.

getAction

```java
Action
getAction​(
KeyStroke
key)
```

Fetches the action appropriate for the given symbolic
event sequence. This is used by JTextController to
determine how to interpret key sequences. If the
binding is not resolved locally, an attempt is made
to resolve through the parent keymap, if one is set.

**Parameters:** key

- the key sequence
**Returns:** the action associated with the key
sequence if one is defined, otherwise

null

---

#### getAction

Action

getAction​(

KeyStroke

key)

Fetches the action appropriate for the given symbolic
event sequence. This is used by JTextController to
determine how to interpret key sequences. If the
binding is not resolved locally, an attempt is made
to resolve through the parent keymap, if one is set.

getBoundKeyStrokes

```java
KeyStroke
[] getBoundKeyStrokes()
```

Fetches all of the keystrokes in this map that
are bound to some action.

**Returns:** the list of keystrokes

---

#### getBoundKeyStrokes

KeyStroke

[] getBoundKeyStrokes()

Fetches all of the keystrokes in this map that
are bound to some action.

getBoundActions

```java
Action
[] getBoundActions()
```

Fetches all of the actions defined in this keymap.

**Returns:** the list of actions

---

#### getBoundActions

Action

[] getBoundActions()

Fetches all of the actions defined in this keymap.

getKeyStrokesForAction

```java
KeyStroke
[] getKeyStrokesForAction​(
Action
a)
```

Fetches the keystrokes that will result in
the given action.

**Parameters:** a

- the action
**Returns:** the list of keystrokes

---

#### getKeyStrokesForAction

KeyStroke

[] getKeyStrokesForAction​(

Action

a)

Fetches the keystrokes that will result in
the given action.

isLocallyDefined

```java
boolean isLocallyDefined​(
KeyStroke
key)
```

Determines if the given key sequence is locally defined.

**Parameters:** key

- the key sequence
**Returns:** true if the key sequence is locally defined else false

---

#### isLocallyDefined

boolean isLocallyDefined​(

KeyStroke

key)

Determines if the given key sequence is locally defined.

addActionForKeyStroke

```java
void addActionForKeyStroke​(
KeyStroke
key,

Action
a)
```

Adds a binding to the keymap.

**Parameters:** key

- the key sequence
**Parameters:** a

- the action

---

#### addActionForKeyStroke

void addActionForKeyStroke​(

KeyStroke

key,

Action

a)

Adds a binding to the keymap.

removeKeyStrokeBinding

```java
void removeKeyStrokeBinding​(
KeyStroke
keys)
```

Removes a binding from the keymap.

**Parameters:** keys

- the key sequence

---

#### removeKeyStrokeBinding

void removeKeyStrokeBinding​(

KeyStroke

keys)

Removes a binding from the keymap.

removeBindings

```java
void removeBindings()
```

Removes all bindings from the keymap.

---

#### removeBindings

void removeBindings()

Removes all bindings from the keymap.

getResolveParent

```java
Keymap
getResolveParent()
```

Fetches the parent keymap used to resolve key-bindings.

**Returns:** the keymap

---

#### getResolveParent

Keymap

getResolveParent()

Fetches the parent keymap used to resolve key-bindings.

setResolveParent

```java
void setResolveParent​(
Keymap
parent)
```

Sets the parent keymap, which will be used to
resolve key-bindings.
The behavior is unspecified if a

Keymap

has itself
as one of its resolve parents.

**Parameters:** parent

- the parent keymap

---

#### setResolveParent

void setResolveParent​(

Keymap

parent)

Sets the parent keymap, which will be used to
resolve key-bindings.
The behavior is unspecified if a

Keymap

has itself
as one of its resolve parents.

---

