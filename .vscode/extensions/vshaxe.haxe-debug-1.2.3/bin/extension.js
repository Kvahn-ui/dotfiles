// Generated by Haxe 4.0.0-rc.4+672c3f246
(function ($hx_exports, $global) { "use strict";
class Extension {
	static main(context) {
		Vscode.debug.registerDebugConfigurationProvider("fdb",{ resolveDebugConfiguration : Extension.resolveDebugConfiguration});
	}
	static resolveDebugConfiguration(folder,config,token) {
		if(config.type == null) {
			return null;
		}
		return config;
	}
}
$hx_exports["activate"] = Extension.main;
var Vscode = require("vscode");
})(typeof exports != "undefined" ? exports : typeof window != "undefined" ? window : typeof self != "undefined" ? self : this, {});
