/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */

import SocialSharing from '@codesyntax/volto-social-sharing/SocialSharing';
import {DEFAULT_SOCIAL} from '@codesyntax/volto-social-sharing/defaultSettings';

// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

// Push new item
DEFAULT_SOCIAL.push({
  name: "Instagram",
  fa_name: ["fab", "instagram"],
  color: "#c8232c",
  sharing_url: "http://instagram.com/?url=",
  id: "pt"
});

export default function applyConfig(config) {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['es'],
    defaultLanguage: 'es',
    appExtras: [
      ...config.settings.appExtras,
      {
        match: '',
        component: SocialSharing,
        props:{
         socialElements: DEFAULT_SOCIAL
        }
      },
    ],
  };
  return config;
}
